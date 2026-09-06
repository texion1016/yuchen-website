(function () {
  'use strict';
  var query = new URLSearchParams(location.search);
  var hash = new URLSearchParams(location.hash.slice(1));
  var storedType = '', expectedUser = '';
  try {
    storedType = sessionStorage.getItem('flw-password-pending') || '';
    expectedUser = sessionStorage.getItem('flw-password-user') || '';
  } catch (_) {}
  var type = hash.get('type') || query.get('type') || storedType;
  var tokenHash = query.get('token_hash');
  var hasCredentials = !!(hash.get('access_token') || query.get('code') || tokenHash);
  var form = document.getElementById('passwordForm');
  var message = document.getElementById('message');
  var button = document.getElementById('savePassword');
  var verifiedUser = null, saving = false, sb = null;
  function tell(text, error) { message.textContent = text; message.className = error ? 'error' : ''; }
  function clearPending() {
    try {
      sessionStorage.removeItem('flw-password-pending');
      sessionStorage.removeItem('flw-password-user');
    } catch (_) {}
  }
  function scrubUrl() { history.replaceState(null, '', '/password-setup.html'); }
  function fail() {
    form.hidden = true;
    scrubUrl();
    tell('連結已失效、已使用或無法驗證。請回原專區重新寄送重設密碼信，或請管理員協助。', true);
  }
  document.getElementById('cancelSetup').addEventListener('click', async function () {
    this.disabled = true;
    try {
      if (sb) {
        var result = await sb.auth.signOut({ scope: 'local' });
        if (result.error) throw result.error;
      }
      clearPending();
      location.replace('/');
    } catch (_) {
      this.disabled = false;
      tell('登出未完成，請確認網路連線後重試。', true);
    }
  });
  form.addEventListener('submit', async function (event) {
    event.preventDefault();
    if (saving || !verifiedUser) return;
    var password = document.getElementById('password').value;
    if (password.length < 12) return tell('新密碼至少需要 12 個字元。', true);
    if (password !== document.getElementById('confirmation').value) return tell('兩次輸入的密碼不一致，請重新確認。', true);
    saving = true; button.disabled = true; button.textContent = '儲存中…';
    try {
      var current = await sb.auth.getUser();
      if (current.error || !current.data.user || current.data.user.id !== verifiedUser.id) {
        verifiedUser = null; fail(); return;
      }
      var result = await sb.auth.updateUser({ password: password });
      if (result.error) {
        tell(result.error.code === 'same_password'
          ? '新密碼不能與原密碼相同，請換一組。'
          : '密碼未儲存，請確認網路並使用至少 12 個字元的新密碼後重試；若連結失效，請重新寄送重設信。', true);
        return;
      }
      document.getElementById('password').value = '';
      document.getElementById('confirmation').value = '';
      clearPending();
      var roleResult = await sb.from('user_roles').select('role').eq('user_id', verifiedUser.id).maybeSingle();
      var destinations = {
        admin: '/yc-console-8k3n7q.html',
        broker: '/?portal=broker',
        builder: '/?portal=builder',
        regional_agent: '/regional-portal.html',
        sourcing_partner: '/sourcing-portal.html'
      };
      if (roleResult.error || !destinations[roleResult.data?.role]) {
        form.hidden = true;
        tell('密碼已儲存。專區權限暫時無法確認，請稍後由首頁登入，或聯絡管理員。', true);
        return;
      }
      try { sessionStorage.setItem('splSeenV9', '1'); } catch (_) {}
      tell('密碼已儲存，正在開啟你的專區。', false);
      location.replace(destinations[roleResult.data.role]);
    } catch (_) {
      tell('網路連線中斷，請確認連線後再試。', true);
    } finally {
      saving = false; button.disabled = false; button.textContent = '儲存密碼並進入專區';
    }
  });
  (async function () {
    try {
      if (!window.supabase) { tell('登入服務載入失敗，請重新整理後再試。', true); return; }
      sb = supabase.createClient('https://femuufnveodwcnusuthy.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZlbXV1Zm52ZW9kd2NudXN1dGh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE2ODQ0MjcsImV4cCI6MjA5NzI2MDQyN30.TQER06oE6_CT8nHprhPlf79qjbcsgS4nhEJs5VUregQ', {
        auth: { persistSession: true, autoRefreshToken: true, detectSessionInUrl: !tokenHash }
      });
      if (hash.has('error') || query.has('error') || !['invite', 'recovery'].includes(type)) { fail(); return; }
      // Never use an unrelated previously signed-in account to accept a broken email link.
      if (!hasCredentials && !expectedUser) { fail(); return; }
      document.getElementById('heading').textContent = type === 'invite' ? '設定登入密碼' : '重設登入密碼';
      var init = await sb.auth.initialize();
      if (init.error) { fail(); return; }
      if (tokenHash) {
        var verified = await sb.auth.verifyOtp({ token_hash: tokenHash, type: type });
        if (verified.error) { fail(); return; }
      }
      var auth = await sb.auth.getUser();
      if (auth.error || !auth.data.user || (!hasCredentials && auth.data.user.id !== expectedUser)) { fail(); return; }
      verifiedUser = auth.data.user;
      try {
        sessionStorage.setItem('flw-password-pending', type);
        sessionStorage.setItem('flw-password-user', verifiedUser.id);
      } catch (_) {}
      scrubUrl();
      document.getElementById('account').textContent = '設定帳號：' + verifiedUser.email;
      form.hidden = false;
      tell('信箱已確認，請設定密碼。', false);
      document.getElementById('password').focus();
    } catch (_) { tell('驗證暫時無法完成，請確認網路後重新整理。', true); }
  })();
})();
