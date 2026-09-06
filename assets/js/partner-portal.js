/* 區代專區與拓案專區共用登入、資料顯示及匯出邏輯。 */
(() => {
  if (window.flwAuthRedirecting) return;
  const config = window.PARTNER_PORTAL_CONFIG;
const sb = supabase.createClient('https://femuufnveodwcnusuthy.supabase.co', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZlbXV1Zm52ZW9kd2NudXN1dGh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE2ODQ0MjcsImV4cCI6MjA5NzI2MDQyN30.TQER06oE6_CT8nHprhPlf79qjbcsgS4nhEJs5VUregQ', { auth: { experimental: { passkey: true }, persistSession: true, autoRefreshToken: true } });
  let currentUser = null;
  let rows = { projects: [], sales: [], commissions: [] };
  const $ = id => document.getElementById(id);
  const money = value => new Intl.NumberFormat('zh-TW', { style: 'currency', currency: 'TWD', maximumFractionDigits: 0 }).format(Number(value || 0));
  const date = value => value ? new Date(value).toLocaleDateString('zh-TW') : '—';
  const safe = value => String(value ?? '').replace(/[&<>"']/g, char => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[char]));
  const statusLabel = { pending: '待審核', approved: '已核准', rejected: '未通過' };
  const badge = value => '<span class="pp-badge ' + safe(value) + '">' + (statusLabel[value] || safe(value)) + '</span>';

  function message(text, type = 'error') { const node = $('ppMessage'); node.textContent = text; node.className = 'pp-message ' + type; }
  function clearMessage() { $('ppMessage').className = 'pp-message'; $('ppMessage').textContent = ''; }
  function toggleLogin(mode) { $('ppLoginControls').style.display = mode === 'login' ? '' : 'none'; $('ppResetControls').style.display = mode === 'reset' ? '' : 'none'; }
  function callbackMode() { return /(?:[?&#])type=(invite|recovery)/i.test(location.search + '&' + location.hash); }
  function unitText(unit) { return unit ? String(unit.floor).padStart(2, '0') + '-' + unit.unit_no : '—'; }
  function relation(value) { return Array.isArray(value) ? value[0] : value; }

  async function boot() {
    if (callbackMode()) { toggleLogin('reset'); message('請先設定登入密碼，完成後即可進入' + config.title + '。', 'success'); }
    const { data: { user } } = await sb.auth.getUser();
    if (user && !callbackMode()) await enter(user);
  }
  async function enter(user) {
    const { data: role, error } = await sb.from('user_roles').select('role').eq('user_id', user.id).maybeSingle();
    if (error || role?.role !== config.role) { await sb.auth.signOut(); toggleLogin('login'); message('此帳號沒有' + config.title + '權限，請聯絡譽誠平台管理員。'); return; }
    const { data: partner } = await sb.from('platform_partners').select('display_name,region,status').eq('user_id', user.id).maybeSingle();
    if (!partner || partner.status !== 'active') { await sb.auth.signOut(); toggleLogin('login'); message('此合作帳戶目前未啟用，請聯絡譽誠平台管理員。'); return; }
    currentUser = user;
    $('ppLogin').style.display = 'none'; $('ppDashboard').style.display = 'block';
    $('ppUserName').textContent = partner.display_name;
    $('ppUserMeta').textContent = config.role === 'regional_agent' ? (partner.region || '尚未設定負責區域') : '案源拓展夥伴';
    await loadAll();
  }
  async function loadAll() {
    const projectQuery = sb.from('projects').select('id,name,location,address,price,builder,region,approval_status,published,platform_commission_rate,regional_agent_rate,sourcing_partner_rate,created_at,updated_at').order('created_at', { ascending: false });
    const projectResult = config.role === 'regional_agent'
      ? await projectQuery.or('regional_agent_user_id.eq.' + currentUser.id + ',submitted_by.eq.' + currentUser.id)
      : await projectQuery.eq('sourcing_partner_user_id', currentUser.id);
    rows.projects = projectResult.data || [];
    const { data: sales } = await sb.from('sale_submissions').select('id,deal_price,deal_date,status,created_at,projects(name),units(floor,unit_no,unit_type)').order('deal_date', { ascending: false });
    const { data: commissions } = await sb.from('commission_allocations').select('id,allocation_role,recipient_name,commission_base_amount,share_rate,estimated_amount,created_at,projects(name),units(floor,unit_no,unit_type)').order('created_at', { ascending: false });
    rows.sales = sales || []; rows.commissions = commissions || [];
    renderOverview(); renderProjects(); renderSales(); renderCommissions();
  }
  function renderOverview() {
    const approved = rows.sales.filter(row => row.status === 'approved');
    const total = rows.commissions.reduce((sum, row) => sum + Number(row.estimated_amount || 0), 0);
    $('ppStatProjects').textContent = rows.projects.filter(row => row.approval_status === 'approved').length;
    $('ppStatSales').textContent = approved.length;
    $('ppStatCommission').textContent = money(total);
    $('ppOverviewProjects').innerHTML = rows.projects.length ? rows.projects.slice(0, 5).map(row => '<tr><td><strong>' + safe(row.name) + '</strong><br><span style="font-size:.72rem;color:#617285">' + safe(row.location || '—') + '</span></td><td>' + badge(row.approval_status) + '</td><td>' + safe(row.region || '—') + '</td></tr>').join('') : '<tr><td colspan="3" class="pp-empty">尚未指派或提交建案。</td></tr>';
  }
  function renderProjects() {
    $('ppProjectRows').innerHTML = rows.projects.length ? rows.projects.map(row => '<tr><td><strong>' + safe(row.name) + '</strong><br><span style="font-size:.72rem;color:#617285">' + safe(row.address || row.location || '—') + '</span></td><td>' + safe(row.builder || '—') + '</td><td>' + safe(row.region || '—') + '</td><td>' + badge(row.approval_status) + '</td><td>' + Number(row.platform_commission_rate || 0) + '%</td></tr>').join('') : '<tr><td colspan="5" class="pp-empty">尚無建案資料。</td></tr>';
  }
  function renderSales() {
    $('ppSalesRows').innerHTML = rows.sales.length ? rows.sales.map(row => '<tr><td><strong>' + safe(relation(row.projects)?.name || '—') + '</strong></td><td>' + safe(unitText(relation(row.units))) + '</td><td>' + money(row.deal_price) + '</td><td>' + date(row.deal_date) + '</td><td>' + badge(row.status) + '</td></tr>').join('') : '<tr><td colspan="5" class="pp-empty">尚無成交申報資料。</td></tr>';
  }
  function renderCommissions() {
    const total = rows.commissions.reduce((sum, row) => sum + Number(row.estimated_amount || 0), 0);
    $('ppCommissionTotal').textContent = money(total);
    $('ppCommissionRows').innerHTML = rows.commissions.length ? rows.commissions.map(row => '<tr><td><strong>' + safe(relation(row.projects)?.name || '—') + '</strong></td><td>' + safe(unitText(relation(row.units))) + '</td><td>' + money(row.commission_base_amount) + '</td><td>' + Number(row.share_rate || 0) + '%</td><td><strong>' + money(row.estimated_amount) + '</strong></td><td>' + date(row.created_at) + '</td></tr>').join('') : '<tr><td colspan="6" class="pp-empty">尚無已核准成交，因此沒有暫估應得獎金。</td></tr>';
  }
  function downloadCsv(filename, headers, values) {
    const csv = '\uFEFF' + [headers, ...values].map(row => row.map(cell => '"' + String(cell ?? '').replace(/"/g, '""') + '"').join(',')).join('\r\n');
    const link = document.createElement('a'); link.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv;charset=utf-8' })); link.download = filename; link.click(); URL.revokeObjectURL(link.href);
  }
  window.ppExportCommissions = () => downloadCsv(config.filePrefix + '-暫估獎金.csv', ['建案', '戶別', '平台佣金基礎', '分潤比例', '暫估獎金', '納入日期'], rows.commissions.map(row => [relation(row.projects)?.name, unitText(relation(row.units)), row.commission_base_amount, row.share_rate + '%', row.estimated_amount, date(row.created_at)]));
  window.ppExportSales = () => downloadCsv(config.filePrefix + '-成交紀錄.csv', ['建案', '戶別', '成交價', '成交日期', '審核狀態'], rows.sales.map(row => [relation(row.projects)?.name, unitText(relation(row.units)), row.deal_price, date(row.deal_date), statusLabel[row.status] || row.status]));
  window.ppPrint = () => window.print();
  window.ppSwitch = panel => { document.querySelectorAll('.pp-panel').forEach(node => node.classList.remove('active')); document.querySelectorAll('.pp-nav').forEach(node => node.classList.remove('active')); $('ppPanel' + panel).classList.add('active'); document.querySelector('[data-panel="' + panel + '"]').classList.add('active'); };
  window.ppLogin = async () => { clearMessage(); const email = $('ppEmail').value.trim().toLowerCase(), password = $('ppPassword').value; if (!email || !password) return message('請輸入 Email 與密碼。'); const { error } = await sb.auth.signInWithPassword({ email, password }); if (error) return message('登入失敗：請確認 Email、密碼，或先完成邀請信中的密碼設定。'); const { data: { user } } = await sb.auth.getUser(); if (user) await enter(user); };
  window.ppPasskey = async () => { clearMessage(); if (!window.PublicKeyCredential) return message('此瀏覽器不支援 Passkey，請使用 Email 與密碼登入。'); const { error } = await sb.auth.signInWithPasskey(); if (error) return message('Passkey 登入未完成：' + error.message); const { data: { user } } = await sb.auth.getUser(); if (user) await enter(user); };
  window.ppEnablePasskey = async () => { const { error } = await sb.auth.registerPasskey(); if (error) return alert('Passkey 設定未完成：' + error.message); alert('此裝置已可使用人臉／Passkey 登入。'); };
  window.ppResetRequest = async () => { const email = $('ppEmail').value.trim().toLowerCase(); if (!/^\S+@\S+\.\S+$/.test(email)) return message('請先輸入有效 Email。'); const { error } = await sb.auth.resetPasswordForEmail(email, { redirectTo: location.origin + location.pathname }); if (error) return message('重設信寄送失敗，請稍後再試。'); message('重設連結已寄出，請至信箱開啟後設定新密碼。', 'success'); };
  window.ppSavePassword = async () => { const password = $('ppNewPassword').value, confirmPassword = $('ppConfirmPassword').value; if (password.length < 12) return message('新密碼至少需要 12 個字元。'); if (password !== confirmPassword) return message('兩次輸入的新密碼不一致。'); const { error } = await sb.auth.updateUser({ password }); if (error) return message('設定失敗：' + error.message); history.replaceState(null, '', location.pathname); const { data: { user } } = await sb.auth.getUser(); if (user) await enter(user); };
  window.ppBackToLogin = () => { history.replaceState(null, '', location.pathname); toggleLogin('login'); clearMessage(); };
  window.ppLogout = async () => { await sb.auth.signOut(); currentUser = null; $('ppDashboard').style.display = 'none'; $('ppLogin').style.display = ''; toggleLogin('login'); clearMessage(); };
  window.ppSubmitProject = async () => {
    const value = id => $(id).value.trim(), name = value('ppProjectName'), location = value('ppProjectLocation'), price = value('ppProjectPrice'), description = value('ppProjectDescription');
    const rate = Number(value('ppProjectCommissionRate')), regionalRate = Number(value('ppProjectRegionalRate'));
    if (!name || !location || !price || !description) return alert('請填寫建案名稱、地區、價格與建案說明。');
    if (!(rate > 0 && rate <= 100) || !(regionalRate >= 0 && regionalRate <= 100)) return alert('請填寫有效的平台佣金比例與區代比例。');
    const cover = value('ppProjectCover');
    const payload = { name, location, address: value('ppProjectAddress') || null, price, description, builder: value('ppProjectBuilder') || null, region: value('ppProjectRegion') || null, platform_commission_rate: rate, regional_agent_rate: regionalRate, sourcing_partner_rate: 0, submitted_by: currentUser.id, regional_agent_user_id: currentUser.id, approval_status: 'pending', published: false, images: cover ? [cover] : [] };
    const button = $('ppProjectSubmit'); button.disabled = true; button.textContent = '送審中…';
    const { error } = await sb.from('projects').insert(payload); button.disabled = false; button.textContent = '送交管理員審核';
    if (error) return alert('提案未送出：' + error.message);
    $('ppProjectForm').reset(); alert('建案提案已送出，待管理員審核通過後才會上架主網站。'); await loadAll(); ppSwitch('Projects');
  };
  sb.auth.onAuthStateChange((event) => { if (event === 'PASSWORD_RECOVERY') { toggleLogin('reset'); message('請設定新的登入密碼。', 'success'); } });
  document.addEventListener('DOMContentLoaded', boot);
})();
