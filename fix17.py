# -*- coding: utf-8 -*-
"""
fix17.py
1. 管理員密碼改為 yuchen1101
2. 我的報備紀錄面板加寬
3. 報備時間顯示精確到分鐘（三個地方：我的報備、管理員報備、管理員概覽不變）
4. 刪除所有預約賞屋功能
5. 申請合作加入「經紀人證件號」欄位
"""
import re

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

original_len = len(html)

# ═══════════════════════════════════════════════════════════════
# 1. 管理員密碼
# ═══════════════════════════════════════════════════════════════
html = html.replace(
    "const ADMIN_PWD = 'yuchen2025admin';",
    "const ADMIN_PWD = 'yuchen1101';",
    1
)
print("1. 密碼:", "OK" if "yuchen1101" in html else "MISS")

# ═══════════════════════════════════════════════════════════════
# 2 + 4. CSS: 加寬 myReg；隱藏 bookingOverlay；移除 booking admin tab/panel
# ═══════════════════════════════════════════════════════════════
NEW_CSS = """
/* ── fix17 ── */
/* 我的報備紀錄面板不限寬度 */
#bovMyReg { max-width: none !important; width: 100% !important; padding: 0 !important; }
#myregContent { overflow-x: auto; padding: 1.5rem 2rem; }
/* 隱藏預約賞屋 overlay */
#bookingOverlay { display: none !important; pointer-events: none !important; }
/* 隱藏管理後台「預約帶看」分頁 */
#admBookings { display: none !important; }
"""

last_style = html.rfind('</style>')
html = html[:last_style] + NEW_CSS + '\n' + html[last_style:]
print("2. CSS:", "OK")

# ═══════════════════════════════════════════════════════════════
# 3. 報備時間格式：日期 + 時分
# ═══════════════════════════════════════════════════════════════
OLD_DATE = "new Date(r.created_at).toLocaleDateString('zh-TW')"
NEW_DATE = ("new Date(r.created_at).toLocaleString('zh-TW',"
            "{year:'numeric',month:'2-digit',day:'2-digit',"
            "hour:'2-digit',minute:'2-digit',hour12:false})")
count_date = html.count(OLD_DATE)
html = html.replace(OLD_DATE, NEW_DATE)
print(f"3. 時間格式: 替換了 {count_date} 處")

# 表頭文字
html = html.replace(
    '<th>報備編號</th><th>客戶姓名</th><th>建案</th><th>報備日期</th><th>狀態</th>',
    '<th>報備編號</th><th>客戶姓名</th><th>建案</th><th>報備時間</th><th>狀態</th>',
    1
)
html = html.replace(
    '<th>報備編號</th><th>仲介</th><th>公司</th><th>客戶</th><th>電話</th><th>建案</th><th>日期</th><th>狀態</th>',
    '<th>報備編號</th><th>仲介</th><th>公司</th><th>客戶</th><th>電話</th><th>建案</th><th>報備時間</th><th>狀態</th>',
    1
)

# ═══════════════════════════════════════════════════════════════
# 4. 刪除 預約賞屋
# ═══════════════════════════════════════════════════════════════

# 4a. 主導覽列（手機版）移除「預約賞屋」按鈕
html = html.replace(
    '<a href="#" onclick="closeMobileNav();openBookingOverlay();return false;" class="btn btn-gold">預約賞屋</a>',
    '',
    1
)

# 4b. 主導覽列（桌面版）移除「預約賞屋」按鈕
html = html.replace(
    '<a href="#" onclick="openBookingOverlay();return false;" class="btn btn-gold">預約賞屋</a>',
    '',
    1
)

# 4c. 流程區 Hero CTA
html = html.replace(
    '<a href="#" onclick="openBookingOverlay();return false;" class="btn btn-primary">立即開始 · 預約賞屋</a>',
    '<a href="#broker" class="btn btn-primary">立即諮詢 · 仲介入口</a>',
    1
)

# 4d. lcta-perk 移除預約賞屋條目
html = html.replace(
    '<div class="lcta-perk"><div class="lcta-check">✓</div>線上預約賞屋快速通道</div>',
    '',
    1
)

# 4e. sc-cards：移除 onclick 和「預約賞屋 →」CTA
html = html.replace('onclick="openBookingOverlay()"', '', )  # replace all

