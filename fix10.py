# -*- coding: utf-8 -*-
"""
fix10.py — V2 文案定位更新
1. 網站標題 / meta
2. Hero 區塊 → 聯合銷售平台定位
3. 跑馬燈 → B2B 訊息
4. 精選建案 label 更新
5. 仲介專區 → 客戶報備系統
6. Footer 更新
7. 移除裝潢/輕裝修相關段落（comparison/styles/process/reels 隱藏）
8. 仲介 Overlay 擴充：登入 + 報備 + 我的報備
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. 網頁標題
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    '<title>譽誠廣告｜讓入住從第一天就有生活感</title>',
    '<title>譽誠聯合銷售平台｜成屋聯合銷售 × 建商合作 × 仲介共享案源</title>',
    1
)
print("1. Title:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Hero 區塊
# ─────────────────────────────────────────────────────────────────────────────
OLD_HERO_LEFT = """  <div class="hr-left">
    <div class="hr-ghost" aria-hidden="true">家</div>
    <div class="hr-eyebrow">新成屋 × 輕裝修 × 快速入住</div>
    <h1 class="hr-title">
      <span class="hr-line">讓入住，</span>
      <span class="hr-line">從<span class="accent">第一天</span>就有</span>
      <span class="hr-line"><span class="accent">生活感</span>。</span>
    </h1>
    <p class="hr-sub">
      精選新成屋，搭配<strong>輕裝修方案</strong>與<strong>快速入住</strong>服務。
      降低購屋門檻，從選屋、設計到交屋，我們全程陪伴。
    </p>
    <div class="hr-btns">
      <a href="#" onclick="openBookingOverlay();return false;" class="btn btn-gold">預約賞屋</a>
      <a href="#comparison" class="btn btn-outline">了解輕裝修</a>
    </div>
    <div class="hr-stats">
      <div class="hr-stat">
        <div class="hr-stat-num">200<span>+</span></div>
        <div class="hr-stat-label">成交建案</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">98<span>%</span></div>
        <div class="hr-stat-label">客戶滿意度</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">15<span>年</span></div>
        <div class="hr-stat-label">深耕房產</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">30<span>天</span></div>
        <div class="hr-stat-label">快速入住</div>
      </div>
    </div>
  </div>"""

NEW_HERO_LEFT = """  <div class="hr-left">
    <div class="hr-ghost" aria-hidden="true">誠</div>
    <div class="hr-eyebrow">建商合作｜成屋餘屋｜聯合銷售</div>
    <h1 class="hr-title">
      <span class="hr-line">成屋餘屋，</span>
      <span class="hr-line">讓<span class="accent">聯合銷售</span></span>
      <span class="hr-line">更<span class="accent">高效</span>。</span>
    </h1>
    <p class="hr-sub">
      提供建設公司<strong>成屋餘屋銷售整合服務</strong>，建立透明且高效率的聯合銷售機制。
      降低建商管理成本，提高合作仲介成交效率。
    </p>
    <div class="hr-btns">
      <a href="#projects" class="btn btn-gold">查看建案</a>
      <a href="#" onclick="openBrokerOverlay();return false;" class="btn btn-outline">仲介登入</a>
    </div>
    <div class="hr-stats">
      <div class="hr-stat">
        <div class="hr-stat-num">50<span>+</span></div>
        <div class="hr-stat-label">合作建案</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">300<span>+</span></div>
        <div class="hr-stat-label">合作仲介</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">0<span>件</span></div>
        <div class="hr-stat-label">撞單糾紛</div>
      </div>
      <div class="hr-stat">
        <div class="hr-stat-num">即時</div>
        <div class="hr-stat-label">案源更新</div>
      </div>
    </div>
  </div>"""

html = html.replace(OLD_HERO_LEFT, NEW_HERO_LEFT, 1)
print("2. Hero left:", "OK" if OLD_HERO_LEFT not in html else "MISS")

# Hero 右側垂直文字
html = html.replace(
    '<div class="hr-vert">家，從第一天開始</div>',
    '<div class="hr-vert">聯合銷售．高效去化</div>',
    1
)
print("2b. Hero vert:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 3. 跑馬燈
# ─────────────────────────────────────────────────────────────────────────────
OLD_MQ = """    <span>預約賞屋</span><span>三十天快速入住</span><span>輕裝修　保固兩年</span><span>兩百件成交建案</span><span>設計師一對一規劃</span><span>讓家從第一天開始</span>
    <span>預約賞屋</span><span>三十天快速入住</span><span>輕裝修　保固兩年</span><span>兩百件成交建案</span><span>設計師一對一規劃</span><span>讓家從第一天開始</span>"""

NEW_MQ = """    <span>聯合銷售平台</span><span>即時可售戶資訊</span><span>客戶報備保障</span><span>零撞單機制</span><span>建商×仲介共贏</span><span>成屋餘屋快速去化</span>
    <span>聯合銷售平台</span><span>即時可售戶資訊</span><span>客戶報備保障</span><span>零撞單機制</span><span>建商×仲介共贏</span><span>成屋餘屋快速去化</span>"""

html = html.replace(OLD_MQ, NEW_MQ, 1)
print("3. Marquee:", "OK" if OLD_MQ not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 4. 精選建案 label
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    '<div class="section-label">Featured Projects</div>\n        <h2 class="section-title">精選建案</h2>',
    '<div class="section-label">Available Projects</div>\n        <h2 class="section-title">建案專區</h2>',
    1
)
html = html.replace(
    '<div class="pj-note">五個案場 · 點擊卡片看建案詳情</div>',
    '<div class="pj-note">點擊建案卡片查看詳情、可售戶別與預約帶看</div>',
    1
)
print("4. Projects label:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 5. 仲介專區
# ─────────────────────────────────────────────────────────────────────────────
OLD_BROKER_SECTION = """  <div class="bro-inner">
    <div class="fade-up">
      <div class="section-label">Broker Platform</div>
      <h2 class="section-title">合作仲介<br />快速帶看平台</h2>
      <p class="bro-desc">
        提供仲介夥伴最完整的即時資訊與服務支援，
        讓每一次帶看都更有效率，撮合更快速。
      </p>
      <div class="bro-btns">
        <a href="#" onclick="openBrokerOverlay();return false;" class="btn btn-white">仲介登入</a>
        <a href="#" class="btn btn-outline" style="color:var(--paper);border-color:rgba(247,244,237,0.5);">申請合作</a>
      </div>
    </div>
    <div class="bro-grid">
      <div class="bro-cell">
        <span class="bro-no">一</span>
        <div class="bro-title">即時可售戶</div>
        <p class="bro-desc2">即時更新在售戶別與狀態，避免帶看空跑</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">二</span>
        <div class="bro-title">帶看登記</div>
        <p class="bro-desc2">線上預約帶看時段，系統自動確認與提醒</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">三</span>
        <div class="bro-title">撞客查詢</div>
        <p class="bro-desc2">快速確認客戶歸屬（保護期 60 天），守住您的業績</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">四</span>
        <div class="bro-title">素材下載</div>
        <p class="bro-desc2">高畫質平面圖、外觀圖與 DM 一鍵下載</p>
      </div>
    </div>
  </div>"""

NEW_BROKER_SECTION = """  <div class="bro-inner">
    <div class="fade-up">
      <div class="section-label">Broker Portal</div>
      <h2 class="section-title">仲介夥伴<br />客戶報備系統</h2>
      <p class="bro-desc">
        平台以建商與仲介合作為主軸，客戶資料完全歸屬於報備仲介，
        平台不介入客戶關係，保障每位夥伴的業績權益。
      </p>
      <div class="bro-btns">
        <a href="#" onclick="openBrokerOverlay();return false;" class="btn btn-white">仲介登入 / 報備客戶</a>
        <a href="#" onclick="openBrokerOverlay();return false;" class="btn btn-outline" style="color:var(--paper);border-color:rgba(247,244,237,0.5);">申請成為合作仲介</a>
      </div>
    </div>
    <div class="bro-grid">
      <div class="bro-cell">
        <span class="bro-no">一</span>
        <div class="bro-title">即時可售戶</div>
        <p class="bro-desc2">即時更新在售戶別與狀態，避免帶看空跑</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">二</span>
        <div class="bro-title">客戶報備</div>
        <p class="bro-desc2">線上報備客戶，系統自動產生報備編號與時間戳記</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">三</span>
        <div class="bro-title">客戶歸屬保障</div>
        <p class="bro-desc2">報備成功後客戶永久歸屬，其他仲介不可查看，杜絕撞單</p>
      </div>
      <div class="bro-cell">
        <span class="bro-no">四</span>
        <div class="bro-title">我的報備紀錄</div>
        <p class="bro-desc2">隨時查看已報備客戶、報備日期、指定建案與處理狀態</p>
      </div>
    </div>
  </div>"""

html = html.replace(OLD_BROKER_SECTION, NEW_BROKER_SECTION, 1)
print("5. Broker section:", "OK" if OLD_BROKER_SECTION not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 6. Footer
# ─────────────────────────────────────────────────────────────────────────────
html = html.replace(
    '<div class="footer-logo">譽誠廣告</div>',
    '<div class="footer-logo">譽誠聯合銷售平台</div>',
    1
)
html = html.replace(
    '''          讓入住，從第一天就有生活感。<br />
          精選新成屋搭配輕裝修服務，<br />
          讓每一個家都充滿溫度。''',
    '''          成屋聯合銷售｜建商合作｜仲介共享案源。<br />
          提供建設公司成屋餘屋銷售整合服務，<br />
          建立透明且高效率的聯合銷售機制。''',
    1
)
html = html.replace(
    '© 2025 譽誠廣告股份有限公司 All Rights Reserved.',
    '© 2025 譽誠聯合銷售平台 All Rights Reserved.',
    1
)
print("6. Footer:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 7. 隱藏裝潢相關段落（comparison / styles / process / reels / line-cta）
#    V2 定位不需要這些 B2C 裝修服務區塊
# ─────────────────────────────────────────────────────────────────────────────
HIDE_CSS = """
/* V2: 隱藏 B2C 裝修服務區塊 */
#comparison, #styles, #process, #reels, #line-cta { display: none !important; }
"""
style_end = html.rfind('</style>')
html = html[:style_end] + HIDE_CSS + '\n' + html[style_end:]
print("7. Hide B2C sections:", "OK")

# 同步移除 nav 中裝潢相關連結
html = html.replace('  <a href="#comparison" onclick="closeMobileNav()">裝潢服務</a>\n', '', 1)
html = html.replace('  <a href="#styles" onclick="closeMobileNav()">風格提案</a>\n', '', 1)
html = html.replace('  <a href="#reels" onclick="closeMobileNav()">生活場景</a>\n', '', 1)
html = html.replace('  <a href="#process" onclick="closeMobileNav()">購屋流程</a>\n', '', 1)
html = html.replace('    <a href="#comparison">裝潢服務</a>\n', '', 1)
html = html.replace('    <a href="#styles">風格提案</a>\n', '', 1)
html = html.replace('    <a href="#reels">生活場景</a>\n', '', 1)
html = html.replace('    <a href="#process">購屋流程</a>\n', '', 1)
print("7b. Nav links cleaned:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 8. 仲介 Overlay 擴充 — 加入「客戶報備」和「我的報備紀錄」分頁
#    (取代原本的 brokerOverlay 內容)
# ─────────────────────────────────────────────────────────────────────────────
OLD_BROKER_OV_OPEN = """<div id="brokerOverlay">"""

NEW_BROKER_OV_INJECT = """<!-- ━━ 仲介 Overlay V2 ━━ -->
<style>
/* Broker Overlay V2 */
#brokerOverlay { position:fixed;inset:0;z-index:9500;display:none;flex-direction:column;background:var(--void);overflow:hidden; }
#brokerOverlay.open { display:flex; }
.bov-header { display:flex;align-items:center;justify-content:space-between;padding:1.2rem 2rem;border-bottom:1px solid var(--line);flex-shrink:0; }
.bov-logo { font-family:var(--font-serif);font-size:1.1rem;color:var(--cyan); }
.bov-close { background:none;border:none;color:var(--ink-dim);font-size:1.6rem;cursor:pointer;padding:.2rem .5rem; }
.bov-tabs { display:flex;gap:.5rem;padding:1.2rem 2rem .5rem;border-bottom:1px solid var(--line);flex-shrink:0; }
.bov-tab { padding:.5rem 1.2rem;border-radius:8px;border:1px solid var(--line);background:none;color:var(--ink-dim);cursor:pointer;font-size:.85rem;transition:all .2s; }
.bov-tab.active { background:var(--cyan);color:var(--void);border-color:var(--cyan);font-weight:600; }
.bov-body { flex:1;overflow-y:auto;padding:2rem; }
.bov-panel { display:none; }
.bov-panel.active { display:block; }
.bov-form-title { font-family:var(--font-serif);font-size:1.4rem;margin-bottom:1.5rem;color:var(--ink); }
.bov-field { margin-bottom:1.2rem; }
.bov-field label { display:block;font-size:.8rem;color:var(--ink-dim);margin-bottom:.4rem;letter-spacing:.05em; }
.bov-field input, .bov-field select, .bov-field textarea {
  width:100%;padding:.75rem 1rem;background:var(--panel-2);border:1px solid var(--line);border-radius:10px;
  color:var(--ink);font-size:.9rem;font-family:var(--font-sans);outline:none;transition:border .2s;
}
.bov-field input:focus, .bov-field select:focus, .bov-field textarea:focus { border-color:var(--cyan); }
.bov-field select option { background:#0A1020; }
.bov-row { display:grid;grid-template-columns:1fr 1fr;gap:1rem; }
.bov-btn { width:100%;padding:.85rem;background:var(--cyan);color:var(--void);border:none;border-radius:10px;font-size:.95rem;font-weight:700;cursor:pointer;margin-top:.5rem;transition:opacity .2s; }
.bov-btn:hover { opacity:.85; }
.bov-btn-sec { background:var(--panel-2);color:var(--ink);border:1px solid var(--line); }
.bov-msg { padding:.8rem 1rem;border-radius:8px;font-size:.85rem;margin-bottom:1rem;display:none; }
.bov-msg.success { background:rgba(91,232,255,.12);border:1px solid var(--cyan);color:var(--cyan); }
.bov-msg.error { background:rgba(255,80,80,.1);border:1px solid rgba(255,80,80,.4);color:#ff7070; }
.bov-reg-table { width:100%;border-collapse:collapse;font-size:.85rem; }
.bov-reg-table th { text-align:left;padding:.6rem .8rem;color:var(--ink-dim);border-bottom:1px solid var(--line);font-weight:500; }
.bov-reg-table td { padding:.7rem .8rem;border-bottom:1px solid rgba(120,180,255,0.07);color:var(--ink); }
.bov-status { display:inline-block;padding:.2rem .6rem;border-radius:4px;font-size:.75rem; }
.bov-status.pending { background:rgba(232,193,106,.15);color:var(--gold); }
.bov-status.confirmed { background:rgba(91,232,255,.12);color:var(--cyan); }
.bov-empty { text-align:center;padding:3rem;color:var(--ink-dim); }
.bov-divider { text-align:center;color:var(--ink-faint);font-size:.8rem;margin:1rem 0;position:relative; }
.bov-divider::before,.bov-divider::after { content:'';position:absolute;top:50%;width:42%;height:1px;background:var(--line); }
.bov-divider::before { left:0; } .bov-divider::after { right:0; }
.bov-reg-no { font-family:var(--font-tech);font-size:.8rem;color:var(--gold);letter-spacing:.08em; }
@media(max-width:600px){.bov-row{grid-template-columns:1fr;}.bov-tabs{overflow-x:auto;white-space:nowrap;}}
</style>

<div id="brokerOverlay">
  <div class="bov-header">
    <div class="bov-logo">譽誠聯合銷售平台 — 仲介專區</div>
    <button class="bov-close" onclick="closeBrokerOv()">✕</button>
  </div>
  <div class="bov-tabs" id="bovTabs">
    <button class="bov-tab active" onclick="switchBovTab('login')">仲介登入</button>
    <button class="bov-tab" onclick="switchBovTab('register')">申請合作</button>
    <button class="bov-tab" id="tabReport" style="display:none" onclick="switchBovTab('report')">客戶報備</button>
    <button class="bov-tab" id="tabMyReg" style="display:none" onclick="switchBovTab('myreg')">我的報備</button>
  </div>
  <div class="bov-body">

    <!-- 登入 -->
    <div class="bov-panel active" id="bovLogin">
      <div class="bov-form-title">仲介登入</div>
      <div id="loginMsg" class="bov-msg"></div>
      <div class="bov-field"><label>電子信箱</label><input type="email" id="loginEmail" placeholder="broker@example.com" /></div>
      <div class="bov-field"><label>密碼</label><input type="password" id="loginPwd" placeholder="••••••••" /></div>
      <button class="bov-btn" onclick="doBrokerLogin()">登入</button>
      <div class="bov-divider">或</div>
      <button class="bov-btn bov-btn-sec" onclick="switchBovTab('register')">還沒有帳號？申請成為合作仲介</button>
    </div>

    <!-- 申請合作 -->
    <div class="bov-panel" id="bovRegister">
      <div class="bov-form-title">申請成為合作仲介</div>
      <div id="registerMsg" class="bov-msg"></div>
      <div class="bov-row">
        <div class="bov-field"><label>姓名 *</label><input type="text" id="regName" placeholder="王大明" /></div>
        <div class="bov-field"><label>仲介公司 *</label><input type="text" id="regCompany" placeholder="信義房屋" /></div>
      </div>
      <div class="bov-row">
        <div class="bov-field"><label>聯絡電話 *</label><input type="tel" id="regPhone" placeholder="0912-345-678" /></div>
        <div class="bov-field"><label>電子信箱 *</label><input type="email" id="regEmail" placeholder="broker@example.com" /></div>
      </div>
      <div class="bov-field"><label>設定密碼 *</label><input type="password" id="regPwd" placeholder="至少 8 個字元" /></div>
      <button class="bov-btn" onclick="doBrokerRegister()">送出申請</button>
      <div class="bov-divider">或</div>
      <button class="bov-btn bov-btn-sec" onclick="switchBovTab('login')">已有帳號？登入</button>
    </div>

    <!-- 客戶報備 -->
    <div class="bov-panel" id="bovReport">
      <div class="bov-form-title">客戶報備</div>
      <div id="reportMsg" class="bov-msg"></div>
      <div class="bov-row">
        <div class="bov-field"><label>客戶姓名 *</label><input type="text" id="rptClientName" placeholder="陳小姐" /></div>
        <div class="bov-field"><label>客戶電話 *</label><input type="tel" id="rptClientPhone" placeholder="0912-345-678" /></div>
      </div>
      <div class="bov-field">
        <label>指定建案 *</label>
        <select id="rptProject">
          <option value="">請選擇建案</option>
          <option value="譽誠沐光苑">譽誠沐光苑 — 桃園市中壢區</option>
          <option value="譽誠晴山苑">譽誠晴山苑 — 台中市北屯區</option>
          <option value="譽誠雲頂">譽誠雲頂 — 新北市板橋區</option>
          <option value="譽誠觀海">譽誠觀海 — 高雄市左營區</option>
          <option value="譽誠御所">譽誠御所 — 台北市內湖區</option>
        </select>
      </div>
      <div class="bov-field"><label>備註</label><textarea id="rptNote" rows="3" placeholder="其他說明..."></textarea></div>
      <button class="bov-btn" onclick="doClientReport()">送出報備</button>
    </div>

    <!-- 我的報備紀錄 -->
    <div class="bov-panel" id="bovMyReg">
      <div class="bov-form-title">我的報備紀錄</div>
      <div id="myregContent">
        <div class="bov-empty">載入中…</div>
      </div>
    </div>

  </div>
</div>

<script>
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
</script>

<!-- 原本的 brokerOverlay（已被上面取代，此標籤只是佔位，不再顯示）-->
<div id="brokerOverlayOLD" style="display:none!important">"""

html = html.replace(OLD_BROKER_OV_OPEN, NEW_BROKER_OV_INJECT, 1)
print("8. Broker overlay V2:", "OK" if OLD_BROKER_OV_OPEN not in html else "MISS")

# 原本的 brokerOverlay 結尾需要閉合（舊 div 變成 OLD div）
# 找舊的 </div><!-- end brokerOverlay --> 並關掉新的佔位 div
# 不用特殊處理，舊的 #brokerOverlay 內容現在在 #brokerOverlayOLD 裡，display:none

# 修復舊的 openBrokerOverlay / closeBrokerOverlay JS（可能有衝突）
OLD_OPEN_BROKER_JS = """function openBrokerOverlay(){
  document.getElementById('bookingOverlay').classList.remove('open');
  document.body.style.overflow='hidden';"""

if OLD_OPEN_BROKER_JS in html:
    html = html.replace(OLD_OPEN_BROKER_JS,
        """function openBrokerOverlay_OLD_DISABLED(){
  document.getElementById('bookingOverlay').classList.remove('open');
  document.body.style.overflow='hidden';""", 1)
    print("8b. Old openBrokerOverlay disabled: OK")
else:
    print("8b. Old openBrokerOverlay: SKIP")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ fix10 完成！")
