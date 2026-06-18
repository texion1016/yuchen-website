# -*- coding: utf-8 -*-
"""
Add a full 預約賞屋 (Book a Viewing) overlay to index.html.
Design: split-screen – left luxury dark panel, right clean form.
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── CSS ──────────────────────────────────────────────────────────────────────
BOOKING_CSS = """
/* ===================================================================
   BOOKING OVERLAY
   =================================================================== */
#bookingOverlay {
  position: fixed;
  inset: 0;
  z-index: 9000;
  display: flex;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.45s ease;
}
#bookingOverlay.open {
  opacity: 1;
  pointer-events: all;
}

/* LEFT PANEL ─ luxury dark */
.bk-left {
  width: 42%;
  flex-shrink: 0;
  background:
    linear-gradient(160deg, rgba(10,19,14,0.82) 0%, rgba(27,50,40,0.78) 60%, rgba(10,19,14,0.88) 100%),
    url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&h=1200&fit=crop&auto=format') center/cover no-repeat;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 3rem 3rem 2.5rem;
  position: relative;
  overflow: hidden;
}
.bk-left::before {
  content: '';
  position: absolute;
  bottom: -100px; left: -60px;
  width: 350px; height: 350px;
  border-radius: 50%;
  border: 1px solid rgba(200,169,110,0.15);
  pointer-events: none;
}
.bk-left::after {
  content: '';
  position: absolute;
  bottom: -40px; left: 0px;
  width: 220px; height: 220px;
  border-radius: 50%;
  border: 1px solid rgba(200,169,110,0.22);
  pointer-events: none;
}
.bk-brand {
  font-family: 'Noto Serif TC', serif;
  font-size: 1.45rem;
  font-weight: 700;
  color: #fff;
  letter-spacing: 0.08em;
}
.bk-brand span { color: var(--gold); }
.bk-tagline {
  margin-top: 0.5rem;
  font-size: 0.72rem;
  color: rgba(255,255,255,0.45);
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.bk-hero-text { margin-top: auto; }
.bk-hero-label {
  font-size: 0.68rem;
  letter-spacing: 0.25em;
  color: var(--gold);
  text-transform: uppercase;
  opacity: 0.85;
  margin-bottom: 0.8rem;
}
.bk-hero-title {
  font-family: 'Noto Serif TC', serif;
  font-size: clamp(1.6rem, 2.5vw, 2.2rem);
  font-weight: 700;
  color: #fff;
  line-height: 1.3;
  text-shadow: 0 2px 16px rgba(0,0,0,0.4);
}
.bk-hero-title em { color: var(--gold); font-style: normal; }
.bk-steps {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
}
.bk-step {
  display: flex;
  align-items: center;
  gap: 0.9rem;
}
.bk-step-num {
  width: 28px; height: 28px;
  border-radius: 50%;
  border: 1px solid rgba(200,169,110,0.5);
  display: flex; align-items: center; justify-content: center;
  font-size: 0.7rem;
  color: var(--gold);
  flex-shrink: 0;
}
.bk-step-text {
  font-size: 0.8rem;
  color: rgba(255,255,255,0.65);
  line-height: 1.4;
}

/* RIGHT PANEL ─ form */
.bk-right {
  flex: 1;
  background: #faf8f5;
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  position: relative;
}
.bk-close {
  position: absolute;
  top: 1.4rem; right: 1.6rem;
  background: none;
  border: none;
  font-size: 1.4rem;
  cursor: pointer;
  color: #888;
  line-height: 1;
  transition: color 0.2s;
  z-index: 2;
}
.bk-close:hover { color: var(--green-dark); }
.bk-form-wrap {
  padding: 3rem 3.5rem 2.5rem;
  flex: 1;
}
.bk-form-title {
  font-family: 'Noto Serif TC', serif;
  font-size: 1.7rem;
  font-weight: 700;
  color: var(--green-dark);
  margin-bottom: 0.4rem;
  letter-spacing: 0.04em;
  background: linear-gradient(135deg, #1a3528 0%, #3d7056 50%, #1e3d2a 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.bk-form-sub {
  font-size: 0.82rem;
  color: #888;
  margin-bottom: 2rem;
}
.bk-form-sub span { color: var(--gold); font-weight: 500; }

/* Form grid */
.bk-row {
  display: grid;
  gap: 1.1rem;
  margin-bottom: 1.1rem;
}
.bk-row.cols2 { grid-template-columns: 1fr 1fr; }
.bk-row.cols1 { grid-template-columns: 1fr; }
.bk-fg {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}
.bk-fg label {
  font-size: 0.74rem;
  font-weight: 600;
  color: var(--green-dark);
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.bk-fg label .req { color: var(--gold); margin-left: 2px; }
.bk-fg input,
.bk-fg select,
.bk-fg textarea {
  border: 1.5px solid #e0dbd2;
  border-radius: 10px;
  padding: 0.7rem 0.95rem;
  font-size: 0.9rem;
  color: var(--green-dark);
  background: #fff;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
  font-family: inherit;
  width: 100%;
  box-sizing: border-box;
}
.bk-fg input:focus,
.bk-fg select:focus,
.bk-fg textarea:focus {
  border-color: var(--gold);
  box-shadow: 0 0 0 3px rgba(200,169,110,0.13);
}
.bk-fg textarea { resize: vertical; min-height: 80px; }
.bk-fg select { appearance: none; background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='8' viewBox='0 0 12 8'%3E%3Cpath d='M1 1l5 5 5-5' stroke='%238a7a5a' stroke-width='1.5' fill='none' stroke-linecap='round'/%3E%3C/svg%3E"); background-repeat: no-repeat; background-position: right 0.9rem center; padding-right: 2.2rem; }

/* Time slots */
.bk-time-slots {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 0.6rem;
  margin-top: 0.2rem;
}
.bk-slot {
  position: relative;
}
.bk-slot input[type=radio] {
  position: absolute;
  opacity: 0;
  width: 0; height: 0;
}
.bk-slot label {
  display: block;
  text-align: center;
  padding: 0.6rem 0.4rem;
  border: 1.5px solid #e0dbd2;
  border-radius: 10px;
  font-size: 0.78rem;
  cursor: pointer;
  transition: all 0.2s;
  background: #fff;
  color: #666;
  line-height: 1.4;
  text-transform: none !important;
  font-weight: 400 !important;
  letter-spacing: 0 !important;
}
.bk-slot label strong { display: block; font-size: 0.68rem; color: #aaa; font-weight: 400; margin-top: 2px; }
.bk-slot input[type=radio]:checked + label {
  border-color: var(--gold);
  background: rgba(200,169,110,0.10);
  color: var(--green-dark);
  font-weight: 600 !important;
}
.bk-slot label:hover {
  border-color: rgba(200,169,110,0.5);
}

/* Submit */
.bk-submit-row {
  margin-top: 1.6rem;
  display: flex;
  gap: 1rem;
  align-items: center;
}
.bk-submit-btn {
  background: linear-gradient(135deg, var(--green-dark) 0%, #3d7056 100%);
  color: #fff;
  border: none;
  border-radius: 50px;
  padding: 0.85rem 2.5rem;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  letter-spacing: 0.05em;
  transition: transform 0.2s, box-shadow 0.2s;
  font-family: inherit;
}
.bk-submit-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(44,74,62,0.30);
}
.bk-privacy {
  font-size: 0.72rem;
  color: #aaa;
  line-height: 1.5;
}
.bk-privacy a { color: var(--gold); text-decoration: none; }

/* ── SUCCESS SCREEN ─────────────────────────────── */
#bkSuccess {
  display: none;
  flex: 1;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem;
  text-align: center;
}
#bkSuccess.show { display: flex; }
.bk-success-icon {
  width: 80px; height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--green-dark), #3d7056);
  display: flex; align-items: center; justify-content: center;
  font-size: 2rem;
  margin-bottom: 1.8rem;
  box-shadow: 0 8px 30px rgba(44,74,62,0.25);
  animation: bkPop 0.5s cubic-bezier(0.34,1.56,0.64,1) forwards;
}
@keyframes bkPop {
  from { transform: scale(0); opacity: 0; }
  to   { transform: scale(1); opacity: 1; }
}
.bk-success-title {
  font-family: 'Noto Serif TC', serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--green-dark);
  margin-bottom: 0.7rem;
}
.bk-success-msg {
  font-size: 0.88rem;
  color: #666;
  line-height: 1.7;
  max-width: 320px;
  margin: 0 auto 1rem;
}
.bk-success-ref {
  display: inline-block;
  background: rgba(200,169,110,0.12);
  border: 1px solid rgba(200,169,110,0.35);
  border-radius: 8px;
  padding: 0.5rem 1.2rem;
  font-size: 0.8rem;
  color: var(--gold);
  font-weight: 600;
  letter-spacing: 0.1em;
  margin-bottom: 2rem;
}
.bk-success-close {
  background: var(--green-dark);
  color: #fff;
  border: none;
  border-radius: 50px;
  padding: 0.75rem 2rem;
  font-size: 0.88rem;
  cursor: pointer;
  font-family: inherit;
  transition: background 0.2s;
}
.bk-success-close:hover { background: #3d7056; }

/* Mobile */
@media (max-width: 768px) {
  #bookingOverlay { flex-direction: column; }
  .bk-left { width: 100%; min-height: 220px; padding: 2rem; }
  .bk-steps { display: none; }
  .bk-hero-title { font-size: 1.3rem; }
  .bk-form-wrap { padding: 1.8rem 1.4rem 2rem; }
  .bk-row.cols2 { grid-template-columns: 1fr; }
  .bk-time-slots { grid-template-columns: 1fr 1fr; }
}
"""

# ── HTML ─────────────────────────────────────────────────────────────────────
BOOKING_HTML = """
<!-- ━━ BOOKING OVERLAY ━━ -->
<div id="bookingOverlay">

  <!-- LEFT: luxury panel -->
  <div class="bk-left">
    <div>
      <div class="bk-brand">響誠<span>廣告</span></div>
      <div class="bk-tagline">Premium Living Experience</div>
    </div>
    <div class="bk-hero-text">
      <div class="bk-hero-label">Book a Viewing</div>
      <h2 class="bk-hero-title">預約到府<br/>感受<em>真實生活感</em></h2>
      <div class="bk-steps">
        <div class="bk-step">
          <div class="bk-step-num">1</div>
          <div class="bk-step-text">填寫預約表單，選擇您的偏好時段</div>
        </div>
        <div class="bk-step">
          <div class="bk-step-num">2</div>
          <div class="bk-step-text">專屬顧問在 24 小時內與您確認</div>
        </div>
        <div class="bk-step">
          <div class="bk-step-num">3</div>
          <div class="bk-step-text">親臨現場體驗精選建案魅力</div>
        </div>
      </div>
    </div>
    <div style="font-size:0.68rem;color:rgba(255,255,255,0.25);letter-spacing:0.1em;margin-top:2rem;">
      每週一至六 10:00 — 18:00 開放預約
    </div>
  </div>

  <!-- RIGHT: form -->
  <div class="bk-right">
    <button class="bk-close" onclick="closeBookingOverlay()">✕</button>

    <!-- FORM SCREEN -->
    <div class="bk-form-wrap" id="bkFormWrap">
      <div class="bk-form-title">預約賞屋</div>
      <div class="bk-form-sub">填寫以下資料，我們將安排專屬顧問為您服務 <span>免費諮詢，無任何壓力</span></div>

      <form id="bkForm" onsubmit="bkSubmit(event)" novalidate>
        <!-- Row 1: name + phone -->
        <div class="bk-row cols2">
          <div class="bk-fg">
            <label>姓名 <span class="req">*</span></label>
            <input type="text" id="bkName" placeholder="您的姓名" autocomplete="name" required />
          </div>
          <div class="bk-fg">
            <label>聯絡電話 <span class="req">*</span></label>
            <input type="tel" id="bkPhone" placeholder="09xxxxxxxx" autocomplete="tel" required />
          </div>
        </div>
        <!-- Row 2: email + project -->
        <div class="bk-row cols2">
          <div class="bk-fg">
            <label>Email</label>
            <input type="email" id="bkEmail" placeholder="your@email.com" autocomplete="email" />
          </div>
          <div class="bk-fg">
            <label>有興趣的建案 <span class="req">*</span></label>
            <select id="bkProject" required>
              <option value="">— 請選擇 —</option>
              <option>響誠沐光苑（桃園市中壢區）</option>
              <option>響誠和風居（新北市新莊區）</option>
              <option>響誠山光苑（新北市新店區）</option>
              <option>響誠綠庭院（台中市西屯區）</option>
              <option>響誠晴景台（台北市內湖區）</option>
            </select>
          </div>
        </div>
        <!-- Row 3: date -->
        <div class="bk-row cols1">
          <div class="bk-fg">
            <label>希望看房日期 <span class="req">*</span></label>
            <input type="date" id="bkDate" required />
          </div>
        </div>
        <!-- Row 4: time slots -->
        <div class="bk-row cols1">
          <div class="bk-fg">
            <label>看房時段 <span class="req">*</span></label>
            <div class="bk-time-slots">
              <div class="bk-slot">
                <input type="radio" name="bkTime" id="bkT1" value="上午 10:00–12:00" />
                <label for="bkT1">上午<strong>10:00 – 12:00</strong></label>
              </div>
              <div class="bk-slot">
                <input type="radio" name="bkTime" id="bkT2" value="下午 14:00–17:00" />
                <label for="bkT2">下午<strong>14:00 – 17:00</strong></label>
              </div>
              <div class="bk-slot">
                <input type="radio" name="bkTime" id="bkT3" value="傍晚 17:00–19:00" />
                <label for="bkT3">傍晚<strong>17:00 – 19:00</strong></label>
              </div>
            </div>
          </div>
        </div>
        <!-- Row 5: notes -->
        <div class="bk-row cols1">
          <div class="bk-fg">
            <label>特殊需求或備註</label>
            <textarea id="bkNote" placeholder="如需停車、無障礙設施，或有特別想了解的項目，請在此說明..."></textarea>
          </div>
        </div>
        <!-- Submit -->
        <div class="bk-submit-row">
          <button type="submit" class="bk-submit-btn">📅 確認預約</button>
          <div class="bk-privacy">送出即代表您同意我們的<br/><a href="#">隱私權政策</a>及<a href="#">服務條款</a></div>
        </div>
      </form>
    </div>

    <!-- SUCCESS SCREEN -->
    <div id="bkSuccess">
      <div class="bk-success-icon">✓</div>
      <div class="bk-success-title">預約成功！</div>
      <div class="bk-success-msg">
        感謝您的預約，我們的專屬顧問將在 <strong>24 小時內</strong> 以電話或 LINE 與您確認細節。
      </div>
      <div class="bk-success-ref" id="bkRef">預約編號：BK-000000</div>
      <div style="font-size:0.8rem;color:#999;margin-bottom:1.5rem;">
        請注意來電，號碼將顯示 <strong style="color:var(--green-dark);">02-XXXX-XXXX</strong>
      </div>
      <button class="bk-success-close" onclick="closeBookingOverlay()">返回首頁</button>
    </div>

  </div><!-- /bk-right -->
</div><!-- /bookingOverlay -->
"""

# ── JS ───────────────────────────────────────────────────────────────────────
BOOKING_JS = """
/* ===== BOOKING OVERLAY ===== */
function openBookingOverlay() {
  // Reset form state
  const form = document.getElementById('bkForm');
  if (form) form.reset();
  document.getElementById('bkFormWrap').style.display = '';
  document.getElementById('bkSuccess').classList.remove('show');
  // Set min date to today
  const dateInput = document.getElementById('bkDate');
  if (dateInput) {
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth()+1).padStart(2,'0');
    const dd = String(today.getDate()+1).padStart(2,'0');
    dateInput.min = yyyy+'-'+mm+'-'+dd;
  }
  document.getElementById('bookingOverlay').classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeBookingOverlay() {
  document.getElementById('bookingOverlay').classList.remove('open');
  document.body.style.overflow = '';
}
function bkSubmit(e) {
  e.preventDefault();
  const name = document.getElementById('bkName').value.trim();
  const phone = document.getElementById('bkPhone').value.trim();
  const project = document.getElementById('bkProject').value;
  const date = document.getElementById('bkDate').value;
  const time = document.querySelector('input[name="bkTime"]:checked');
  if (!name || !phone || !project || !date || !time) {
    // Shake fields with missing data
    [['bkName',name],['bkPhone',phone],['bkProject',project],['bkDate',date]].forEach(([id,v])=>{
      if(!v){ const el=document.getElementById(id); el.style.borderColor='#e06060'; el.style.boxShadow='0 0 0 3px rgba(220,80,80,0.12)'; setTimeout(()=>{el.style.borderColor='';el.style.boxShadow='';},1800); }
    });
    if(!time){ document.querySelectorAll('.bk-slot label').forEach(l=>{l.style.borderColor='#e06060'; setTimeout(()=>{l.style.borderColor='';},1800);}); }
    return;
  }
  // Generate reference number
  const ref = 'BK-' + String(Date.now()).slice(-6);
  document.getElementById('bkRef').textContent = '預約編號：' + ref;
  // Show success
  document.getElementById('bkFormWrap').style.display = 'none';
  document.getElementById('bkSuccess').classList.add('show');
}
// Close on backdrop click (left panel area)
document.addEventListener('DOMContentLoaded', function() {
  const overlay = document.getElementById('bookingOverlay');
  if (overlay) {
    overlay.addEventListener('click', function(e) {
      if (e.target === overlay) closeBookingOverlay();
    });
  }
});
"""

# ── INSERT CSS before </style> (find last </style> in <head>) ─────────────
style_end = html.rfind('</style>')
if style_end >= 0:
    html = html[:style_end] + BOOKING_CSS + '\n' + html[style_end:]
    print("CSS inserted: OK")
else:
    print("CSS: MISS - no </style> found")

# ── INSERT HTML before </body> ─────────────────────────────────────────────
body_end = html.rfind('</body>')
if body_end >= 0:
    html = html[:body_end] + BOOKING_HTML + '\n' + html[body_end:]
    print("HTML inserted: OK")
else:
    print("HTML: MISS")

# ── INSERT JS before </script></body> ─────────────────────────────────────
# Find the last </script> before </body>
script_end = html.rfind('</script>', 0, html.rfind('</body>'))
if script_end >= 0:
    html = html[:script_end] + '\n' + BOOKING_JS + '\n' + html[script_end:]
    print("JS inserted: OK")
else:
    print("JS: MISS")

# ── WIRE UP 預約賞屋 buttons ──────────────────────────────────────────────
# Hero section btn-gold: <a href="#" class="btn btn-gold" ...>預約賞屋</a>
old_hero_btn = 'href="#" class="btn btn-gold" style="border-radius:50px;">'
new_hero_btn = 'href="#" onclick="openBookingOverlay();return false;" class="btn btn-gold" style="border-radius:50px;">'
html = html.replace(old_hero_btn, new_hero_btn, 1)
print("Hero btn wired:", "OK" if old_hero_btn not in html else "MISS - check manually")

# Nav btn: <a ... class="btn btn-primary" ...>預約賞屋</a>
old_nav_btn = 'class="btn btn-primary" style="padding:0.55rem 1.3rem; font-size:0.82rem;">'
new_nav_btn = 'onclick="openBookingOverlay();return false;" class="btn btn-primary" style="padding:0.55rem 1.3rem; font-size:0.82rem;">'
html = html.replace(old_nav_btn, new_nav_btn, 1)
print("Nav btn wired:", "OK" if old_nav_btn not in html else "MISS - check manually")

with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\n✅ Booking overlay added!")