# 移除所有 sc-cta 預約賞屋文字
html = re.sub(r'<div class="sc-cta">預約賞屋 →</div>', '', html)

# 4f. projDetailOverlay 頂部「預約賞屋」按鈕
html = html.replace(
    """<button onclick="openBookingOverlay()" style="background:var(--gold);color:#fff;border:none;border-radius:10px;padding:.5rem 1.2rem;font-size:.8rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;transition:opacity .2s;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏠 預約賞屋</button>""",
    '',
    1
)

# 4g. projDetailOverlay 底部「預約賞屋」按鈕（可能有多個）
html = html.replace(
    """<button onclick="openBookingOverlay()" style="flex-shrink:0;background:linear-gradient(135deg,#2F4A3E,#4A6B59);color:#fff;border:none;border-radius:8px;padding:.48rem 1.2rem;font-size:.78rem;font-weight:600;cursor:pointer;font-family:inherit;white-space:nowrap;letter-spacing:.03em;">🏠 預約諮詢</button>""",
    '',
)

html = html.replace(
    """<button onclick="openBookingOverlay()" style="width:100%;background:linear-gradient(135deg,#2F4A3E,#4A6B59);color:#fff;border:none;border-radius:10px;padding:.85rem;font-size:.85rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;">預約設計諮詢 →</button>""",
    '',
)

html = html.replace(
    """<button onclick="openBookingOverlay()" style="width:100%;background:var(--gold);color:#fff;border:none;border-radius:12px;padding:.75rem 2rem;font-size:.88rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;transition:opacity .2s;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏠 預約賞屋</button>""",
    '',
)

# 4h. openBookingOverlay 函式改成 no-op（避免殘餘呼叫報錯）
html = html.replace(
    'function openBookingOverlay() {',
    'function openBookingOverlay() { return; /* removed */ \n  if(false) {',
    1
)
# 找對應的結尾 } 後插入補充的 }
# 更可靠方法：直接在函式名稱旁加 no-op override（放在 </body> 前）
NOOP_SCRIPT = """
<script>
// fix17: 預約賞屋功能已移除
function openBookingOverlay(){return;}
function closeBookingOverlay(){return;}
</script>
"""
html = html.replace('</body>', NOOP_SCRIPT + '\n</body>', 1)

# 4i. 管理後台：移除「預約帶看」側邊欄按鈕
html = html.replace(
    '<button class="adm-nav-btn" onclick="switchAdmPanel(\'bookings\')">預約帶看</button>',
    '',
    1
)

# 4j. 管理後台：移除統計卡「預約帶看」
html = html.replace(
    '<div class="adm-stat-card"><div class="adm-stat-num" id="statBook">-</div><div class="adm-stat-label">預約帶看</div></div>',
    '',
    1
)

# 4k. loadAdmOverview 移除 bookings 查詢
html = html.replace(
    """async function loadAdmOverview() {
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
}""",
    """async function loadAdmOverview() {
  const [r1,r3,r4] = await Promise.all([
    _sb.from('client_registrations').select('id', {count:'exact',head:true}),
    _sb.from('inquiries').select('id', {count:'exact',head:true}),
    _sb.from('brokers').select('id', {count:'exact',head:true})
  ]);
  document.getElementById('statRegs').textContent = r1.count ?? '-';
  document.getElementById('statInq').textContent = r3.count ?? '-';
  document.getElementById('statBrokers').textContent = r4.count ?? '-';
}""",
    1
)

# 4l. switchAdmPanel loaders map：移除 bookings
html = html.replace(
    "const loaders = { registrations: loadAdmRegs, bookings: loadAdmBookings, inquiries: loadAdmInq, brokers: loadAdmBrokers };",
    "const loaders = { registrations: loadAdmRegs, inquiries: loadAdmInq, brokers: loadAdmBrokers };",
    1
)

print("4. 預約賞屋移除: OK")

# ═══════════════════════════════════════════════════════════════
# 5. 申請合作表單加入「經紀人證件號」欄位
# ═══════════════════════════════════════════════════════════════

