# -*- coding: utf-8 -*-
"""
fix11.py - 接入 Supabase：真實登入、客戶報備存DB、我的報備從DB讀取
"""

SUPABASE_URL = "https://femuufnveodwcnusuthy.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZlbXV1Zm52ZW9kd2NudXN1dGh5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE2ODQ0MjcsImV4cCI6MjA5NzI2MDQyN30.TQER06oE6_CT8nHprhPlf79qjbcsgS4nhEJs5VUregQ"

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. 在 </head> 前注入 Supabase SDK + 設定 ────────────────────────────────
SUPABASE_SDK = f"""
  <!-- Supabase SDK -->
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script>
    const _SB_URL = '{SUPABASE_URL}';
    const _SB_KEY = '{SUPABASE_KEY}';
    const _sb = supabase.createClient(_SB_URL, _SB_KEY);
  </script>
"""
html = html.replace('</head>', SUPABASE_SDK + '</head>', 1)
print("1. Supabase SDK:", "OK")

# ── 2. 替換仲介 Overlay 的 JS 邏輯（接真實 DB）────────────────────────────
OLD_BOV_JS = """<script>
// ── Broker Overlay V2 Logic ──────────────────────────────────────────────────
let bovCurrentUser = null;

function openBrokerOverlay() {
  document.getElementById('brokerOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  if (bovCurrentUser) {
    showBovLoggedIn();
  }
}
function closeBrokerOv() {
  document.getElementById('brokerOverlay').classList.remove('open');
  document.body.style.overflow = '';
}
function switchBovTab(tab) {
  document.querySelectorAll('.bov-tab').forEach((t,i) => t.classList.remove('active'));
  document.querySelectorAll('.bov-panel').forEach(p => p.classList.remove('active'));
  const tabs = { login:'bovLogin', register:'bovRegister', report:'bovReport', myreg:'bovMyReg' };
  document.getElementById(tabs[tab]).classList.add('active');
  const btnMap = { login:0, register:1, report:2, myreg:3 };
  const allTabs = document.querySelectorAll('.bov-tab');
  allTabs.forEach(t => t.classList.remove('active'));
  // find by onclick
  document.querySelectorAll('.bov-tab').forEach(t => {
    if (t.getAttribute('onclick') && t.getAttribute('onclick').includes("'"+tab+"'")) t.classList.add('active');
  });
}

function showBovMsg(id, msg, type) {
  const el = document.getElementById(id);
  el.textContent = msg; el.className = 'bov-msg ' + type; el.style.display = 'block';
  setTimeout(() => { el.style.display='none'; }, 5000);
}

function showBovLoggedIn() {
  document.getElementById('tabReport').style.display = '';
  document.getElementById('tabMyReg').style.display = '';
  switchBovTab('report');
}

// 產生報備編號
function genRegNo() {
  const now = new Date();
  const d = now.toISOString().slice(2,10).replace(/-/g,'');
  const r = Math.random().toString(36).substr(2,4).toUpperCase();
  return 'YC-' + d + '-' + r;
}

// 本地報備資料（連接 Supabase 前的暫時版本）
function doBrokerLogin() {
  const email = document.getElementById('loginEmail').value.trim();
  const pwd = document.getElementById('loginPwd').value;
  if (!email || !pwd) { showBovMsg('loginMsg','請填寫信箱與密碼','error'); return; }
  // 暫時：模擬登入成功（接 Supabase 後替換）
  bovCurrentUser = { email, name: email.split('@')[0] };
  showBovLoggedIn();
  showBovMsg('loginMsg','登入成功，歡迎回來！','success');
}

function doBrokerRegister() {
  const name = document.getElementById('regName').value.trim();
  const company = document.getElementById('regCompany').value.trim();
  const phone = document.getElementById('regPhone').value.trim();
  const email = document.getElementById('regEmail').value.trim();
  const pwd = document.getElementById('regPwd').value;
  if (!name || !company || !phone || !email || !pwd) {
    showBovMsg('registerMsg','請填寫所有必填欄位','error'); return;
  }
  if (pwd.length < 8) { showBovMsg('registerMsg','密碼至少需要 8 個字元','error'); return; }
  // 暫時：模擬申請成功
  bovCurrentUser = { email, name };
  showBovLoggedIn();
  showBovMsg('registerMsg','申請成功！歡迎加入譽誠聯合銷售平台','success');
}

function doClientReport() {
  const clientName = document.getElementById('rptClientName').value.trim();
  const clientPhone = document.getElementById('rptClientPhone').value.trim();
  const project = document.getElementById('rptProject').value;
  const note = document.getElementById('rptNote').value.trim();
  if (!clientName || !clientPhone || !project) {
    showBovMsg('reportMsg','請填寫客戶姓名、電話與指定建案','error'); return;
  }
  const regNo = genRegNo();
  const record = { regNo, clientName, clientPhone, project, note, date: new Date().toLocaleDateString('zh-TW'), status: 'pending', broker: bovCurrentUser };
  // 存到 localStorage（Supabase 接好後替換）
  const records = JSON.parse(localStorage.getItem('bov_records') || '[]');
  records.unshift(record);
  localStorage.setItem('bov_records', JSON.stringify(records));
  showBovMsg('reportMsg', `報備成功！報備編號：${regNo}`, 'success');
  document.getElementById('rptClientName').value = '';
  document.getElementById('rptClientPhone').value = '';
  document.getElementById('rptProject').value = '';
  document.getElementById('rptNote').value = '';
}

function loadMyRegs() {
  const records = JSON.parse(localStorage.getItem('bov_records') || '[]');
  const el = document.getElementById('myregContent');
  if (records.length === 0) {
    el.innerHTML = '<div class="bov-empty">尚無報備紀錄</div>'; return;
  }
  let rows = records.map(r => `
    <tr>
      <td><span class="bov-reg-no">${r.regNo}</span></td>
      <td>${r.clientName}</td>
      <td>${r.project}</td>
      <td>${r.date}</td>
      <td><span class="bov-status ${r.status}">${r.status === 'pending' ? '待確認' : '已確認'}</span></td>
    </tr>`).join('');
  el.innerHTML = `<table class="bov-reg-table">
    <thead><tr><th>報備編號</th><th>客戶姓名</th><th>建案</th><th>報備日期</th><th>狀態</th></tr></thead>
    <tbody>${rows}</tbody></table>`;
}

// 當切到我的報備時自動載入
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('bovMyReg').addEventListener('transitionend', loadMyRegs);
});
// 修補 switchBovTab 以觸發載入
const _origSwitch = window.switchBovTab;
window.switchBovTab = function(tab) {
  _origSwitch(tab);
  if (tab === 'myreg') loadMyRegs();
};
</script>"""

