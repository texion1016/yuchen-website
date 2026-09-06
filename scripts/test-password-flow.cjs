// Browser regression tests: no production users are created and no email is sent.
const { chromium } = require(process.env.FLW_NODE_MODULES + '/playwright');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const server = http.createServer((req, res) => {
  const target = path.resolve(root, '.' + new URL(req.url, 'http://local').pathname);
  if (!target.startsWith(root + path.sep) && target !== root) { res.writeHead(403).end(); return; }
  const file = target === root ? path.join(root, 'index.html') : target;
  try {
    const mime = { '.js':'text/javascript', '.html':'text/html', '.svg':'image/svg+xml', '.png':'image/png', '.css':'text/css' };
    res.setHeader('Content-Type', mime[path.extname(file)] || 'application/octet-stream');
    res.end(fs.readFileSync(file));
  } catch { res.writeHead(404).end(); }
});
const mockSdk = `window.supabase = { createClient() {
  const initialHash = location.hash;
  const initialQuery = location.search;
  window.mockAuth = { user: { id: 'test-user', email: 'test@example.invalid' }, role: 'broker', saves: 0, updateError: false };
  return {
    auth: {
      initialize: async () => { history.replaceState(null, '', location.pathname); return {error: initialHash.includes('invalid') ? {message:'expired'} : null}; },
      getUser: async () => ({data:{user:window.mockAuth.user},error:null}),
      updateUser: async () => { window.mockAuth.saves++; return {error:window.mockAuth.updateError ? {code:'same_password'} : null}; },
      signOut: async () => { window.mockAuth.user = null; return {error:null}; },
      verifyOtp: async () => ({error:null}),
      onAuthStateChange: () => ({data:{subscription:{unsubscribe(){}}}})
    },
    from: () => ({select: () => ({eq: () => ({maybeSingle: async () => ({data:{role:window.mockAuth.role},error:null})})})})
  };
}};`;
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = 'http://127.0.0.1:' + server.address().port;
  const browser = await chromium.launch({headless:true, channel:'chrome'});
  const out = path.join(root, 'test-results'); fs.mkdirSync(out, {recursive:true});
  let passes = 0;
  async function setup() {
    const context = await browser.newContext();
    await context.route('**/*', async route => {
      const url = route.request().url();
      if (url.includes('supabase-js@')) return route.fulfill({contentType:'text/javascript',body:mockSdk});
      if (!url.startsWith(base)) return route.abort();
      return route.continue();
    });
    return {context, page:await context.newPage()};
  }
  async function ready(page, source = '/', type = 'invite') {
    await page.goto(base + source + '#access_token=test&refresh_token=test&type=' + type);
    await page.waitForURL('**/password-setup.html*');
    await page.locator('#passwordForm:not([hidden])').waitFor();
    assert.equal(await page.evaluate(() => mockAuth.saves), 0);
  }
  try {
    for (const source of ['/', '/yc-console-8k3n7q.html','/regional-portal.html','/sourcing-portal.html']) {
      for (const type of ['invite','recovery']) {
        const {context,page} = await setup();
        await ready(page,source,type);
        assert.equal(await page.locator('#heading').innerText(), type === 'invite' ? '設定登入密碼' : '重設登入密碼');
        await page.reload();
        await page.locator('#passwordForm:not([hidden])').waitFor();
        await page.goto(base + '/');
        await page.waitForURL('**/password-setup.html*');
        await page.locator('#passwordForm:not([hidden])').waitFor();
        await context.close(); passes++;
      }
    }
    // Exercise the real SDK too: only its HTTP responses are mocked.
    const sdkUrl = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.115.0/dist/umd/supabase.js';
    const sdkResponse = await fetch(sdkUrl);
    assert.equal(sdkResponse.status,200);
    const realSdk = await sdkResponse.text();
    for (const type of ['invite','recovery']) {
      const context = await browser.newContext();
      const uid = '11111111-1111-4111-8111-111111111111';
      const user = {id:uid,aud:'authenticated',role:'authenticated',email:'test@example.invalid',app_metadata:{provider:'email',providers:['email']},user_metadata:{},created_at:new Date().toISOString()};
      const jwt = Buffer.from(JSON.stringify({alg:'HS256',typ:'JWT'})).toString('base64url')+'.'+Buffer.from(JSON.stringify({sub:uid,aud:'authenticated',role:'authenticated',exp:Math.floor(Date.now()/1000)+3600})).toString('base64url')+'.test-signature';
      let saved = 0;
      await context.route('**/*', route => {
        const url = route.request().url();
        if (url.includes('supabase-js@')) return route.fulfill({contentType:'text/javascript',body:realSdk});
        if (url.includes('/auth/v1/user')) {
          if(route.request().method()==='PUT') saved++;
          return route.fulfill({contentType:'application/json',body:JSON.stringify(user)});
        }
        if (url.includes('/rest/v1/user_roles')) return route.fulfill({contentType:'application/json',body:'{"role":"broker"}'});
        if (url === base+'/?portal=broker') return route.fulfill({contentType:'text/html',body:'<p>Verified destination</p>'});
        if (url.startsWith(base)) return route.continue();
        return route.abort();
      });
      const page = await context.newPage();
      await page.goto(base+'/#access_token='+jwt+'&refresh_token=test-refresh&expires_in=3600&token_type=bearer&type='+type);
      await page.waitForURL('**/password-setup.html*');
      await page.locator('#passwordForm:not([hidden])').waitFor();
      assert.equal(saved,0);
      await page.reload();
      await page.locator('#passwordForm:not([hidden])').waitFor();
      await page.locator('#password').fill('New-password-2026');
      await page.locator('#confirmation').fill('New-password-2026');
      await page.locator('#savePassword').click();
      await page.waitForURL(base+'/?portal=broker');
      assert.equal(saved,1);
      await context.close(); passes++;
    }
    const roles = {admin:'/yc-console-8k3n7q.html',broker:'/?portal=broker',builder:'/?portal=builder',regional_agent:'/regional-portal.html',sourcing_partner:'/sourcing-portal.html'};
    for (const [role,target] of Object.entries(roles)) {
      const {context,page} = await setup(); await ready(page);
      await page.evaluate(role => {mockAuth.role=role;},role);
      await page.locator('#password').fill('New-password-2026');
      await page.locator('#confirmation').fill('Different-password');
      await page.locator('#savePassword').click();
      assert.match(await page.locator('#message').innerText(), /不一致/);
      assert.equal(await page.evaluate(() => mockAuth.saves),0);
      await page.locator('#confirmation').fill('New-password-2026');
      await page.evaluate(() => {mockAuth.updateError=true;});
      await page.locator('#savePassword').click();
      assert.match(await page.locator('#message').innerText(), /原密碼/);
      assert.equal(await page.evaluate(() => sessionStorage.getItem('flw-password-pending')),'invite');
      await page.evaluate(() => {mockAuth.updateError=false;});
      await page.route(base+target, route => route.fulfill({contentType:'text/html',body:'<p>Verified destination</p>'}));
      await page.locator('#savePassword').click();
      await page.waitForURL(base+target);
      assert.equal(await page.evaluate(() => sessionStorage.getItem('flw-password-pending')),null);
      await context.close(); passes++;
    }
    for (const suffix of ['#access_token=invalid&type=invite','#error=access_denied&type=recovery','?type=invite']) {
      const {context,page} = await setup();
      await page.goto(base+'/password-setup.html'+suffix);
      await page.waitForFunction(() => document.getElementById('message').className === 'error');
      assert.equal(await page.locator('#passwordForm').isVisible(), false);
      assert.equal(await page.evaluate(() => mockAuth.saves),0);
      await context.close(); passes++;
    }
    {
      const {context,page} = await setup(); await ready(page);
      await page.evaluate(() => {mockAuth.user = {id:'another-user'};});
      await page.locator('#password').fill('New-password-2026');
      await page.locator('#confirmation').fill('New-password-2026');
      await page.locator('#savePassword').click();
      assert.equal(await page.locator('#passwordForm').isVisible(),false);
      assert.equal(await page.evaluate(() => mockAuth.saves),0);
      await context.close(); passes++;
    }
    for (const width of [1440,390]) {
      const {context,page} = await setup(); await page.setViewportSize({width,height:900});
      await ready(page);
      assert.ok(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth));
      await page.screenshot({path:path.join(out,'password-'+width+'.png'),fullPage:true});
      await context.close();
    }
    {
      const {context,page} = await setup(); await page.setViewportSize({width:1440,height:900});
      await page.addInitScript(() => {
        sessionStorage.setItem('splSeenV9','1');
        Object.defineProperty(navigator,'share',{value:undefined,configurable:true});
        Object.defineProperty(navigator,'clipboard',{value:{writeText:async value=>{window.copiedShare=value;}},configurable:true});
      });
      await page.goto(base+'/'); await page.locator('#shareWebsite').click();
      assert.equal(await page.evaluate(() => window.copiedShare),'https://yuchen-realty.com/');
      assert.match(await page.locator('#shareStatus').innerText(),/已複製/);
      assert.equal(await page.locator('#desktopInstallButton').evaluate(el=>getComputedStyle(el).backgroundColor),'rgb(24, 51, 79)');
      await page.locator('#shareWebsite').scrollIntoViewIfNeeded();
      await page.screenshot({path:path.join(out,'homepage-desktop.png')});
      await page.setViewportSize({width:390,height:844});
      await page.locator('#shareWebsite').scrollIntoViewIfNeeded();
      await page.screenshot({path:path.join(out,'homepage-mobile.png')});
      await page.goto(base+'/photo/icons/qr-site-current.svg');
      await page.locator('svg').screenshot({path:path.join(out,'qr.png')});
      await context.close(); passes++;
    }
    console.log('PASS '+passes+' auth/share scenarios; desktop/mobile screenshots saved to test-results.');
  } finally { await browser.close(); server.close(); }
})().catch(error => {console.error(error);server.close();process.exitCode=1;});