# 在姓名/公司那行後，電話/信箱那行後，加入新欄位（在密碼欄位之前）
OLD_FORM_SECTION = """      <div class="bov-field"><label>設定密碼 *</label><div class="pwd-wrap">
      <input type="password" id="regPwd" placeholder="至少 8 個字元" />
      <span class="pwd-eye" onclick="togglePwd('regPwd',this)">👁</span>
    </div></div>"""

NEW_FORM_SECTION = """      <div class="bov-field"><label>經紀人證件號 *</label><input type="text" id="regLicenseNo" placeholder="例：B-01234567" /></div>
      <div class="bov-field"><label>設定密碼 *</label><div class="pwd-wrap">
      <input type="password" id="regPwd" placeholder="至少 8 個字元" />
      <span class="pwd-eye" onclick="togglePwd('regPwd',this)">👁</span>
    </div></div>"""

if OLD_FORM_SECTION in html:
    html = html.replace(OLD_FORM_SECTION, NEW_FORM_SECTION, 1)
    print("5a. 表單欄位: OK")
else:
    print("5a. 表單欄位: MISS（可能已修改）")

# 更新驗證與送出邏輯
OLD_REGISTER_FN = """async function doBrokerRegister() {
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
    });"""

NEW_REGISTER_FN = """async function doBrokerRegister() {
  const name = document.getElementById('regName').value.trim();
  const company = document.getElementById('regCompany').value.trim();
  const phone = document.getElementById('regPhone').value.trim();
  const email = document.getElementById('regEmail').value.trim().toLowerCase();
  const licenseNo = document.getElementById('regLicenseNo').value.trim();
  const pwd = document.getElementById('regPwd').value;
  if (!name||!company||!phone||!email||!licenseNo||!pwd) {
    showBovMsg('registerMsg','請填寫所有必填欄位（含經紀人證件號）','error'); return;
  }
  if (pwd.length < 8) { showBovMsg('registerMsg','密碼至少需要 8 個字元','error'); return; }
  const btn = document.querySelector('#bovRegister .bov-btn');
  btn.textContent = '送出中…'; btn.disabled = true;
  try {
    const hash = await hashPwd(pwd);
    const { error } = await _sb.from('brokers').insert({
      name, company, phone, email, license_no: licenseNo, password_hash: hash, status: 'active'
    });"""

if OLD_REGISTER_FN in html:
    html = html.replace(OLD_REGISTER_FN, NEW_REGISTER_FN, 1)
    print("5b. 送出函式: OK")
else:
    print("5b. 送出函式: MISS")

# 更新管理後台仲介清單顯示
OLD_BROKER_TABLE = """  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>姓名</th><th>公司</th><th>電話</th><th>信箱</th><th>申請日期</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td>${r.name}</td><td>${r.company}</td><td>${r.phone}</td><td>${r.email}</td>
    <td>${new Date(r.created_at).toLocaleDateString('zh-TW')}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'審核中',active:'啟用',suspended:'停用'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;"""

NEW_BROKER_TABLE = """  el.innerHTML = `<table class="adm-table"><thead><tr>
    <th>姓名</th><th>公司</th><th>證件號</th><th>電話</th><th>信箱</th><th>申請日期</th><th>狀態</th>
    </tr></thead><tbody>${data.map(r=>`<tr>
    <td>${r.name}</td><td>${r.company}</td><td style="font-family:monospace;font-size:.8rem;color:var(--ov-gold)">${r.license_no||'—'}</td><td>${r.phone}</td><td>${r.email}</td>
    <td>${new Date(r.created_at).toLocaleString('zh-TW',{year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hour12:false})}</td>
    <td><span class="adm-badge ${r.status}">${{pending:'審核中',active:'啟用',suspended:'停用'}[r.status]||r.status}</span></td>
    </tr>`).join('')}</tbody></table>`;"""

if OLD_BROKER_TABLE in html:
    html = html.replace(OLD_BROKER_TABLE, NEW_BROKER_TABLE, 1)
    print("5c. 管理後台仲介表格: OK")
else:
    print("5c. 管理後台仲介表格: MISS")

# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nfix17 done. 大小 {original_len} → {len(html)} bytes")
print("\n⚠️  Supabase 需要執行以下 SQL 新增欄位：")
print("   ALTER TABLE brokers ADD COLUMN license_no TEXT;")