NEW_BOV_JS = """<script>
// ── Broker Overlay V2 — Supabase 版 ─────────────────────────────────────────
let bovCurrentUser = null; // { id, name, company, email }

// 簡易密碼雜湊（前端用，非加密級別）
async function hashPwd(pwd) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(pwd));
  return Array.from(new Uint8Array(buf)).map(b=>b.toString(16).padStart(2,'0')).join('');
}

function openBrokerOverlay() {
  document.getElementById('brokerOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
  if (bovCurrentUser) showBovLoggedIn();
}
function closeBrokerOv() {
  document.getElementById('brokerOverlay').classList.remove('open');
  document.body.style.overflow = '';
}
function switchBovTab(tab) {
  document.querySelectorAll('.bov-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.bov-tab').forEach(t => t.classList.remove('active'));
  const panelMap = { login:'bovLogin', register:'bovRegister', report:'bovReport', myreg:'bovMyReg' };
  const panel = document.getElementById(panelMap[tab]);
  if (panel) panel.classList.add('active');
  document.querySelectorAll('.bov-tab').forEach(t => {
    if (t.getAttribute('onclick') && t.getAttribute('onclick').includes("'"+tab+"'")) t.classList.add('active');
  });
  if (tab === 'myreg') loadMyRegs();
}
function showBovMsg(id, msg, type) {
  const el = document.getElementById(id);
  if (!el) return;
  el.textContent = msg; el.className = 'bov-msg ' + type; el.style.display = 'block';
  setTimeout(() => { el.style.display = 'none'; }, 6000);
}
function showBovLoggedIn() {
  document.getElementById('tabReport').style.display = '';
  document.getElementById('tabMyReg').style.display = '';
  switchBovTab('report');
}
function genRegNo() {
  const d = new Date().toISOString().slice(2,10).replace(/-/g,'');
  const r = Math.random().toString(36).substr(2,4).toUpperCase();
  return 'YC-' + d + '-' + r;
}

// ── 登入 ──────────────────────────────────────────────────────────────────
async function doBrokerLogin() {
  const email = document.getElementById('loginEmail').value.trim().toLowerCase();
  const pwd = document.getElementById('loginPwd').value;
  if (!email || !pwd) { showBovMsg('loginMsg','請填寫信箱與密碼','error'); return;  }
  const btn = document.querySelector('#bovLogin .bov-btn');
  btn.textContent = '登入中…'; btn.disabled = true;
  try {
    const hash = await hashPwd(pwd);
    const { data, error } = await _sb.from('brokers')
      .select('id,name,company,email,status')
      .eq('email', email)
      .eq('password_hash', hash)
      .single();
    if (error || !data) {
      showBovMsg('loginMsg','帳號或密碼錯誤','error');
    } else if (data.status === 'pending') {
      showBovMsg('loginMsg','帳號審核中，請等待管理員啟用','error');
    } else if (data.status === 'suspended') {
      showBovMsg('loginMsg','帳號已停用，請聯絡管理員','error');
    } else {
      bovCurrentUser = data;
      localStorage.setItem('bov_user', JSON.stringify(data));
      showBovLoggedIn();
    }
  } catch(e) {
    showBovMsg('loginMsg','連線錯誤，請稍後再試','error');
  }
  btn.textContent = '登入'; btn.disabled = false;
}

// ── 申請合作 ──────────────────────────────────────────────────────────────
async function doBrokerRegister() {
  const name = document.getElementById('regName').value.trim();
  const company = document.getElementById('regCompany').value.trim();
  const phone = document.getElementById('regPhone').value.trim();
  const email = document.getElementById('regEmail').value.trim().toLowerCase();
  const pwd = document.getElementById('regPwd').value;
  if (!name||!company||!phone||!email||!pwd) {
    showBovMsg('registerMsg','請填寫所有必填欄位','error'); return;
  }
  if (pwd.length < 8) { showBovMsg('registerMsg','密碼至少需要 8 個字元','error'); return; }
  const btn = document.querySelector('#bovRegister .bov-btn');
  btn.textContent = '送出中…'; btn.disabled = true;
  try {
    const hash = await hashPwd(pwd);
    const { error } = await _sb.from('brokers').insert({
      name, company, phone, email, password_hash: hash, status: 'active'
    });
    if (error) {
      if (error.code === '23505') {
        showBovMsg('registerMsg','此信箱已註冊，請直接登入','error');
      } else {
        showBovMsg('registerMsg','送出失敗：'+error.message,'error');
      }
    } else {
      // 自動登入
      bovCurrentUser = { name, company, email };
      localStorage.setItem('bov_user', JSON.stringify(bovCurrentUser));
      showBovMsg('registerMsg','申請成功！歡迎加入譽誠聯合銷售平台','success');
      setTimeout(() => showBovLoggedIn(), 1200);
    }
  } catch(e) {
    showBovMsg('registerMsg','連線錯誤，請稍後再試','error');
  }
  btn.textContent = '送出申請'; btn.disabled = false;
}

// ── 客戶報備 ──────────────────────────────────────────────────────────────
async function doClientReport() {
  const clientName = document.getElementById('rptClientName').value.trim();
  const clientPhone = document.getElementById('rptClientPhone').value.trim();
  const project = document.getElementById('rptProject').value;
  const note = document.getElementById('rptNote').value.trim();
  if (!clientName||!clientPhone||!project) {
    showBovMsg('reportMsg','請填寫客戶姓名、電話與指定建案','error'); return;
  }
  const btn = document.querySelector('#bovReport .bov-btn');
  btn.textContent = '送出中…'; btn.disabled = true;
  try {
    const regNo = genRegNo();
    const { error } = await _sb.from('client_registrations').insert({
      registration_no: regNo,
      broker_id: bovCurrentUser.id || null,
      broker_name: bovCurrentUser.name,
      broker_company: bovCurrentUser.company,
      project_name: project,
      client_name: clientName,
      client_phone: clientPhone,
      note: note,
      status: 'pending'
    });
    if (error) {
      showBovMsg('reportMsg','送出失敗：'+error.message,'error');
    } else {
      showBovMsg('reportMsg','報備成功！報備編號：' + regNo,'success');
      document.getElementById('rptClientName').value = '';
      document.getElementById('rptClientPhone').value = '';
      document.getElementById('rptProject').value = '';
      document.getElementById('rptNote').value = '';
    }
  } catch(e) {
    showBovMsg('reportMsg','連線錯誤，請稍後再試','error');
  }
  btn.textContent = '送出報備'; btn.disabled = false;
}

// ── 我的報備紀錄 ──────────────────────────────────────────────────────────
async function loadMyRegs() {
  if (!bovCurrentUser) return;
  const el = document.getElementById('myregContent');
  el.innerHTML = '<div class="bov-empty">載入中…</div>';
  try {
    const { data, error } = await _sb.from('client_registrations')
      .select('*')
      .eq('broker_name', bovCurrentUser.name)
      .eq('broker_company', bovCurrentUser.company)
      .order('created_at', { ascending: false });
    if (error || !data || data.length === 0) {
      el.innerHTML = '<div class="bov-empty">尚無報備紀錄</div>'; return;
    }
    const statusLabel = { pending:'待確認', confirmed:'已確認', closed:'已結案' };
    const rows = data.map(r => `
      <tr>
        <td><span class="bov-reg-no">${r.registration_no}</span></td>
        <td>${r.client_name}</td>
        <td>${r.project_name}</td>
        <td>${new Date(r.created_at).toLocaleDateString('zh-TW')}</td>
        <td><span class="bov-status ${r.status}">${statusLabel[r.status]||r.status}</span></td>
      </tr>`).join('');
    el.innerHTML = `<table class="bov-reg-table">
      <thead><tr><th>報備編號</th><th>客戶姓名</th><th>建案</th><th>報備日期</th><th>狀態</th></tr></thead>
      <tbody>${rows}</tbody></table>`;
  } catch(e) {
    el.innerHTML = '<div class="bov-empty">載入失敗，請稍後再試</div>';
  }
}

// ── 頁面載入：恢復登入狀態 ───────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  const saved = localStorage.getItem('bov_user');
  if (saved) {
    try { bovCurrentUser = JSON.parse(saved); } catch(e) {}
  }
});
</script>"""

