# -*- coding: utf-8 -*-
"""
fix18.py
1. 客戶報備加入「預約帶看日期 + 帶看時段」欄位
2. 我的報備記錄 / 管理後台同步顯示帶看時間
3. 修正 .bov-body 寬度問題（全寬 myReg）
4. 修正顏色衝突 + 增強整體 UI
5. 品牌開場 Splash 動畫
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ══════════════════════════════════════════════════════════════════════
# 1. 客戶報備表單 — 加入帶看日期 + 時段
# ══════════════════════════════════════════════════════════════════════
OLD_REPORT_FORM = """      <div class="bov-field"><label>備註</label><textarea id="rptNote" rows="3" placeholder="其他說明..."></textarea></div>
      <button class="bov-btn" onclick="doClientReport()">送出報備</button>"""

NEW_REPORT_FORM = """      <div class="bov-row">
        <div class="bov-field">
          <label>預約帶看日期</label>
          <input type="date" id="rptViewDate" />
        </div>
        <div class="bov-field">
          <label>帶看時段</label>
          <select id="rptViewTime">
            <option value="">— 請選擇 —</option>
            <option value="上午 10:00–12:00">上午 10:00–12:00</option>
            <option value="下午 14:00–17:00">下午 14:00–17:00</option>
            <option value="傍晚 17:00–19:00">傍晚 17:00–19:00</option>
            <option value="彈性協調">彈性協調（由顧問確認）</option>
          </select>
        </div>
      </div>
      <div class="bov-field"><label>備註</label><textarea id="rptNote" rows="3" placeholder="其他說明..."></textarea></div>
      <button class="bov-btn" onclick="doClientReport()">送出報備</button>"""

if OLD_REPORT_FORM in html:
    html = html.replace(OLD_REPORT_FORM, NEW_REPORT_FORM, 1)
    print("1a. 報備表單: OK")
else:
    print("1a. 報備表單: MISS")

# ══════════════════════════════════════════════════════════════════════
# 2. doClientReport() — 加入 view_date, view_time
# ══════════════════════════════════════════════════════════════════════
OLD_REPORT_FN = """  const clientName = document.getElementById('rptClientName').value.trim();
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
    });"""

NEW_REPORT_FN = """  const clientName = document.getElementById('rptClientName').value.trim();
  const clientPhone = document.getElementById('rptClientPhone').value.trim();
  const project = document.getElementById('rptProject').value;
  const viewDate = document.getElementById('rptViewDate').value;
  const viewTime = document.getElementById('rptViewTime').value;
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
      view_date: viewDate || null,
      view_time: viewTime || null,
      note: note,
      status: 'pending'
    });"""

if OLD_REPORT_FN in html:
    html = html.replace(OLD_REPORT_FN, NEW_REPORT_FN, 1)
    print("1b. doClientReport: OK")
else:
    print("1b. doClientReport: MISS")

# clear 欄位
OLD_CLEAR = """      document.getElementById('rptClientName').value = '';
      document.getElementById('rptClientPhone').value = '';
      document.getElementById('rptProject').value = '';
      document.getElementById('rptNote').value = '';"""

NEW_CLEAR = """      document.getElementById('rptClientName').value = '';
      document.getElementById('rptClientPhone').value = '';
      document.getElementById('rptProject').value = '';
      document.getElementById('rptViewDate').value = '';
      document.getElementById('rptViewTime').value = '';
      document.getElementById('rptNote').value = '';"""

if OLD_CLEAR in html:
    html = html.replace(OLD_CLEAR, NEW_CLEAR, 1)
    print("1c. 清空欄位: OK")

# ══════════════════════════════════════════════════════════════════════
# 3. loadMyRegs() — 加入帶看時間列
# ══════════════════════════════════════════════════════════════════════
OLD_MY_ROWS = """    const statusLabel = { pending:'待確認', confirmed:'已確認', closed:'已結案' };
    const rows = data.map(r => `
      <tr>
        <td><span class="bov-reg-no">${r.registration_no}</span></td>
        <td>${r.client_name}</td>
        <td>${r.project_name}</td>
        <td>${new Date(r.created_at).toLocaleString('zh-TW',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}</td>
        <td><span class="bov-status ${r.status}">${statusLabel[r.status]||r.status}</span></td>
      </tr>`).join('');
    el.innerHTML = `<table class="bov-reg-table">
      <thead><tr><th>報備編號</th><th>客戶姓名</th><th>建案</th><th>報備時間</th><th>狀態</th></tr></thead>
      <tbody>${rows}</tbody></table>`;"""

NEW_MY_ROWS = """    const statusLabel = { pending:'待確認', confirmed:'已確認', closed:'已結案' };
    const rows = data.map(r => `
      <tr>
        <td><span class="bov-reg-no">${r.registration_no}</span></td>
        <td>${r.client_name}</td>
        <td>${r.project_name}</td>
        <td>${r.view_date ? r.view_date + (r.view_time ? '<br><span style=\"font-size:.75rem;color:var(--ov-ink3)\">' + r.view_time + '</span>' : '') : '<span style=\"color:var(--ov-ink3);font-size:.78rem\">未指定</span>'}</td>
        <td>${new Date(r.created_at).toLocaleString('zh-TW',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}</td>
        <td><span class="bov-status ${r.status}">${statusLabel[r.status]||r.status}</span></td>
      </tr>`).join('');
    el.innerHTML = `<table class="bov-reg-table">
      <thead><tr><th>報備編號</th><th>客戶姓名</th><th>建案</th><th>帶看時間</th><th>報備時間</th><th>狀態</th></tr></thead>
      <tbody>${rows}</tbody></table>`;"""

if OLD_MY_ROWS in html:
    html = html.replace(OLD_MY_ROWS, NEW_MY_ROWS, 1)
    print("3. loadMyRegs: OK")
else:
    print("3. loadMyRegs: MISS")

# ══════════════════════════════════════════════════════════════════════
# 4. loadAdmRegs() — 加入帶看時間列
# ══════════════════════════════════════════════════════════════════════
OLD_ADM_REGS = """  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>報備編號</th><th>仲介</th><th>公司</th><th>客戶</th><th>電話</th><th>建案</th><th>報備時間</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td style="font-family:var(--font-tech);font-size:.75rem;color:var(--gold)">${r.registration_no}</td>
    <td>${r.broker_name||''}</td><td>${r.broker_company||''}</td>
    <td>${r.client_name}</td><td>${r.client_phone}</td><td>${r.project_name}</td>
    <td>${new Date(r.created_at).toLocaleString('zh-TW',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'待確認',confirmed:'已確認',closed:'結案'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;"""

NEW_ADM_REGS = """  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>報備編號</th><th>仲介</th><th>公司</th><th>客戶</th><th>電話</th><th>建案</th><th>帶看時間</th><th>報備時間</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td style="font-family:monospace;font-size:.75rem;color:var(--ov-gold)">${r.registration_no}</td>
    <td>${r.broker_name||''}</td><td>${r.broker_company||''}</td>
    <td>${r.client_name}</td><td>${r.client_phone}</td><td>${r.project_name}</td>
    <td>${r.view_date ? '<strong>' + r.view_date + '</strong>' + (r.view_time ? '<br><span style=\\"font-size:.75rem;opacity:.7\\">' + r.view_time + '</span>' : '') : '<span style=\\"opacity:.4\\">—</span>'}</td>
    <td style="font-size:.78rem">${new Date(r.created_at).toLocaleString('zh-TW',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'待確認',confirmed:'已確認',closed:'結案'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;"""

if OLD_ADM_REGS in html:
    html = html.replace(OLD_ADM_REGS, NEW_ADM_REGS, 1)
    print("4. loadAdmRegs: OK")
else:
    print("4. loadAdmRegs: MISS")

# ══════════════════════════════════════════════════════════════════════
# 5. Splash HTML — 插入在 <body> 開頭
# ══════════════════════════════════════════════════════════════════════
SPLASH_HTML = """
<!-- ━━ SPLASH SCREEN ━━ -->
<div id="splash" aria-hidden="true">
  <div class="spl-bg"></div>
  <div class="spl-grain"></div>
  <div class="spl-vignette"></div>
  <div class="spl-content">
    <div class="spl-rule"></div>
    <div class="spl-brand">
      <div class="spl-cn">譽誠廣告</div>
      <div class="spl-en">YUCHEN PROPERTIES</div>
    </div>
    <div class="spl-tagline">建商成屋 ・ 聯合銷售專家</div>
    <div class="spl-rule"></div>
    <div class="spl-bar-wrap"><div class="spl-bar"></div></div>
  </div>
</div>
"""

html = html.replace('<body>', '<body>\n' + SPLASH_HTML, 1)
print("5. Splash HTML: OK")

# ══════════════════════════════════════════════════════════════════════
# 6. Splash + Color + Width CSS (注入到最後的 </style> 前)
# ══════════════════════════════════════════════════════════════════════
FIX18_CSS = """
/* ══════════════════════════════════════════════════════════════
   FIX18 — Splash + Color Fixes + Width Fix
══════════════════════════════════════════════════════════════ */

/* ── Splash Screen ── */
#splash {
  position: fixed; inset: 0; z-index: 999999;
  display: flex; align-items: center; justify-content: center;
  background: #06111E;
  transition: opacity 1.4s cubic-bezier(0.4,0,0.2,1),
              transform 1.6s cubic-bezier(0.4,0,0.2,1);
}
#splash.spl-out {
  opacity: 0 !important;
  transform: scale(1.04) !important;
  pointer-events: none !important;
}
.spl-bg {
  position: absolute; inset: 0;
  background: url('https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
  opacity: .22;
  transform: scale(1.04);
  animation: spl-drift 8s ease-in-out infinite alternate;
}
@keyframes spl-drift {
  from { transform: scale(1.04) translate(0,0); }
  to   { transform: scale(1.08) translate(-1%,-0.5%); }
}
.spl-grain {
  position: absolute; inset: 0; pointer-events: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='4'/%3E%3C/filter%3E%3Crect width='300' height='300' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  opacity: .35;
}
.spl-vignette {
  position: absolute; inset: 0; pointer-events: none;
  background: radial-gradient(ellipse 90% 90% at 50% 50%,
    transparent 30%, rgba(6,17,30,0.7) 100%);
}
.spl-content {
  position: relative; z-index: 1;
  text-align: center; color: #fff;
  animation: spl-rise 1.1s cubic-bezier(0.2,0,0.2,1) forwards;
}
@keyframes spl-rise {
  from { opacity: 0; transform: translateY(28px); }
  to   { opacity: 1; transform: translateY(0); }
}
.spl-rule {
  width: 72px; height: 1px;
  background: linear-gradient(90deg, transparent, #C19A4E, transparent);
  margin: 1.6rem auto;
  animation: spl-rule-in 1.4s ease forwards;
}
@keyframes spl-rule-in {
  from { width: 0; opacity: 0; }
  to   { width: 72px; opacity: 1; }
}
.spl-brand { overflow: hidden; }
.spl-cn {
  font-family: 'Noto Serif TC', serif;
  font-size: clamp(3rem, 9vw, 6.5rem);
  font-weight: 700; letter-spacing: .08em;
  color: #fff; line-height: 1;
  animation: spl-brand-in 1s .2s cubic-bezier(0.2,0,0,1) both;
}
@keyframes spl-brand-in {
  from { transform: translateY(100%); opacity: 0; }
  to   { transform: translateY(0); opacity: 1; }
}
.spl-en {
  font-size: clamp(.65rem, 2vw, .9rem);
  letter-spacing: .45em;
  color: #C19A4E;
  margin-top: .75rem;
  font-weight: 500;
  animation: spl-fade-in 1.2s .5s ease both;
}
.spl-tagline {
  font-size: clamp(.7rem, 1.5vw, .8rem);
  letter-spacing: .25em;
  color: rgba(255,255,255,0.45);
  animation: spl-fade-in 1.2s .7s ease both;
}
@keyframes spl-fade-in {
  from { opacity: 0; }
  to   { opacity: 1; }
}
.spl-bar-wrap {
  width: clamp(160px,30vw,240px);
  height: 1px; background: rgba(255,255,255,0.12);
  margin: 2rem auto 0; overflow: hidden;
}
.spl-bar {
  height: 100%; width: 0;
  background: linear-gradient(90deg, rgba(193,154,78,0) 0%, #C19A4E 100%);
  animation: spl-load 2.4s .3s cubic-bezier(0.4,0,0.2,1) forwards;
}
@keyframes spl-load {
  from { width: 0; }
  to   { width: 100%; }
}


/* ── 我的報備紀錄：全寬修正 ── */
/* 登入/申請/報備面板保持窄版 */
#bovLogin, #bovRegister, #bovReport {
  max-width: 560px !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding: 2.5rem !important;
}
/* myReg 面板用全寬 */
.bov-body { max-width: none !important; margin: 0 !important; padding: 0 !important; }
#bovMyReg { max-width: none !important; width: 100% !important; padding: 0 !important; }
.bov-form-title { font-family: 'Noto Serif TC', serif; }
#myregContent { padding: 1.5rem 2rem 2rem !important; overflow-x: auto; }
.bov-reg-table { width: 100%; min-width: 640px; }
#bovMyReg .bov-form-title { padding: 1.5rem 2rem .5rem; font-size: 1.3rem; color: var(--ov-ink); }


/* ── 顏色衝突全面修正 ── */

/* 主網站深色背景文字確認為白色 */
.hero-slide, .hr-left, .hr-right, #hero { color: #fff !important; }
.hr-title, .hr-eyebrow { color: #fff !important; }
.hr-ghost { color: rgba(255,255,255,0.04) !important; }

/* 修正暗色 section 中可能出現文字與背景相同的問題 */
.section-dark, [style*="background:#0B2035"],
[style*="background: #0B2035"],
[style*="background:#1A2D42"],
[style*="background:#0F1923"] { color: #fff !important; }

/* 修正所有 bov-* 元素的對比 */
.bov-field label { color: var(--ov-ink2) !important; }
.bov-field input, .bov-field select, .bov-field textarea {
  color: var(--ov-ink) !important;
  background: #fff !important;
}
.bov-field input::placeholder,
.bov-field textarea::placeholder { color: #B0BEC8 !important; }

/* Tab active 狀態：白色文字在海軍藍背景 */
.bov-tab.active { color: #ffffff !important; }
.bov-tab:not(.active) { color: #3A4E63 !important; background: #fff !important; }

/* admin 側邊欄導覽 */
.adm-nav-btn { color: #3A4E63 !important; }
.adm-nav-btn.active { color: var(--ov-navy) !important; background: rgba(26,58,95,0.09) !important; }
.adm-nav-btn:hover { color: var(--ov-navy) !important; }

/* admin header 的文字在深色背景上 */
.adm-header .adm-logo { color: var(--ov-gold) !important; }
.adm-header .adm-close { color: rgba(255,255,255,0.75) !important; }
.adm-header .adm-close:hover { color: #fff !important; }

/* stat-card 數字 */
.adm-stat-num { color: var(--ov-navy) !important; }
.adm-stat-label { color: var(--ov-ink3) !important; }

/* table 文字 */
.adm-table th { color: var(--ov-ink3) !important; }
.adm-table td { color: var(--ov-ink) !important; }

/* badge 文字 */
.adm-badge.pending { color: #9B7520 !important; }
.adm-badge.active  { color: #1A3A5F !important; }
.adm-badge.new     { color: #5045A0 !important; }

/* bov messages */
.bov-msg { font-size: .84rem !important; }

/* broker header */
.bov-logo { color: var(--ov-navy) !important; }
.bov-header { background: #fff !important; }

/* 報備狀態徽章 */
.bov-status.pending { color: #9B7520 !important; }
.bov-status.confirmed { color: var(--ov-navy) !important; }

/* bov-reg-no */
.bov-reg-no { color: var(--ov-gold) !important; }

/* proj detail 修正綠色遺留 */
#projDetailOverlay { color: var(--ov-ink) !important; }
#projDetailOverlay h1, #projDetailOverlay h2, #projDetailOverlay h3 { color: var(--ov-ink) !important; }

/* deco overlay 修正 */
#decoOverlay { color: var(--ov-ink) !important; }
#decoTrack h3 { color: var(--ov-ink) !important; }
#decoTrack p  { color: var(--ov-ink2) !important; }

/* 修正老版 CSS 留下的淡色變數誤用 */
.adm-login-box .bov-field label { color: var(--ov-ink2) !important; }
.adm-login-box input { color: var(--ov-ink) !important; background: #fff !important; }

/* 確保 bov-btn 文字在深色背景上 */
.bov-btn { color: #fff !important; }
.bov-btn-sec { color: var(--ov-ink2) !important; }


/* ── 增強 UI 特效 ── */

/* 按鈕 ripple 效果 */
.bov-btn, .adm-btn {
  position: relative; overflow: hidden;
}
.bov-btn::after {
  content: '';
  position: absolute;
  width: 200%; height: 200%;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%) scale(0);
  background: rgba(255,255,255,0.15);
  border-radius: 50%;
  transition: transform 0.5s ease, opacity 0.5s ease;
  opacity: 0;
}
.bov-btn:active::after {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  transition: 0s;
}

/* 表單欄位 focus 動畫 */
.bov-field { position: relative; }
.bov-field input, .bov-field select, .bov-field textarea {
  transition: border-color .25s, box-shadow .25s, transform .15s !important;
}
.bov-field input:focus, .bov-field select:focus, .bov-field textarea:focus {
  transform: translateY(-1px) !important;
}

/* 卡片 hover 提升 */
.adm-stat-card { transition: transform .25s, box-shadow .25s !important; }

/* 側邊欄按鈕滑入 */
.adm-nav-btn { transition: all .18s !important; }

/* 報備紀錄 row hover */
.bov-reg-table tr:hover td {
  background: rgba(26,58,95,0.04) !important;
  transition: background .15s !important;
}
.adm-table tr:hover td {
  background: rgba(26,58,95,0.03) !important;
}

/* 仲介 overlay 背景微妙紋理 */
#brokerOverlay {
  background-image: radial-gradient(circle at 80% 20%, rgba(193,154,78,0.05) 0%, transparent 50%),
                    radial-gradient(circle at 20% 80%, rgba(26,58,95,0.06) 0%, transparent 50%) !important;
}

/* 管理後台背景 */
#adminOverlay .adm-content {
  background: #F0F3F7 !important;
}

/* 精進 select 箭頭 */
.bov-field select {
  appearance: none !important;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%238A9AB5' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E") !important;
  background-repeat: no-repeat !important;
  background-position: right 1rem center !important;
  padding-right: 2.5rem !important;
}
"""

last_style = html.rfind('</style>')
html = html[:last_style] + FIX18_CSS + '\n' + html[last_style:]
print("6. CSS: OK")

# ══════════════════════════════════════════════════════════════════════
# 7. Splash JavaScript — 插入在 </body> 前
# ══════════════════════════════════════════════════════════════════════
SPLASH_JS = """
<script>
// Splash screen auto-dismiss
(function() {
  var spl = document.getElementById('splash');
  if (!spl) return;
  var dismissed = false;
  function dismiss() {
    if (dismissed) return;
    dismissed = true;
    spl.classList.add('spl-out');
    setTimeout(function() { spl.style.display = 'none'; }, 1600);
  }
  // Auto dismiss after 2.8s
  setTimeout(dismiss, 2800);
  // Click to skip
  spl.addEventListener('click', dismiss);
})();
</script>
"""

html = html.replace('</body>', SPLASH_JS + '\n</body>', 1)
print("7. Splash JS: OK")

# ══════════════════════════════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════════════════════════════
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nfix18 done.")
print("")
print("Supabase SQL - please run:")
print("  ALTER TABLE client_registrations ADD COLUMN view_date DATE;")
print("  ALTER TABLE client_registrations ADD COLUMN view_time TEXT;")