html = html.replace(OLD_BOV_JS, NEW_BOV_JS, 1)
print("2. Supabase JS:", "OK" if OLD_BOV_JS not in html else "MISS")

# ── 3. 注入管理後台 ────────────────────────────────────────────────────────
ADMIN_HTML = """
<!-- ━━ 管理後台 Overlay ━━ -->
<style>
#adminOverlay{position:fixed;inset:0;z-index:9800;display:none;flex-direction:column;background:var(--void);}
#adminOverlay.open{display:flex;}
.adm-header{display:flex;align-items:center;justify-content:space-between;padding:1rem 2rem;border-bottom:1px solid var(--line);flex-shrink:0;}
.adm-logo{font-family:var(--font-serif);color:var(--gold);font-size:1rem;}
.adm-close{background:none;border:none;color:var(--ink-dim);font-size:1.5rem;cursor:pointer;}
.adm-layout{display:flex;flex:1;overflow:hidden;}
.adm-sidebar{width:180px;border-right:1px solid var(--line);padding:1rem 0;flex-shrink:0;}
.adm-nav-btn{display:block;width:100%;padding:.7rem 1.2rem;background:none;border:none;color:var(--ink-dim);text-align:left;cursor:pointer;font-size:.85rem;transition:all .18s;}
.adm-nav-btn:hover,.adm-nav-btn.active{background:var(--panel-2);color:var(--cyan);}
.adm-content{flex:1;overflow-y:auto;padding:1.5rem 2rem;}
.adm-panel{display:none;}
.adm-panel.active{display:block;}
.adm-title{font-family:var(--font-serif);font-size:1.2rem;margin-bottom:1.2rem;color:var(--ink);}
.adm-table{width:100%;border-collapse:collapse;font-size:.82rem;}
.adm-table th{text-align:left;padding:.6rem .8rem;color:var(--ink-dim);border-bottom:1px solid var(--line);font-weight:500;}
.adm-table td{padding:.65rem .8rem;border-bottom:1px solid rgba(120,180,255,0.06);color:var(--ink);}
.adm-badge{display:inline-block;padding:.15rem .5rem;border-radius:4px;font-size:.72rem;}
.adm-badge.pending{background:rgba(232,193,106,.15);color:var(--gold);}
.adm-badge.active{background:rgba(91,232,255,.12);color:var(--cyan);}
.adm-badge.new{background:rgba(154,134,255,.15);color:var(--violet);}
.adm-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem;margin-bottom:1.5rem;}
.adm-stat-card{background:var(--panel-2);border:1px solid var(--line);border-radius:12px;padding:1.2rem;}
.adm-stat-num{font-family:var(--font-tech);font-size:1.8rem;color:var(--cyan);}
.adm-stat-label{font-size:.75rem;color:var(--ink-dim);margin-top:.3rem;}
.adm-login-box{max-width:360px;margin:5rem auto;}
.adm-empty{text-align:center;padding:3rem;color:var(--ink-dim);}
</style>

<div id="adminOverlay">
  <div class="adm-header">
    <div class="adm-logo">譽誠聯合銷售平台 — 管理後台</div>
    <button class="adm-close" onclick="closeAdmin()">✕</button>
  </div>
  <div id="admLoginWrap" style="flex:1;display:flex;align-items:center;justify-content:center;">
    <div class="adm-login-box">
      <div style="font-family:var(--font-serif);font-size:1.3rem;margin-bottom:1.5rem;color:var(--ink);">管理員登入</div>
      <div id="admLoginErr" class="bov-msg error" style="display:none;">密碼錯誤</div>
      <div class="bov-field"><label>管理員密碼</label><input type="password" id="admPwd" placeholder="••••••••" onkeydown="if(event.key==='Enter')doAdminLogin()" /></div>
      <button class="bov-btn" style="width:100%;margin-top:.5rem;" onclick="doAdminLogin()">登入</button>
    </div>
  </div>
  <div id="admDash" style="display:none;flex:1;overflow:hidden;flex-direction:row;" class="adm-layout">
    <div class="adm-sidebar">
      <button class="adm-nav-btn active" onclick="switchAdmPanel('overview')">總覽</button>
      <button class="adm-nav-btn" onclick="switchAdmPanel('registrations')">客戶報備</button>
      <button class="adm-nav-btn" onclick="switchAdmPanel('bookings')">預約帶看</button>
      <button class="adm-nav-btn" onclick="switchAdmPanel('inquiries')">案件詢問</button>
      <button class="adm-nav-btn" onclick="switchAdmPanel('brokers')">仲介管理</button>
    </div>
    <div class="adm-content">
      <!-- 總覽 -->
      <div class="adm-panel active" id="admOverview">
        <div class="adm-title">總覽儀表板</div>
        <div class="adm-stats" id="admStatsGrid">
          <div class="adm-stat-card"><div class="adm-stat-num" id="statRegs">-</div><div class="adm-stat-label">客戶報備</div></div>
          <div class="adm-stat-card"><div class="adm-stat-num" id="statBook">-</div><div class="adm-stat-label">預約帶看</div></div>
          <div class="adm-stat-card"><div class="adm-stat-num" id="statInq">-</div><div class="adm-stat-label">案件詢問</div></div>
          <div class="adm-stat-card"><div class="adm-stat-num" id="statBrokers">-</div><div class="adm-stat-label">合作仲介</div></div>
        </div>
      </div>
      <!-- 客戶報備 -->
      <div class="adm-panel" id="admRegistrations">
        <div class="adm-title">客戶報備紀錄</div>
        <div id="admRegContent"><div class="adm-empty">載入中…</div></div>
      </div>
      <!-- 預約帶看 -->
      <div class="adm-panel" id="admBookings">
        <div class="adm-title">預約帶看紀錄</div>
        <div id="admBookContent"><div class="adm-empty">載入中…</div></div>
      </div>
      <!-- 案件詢問 -->
      <div class="adm-panel" id="admInquiries">
        <div class="adm-title">案件詢問紀錄</div>
        <div id="admInqContent"><div class="adm-empty">載入中…</div></div>
      </div>
      <!-- 仲介管理 -->
      <div class="adm-panel" id="admBrokers">
        <div class="adm-title">合作仲介名單</div>
        <div id="admBrokerContent"><div class="adm-empty">載入中…</div></div>
      </div>
    </div>
  </div>
</div>

<script>
const ADMIN_PWD = 'yuchen2025admin';

function openAdmin() {
  document.getElementById('adminOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeAdmin() {
  document.getElementById('adminOverlay').classList.remove('open');
  document.body.style.overflow = '';
}
function doAdminLogin() {
  if (document.getElementById('admPwd').value === ADMIN_PWD) {
    document.getElementById('admLoginWrap').style.display = 'none';
    const dash = document.getElementById('admDash');
    dash.style.display = 'flex';
    loadAdmOverview();
  } else {
    document.getElementById('admLoginErr').style.display = 'block';
  }
}
function switchAdmPanel(name) {
  document.querySelectorAll('.adm-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.adm-nav-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('adm' + name.charAt(0).toUpperCase() + name.slice(1)).classList.add('active');
  event.target.classList.add('active');
  const loaders = { registrations: loadAdmRegs, bookings: loadAdmBookings, inquiries: loadAdmInq, brokers: loadAdmBrokers };
  if (loaders[name]) loaders[name]();
}

async function loadAdmOverview() {
  const [r1,r2,r3,r4] = await Promise.all([
    _sb.from('client_registrations').select('id', {count:'exact',head:true}),
    _sb.from('bookings').select('id', {count:'exact',head:true}),
    _sb.from('inquiries').select('id', {count:'exact',head:true}),
    _sb.from('brokers').select('id', {count:'exact',head:true})
  ]);
  document.getElementById('statRegs').textContent = r1.count ?? '-';
  document.getElementById('statBook').textContent = r2.count ?? '-';
  document.getElementById('statInq').textContent = r3.count ?? '-';
  document.getElementById('statBrokers').textContent = r4.count ?? '-';
}

async function loadAdmRegs() {
  const el = document.getElementById('admRegContent');
  const { data } = await _sb.from('client_registrations').select('*').order('created_at',{ascending:false});
  if (!data||!data.length){el.innerHTML='<div class="adm-empty">尚無資料</div>';return;}
  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>報備編號</th><th>仲介</th><th>公司</th><th>客戶</th><th>電話</th><th>建案</th><th>日期</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td style="font-family:var(--font-tech);font-size:.75rem;color:var(--gold)">${r.registration_no}</td>
    <td>${r.broker_name||''}</td><td>${r.broker_company||''}</td>
    <td>${r.client_name}</td><td>${r.client_phone}</td><td>${r.project_name}</td>
    <td>${new Date(r.created_at).toLocaleDateString('zh-TW')}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'待確認',confirmed:'已確認',closed:'結案'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;
}

async function loadAdmBookings() {
  const el = document.getElementById('admBookContent');
  const { data } = await _sb.from('bookings').select('*').order('created_at',{ascending:false});
  if (!data||!data.length){el.innerHTML='<div class="adm-empty">尚無資料</div>';return;}
  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>客戶</th><th>電話</th><th>建案</th><th>預約日期</th><th>時段</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td>${r.client_name}</td><td>${r.client_phone}</td><td>${r.project_name}</td>
    <td>${r.booking_date||''}</td><td>${r.time_slot||''}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'待確認',confirmed:'已確認'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;
}

async function loadAdmInq() {
  const el = document.getElementById('admInqContent');
  const { data } = await _sb.from('inquiries').select('*').order('created_at',{ascending:false});
  if (!data||!data.length){el.innerHTML='<div class="adm-empty">尚無資料</div>';return;}
  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>姓名</th><th>電話</th><th>建案</th><th>詢問內容</th><th>日期</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td>${r.name}</td><td>${r.phone}</td><td>${r.project_name||'未指定'}</td>
    <td style="max-width:200px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">${r.content||''}</td>
    <td>${new Date(r.created_at).toLocaleDateString('zh-TW')}</td>
    <td><span class="adm-badge new">${r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;
}

async function loadAdmBrokers() {
  const el = document.getElementById('admBrokerContent');
  const { data } = await _sb.from('brokers').select('*').order('created_at',{ascending:false});
  if (!data||!data.length){el.innerHTML='<div class="adm-empty">尚無資料</div>';return;}
  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>姓名</th><th>公司</th><th>電話</th><th>信箱</th><th>申請日期</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td>${r.name}</td><td>${r.company}</td><td>${r.phone}</td><td>${r.email}</td>
    <td>${new Date(r.created_at).toLocaleDateString('zh-TW')}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'審核中',active:'啟用',suspended:'停用'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;
}
</script>
"""

# 注入管理後台在 </body> 前
html = html.replace('</body>', ADMIN_HTML + '\n</body>', 1)
print("3. Admin overlay:", "OK")

# ── 4. Footer 加入隱藏的管理後台入口 ──────────────────────────────────────
html = html.replace(
    '© 2025 譽誠聯合銷售平台 All Rights Reserved.',
    '© 2025 譽誠聯合銷售平台 All Rights Reserved. <span onclick="openAdmin()" style="cursor:pointer;opacity:0;user-select:none;" title="admin">·</span>',
    1
)
print("4. Admin entry:", "OK")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix11 done.")
