# -*- coding: utf-8 -*-
"""
fix14.py — 設計感大升級
1. 徹底移除所有霓虹發光特效
2. 建立乾淨的設計語言系統
3. Hero 加入「報備卡」signature element
4. 按鈕、卡片、排版全面精緻化
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. Hero 右側加入報備卡 ──────────────────────────────────────────────────
OLD_HR_RIGHT = """  <div class="hr-right">
    <div class="hero-slide active">
      <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="溫暖客廳空間" />
    </div>
    <div class="hero-slide">
      <img src="https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="自然採光客廳" />
    </div>
    <div class="hero-slide">
      <img src="https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="靜謐臥室" />
    </div>
    <div class="hr-frame" aria-hidden="true"></div>
    <div class="hr-vert">聯合銷售．高效去化</div>
    <div class="hero-dots">
      <div class="hero-dot active" onclick="goToSlide(0)"></div>
      <div class="hero-dot" onclick="goToSlide(1)"></div>
      <div class="hero-dot" onclick="goToSlide(2)"></div>
    </div>
  </div>"""

NEW_HR_RIGHT = """  <div class="hr-right">
    <div class="hero-slide active">
      <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="溫暖客廳空間" />
    </div>
    <div class="hero-slide">
      <img src="https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="自然採光客廳" />
    </div>
    <div class="hero-slide">
      <img src="https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=1400&h=1600&fit=crop&auto=format" class="hero-bg" alt="靜謐臥室" />
    </div>
    <div class="hr-frame" aria-hidden="true"></div>
    <div class="hr-vert">聯合銷售．高效去化</div>
    <div class="hero-dots">
      <div class="hero-dot active" onclick="goToSlide(0)"></div>
      <div class="hero-dot" onclick="goToSlide(1)"></div>
      <div class="hero-dot" onclick="goToSlide(2)"></div>
    </div>
    <!-- 報備卡 signature element -->
    <div class="reg-card-demo">
      <div class="rcd-top">
        <span class="rcd-badge">● 已確認</span>
        <span class="rcd-platform">譽誠聯合銷售平台</span>
      </div>
      <div class="rcd-no">YC-260618-A3K2</div>
      <div class="rcd-label-main">客戶報備紀錄</div>
      <div class="rcd-divider"></div>
      <div class="rcd-row"><span class="rcd-key">客　戶</span><span class="rcd-val">陳○○ 小姐</span></div>
      <div class="rcd-row"><span class="rcd-key">指定建案</span><span class="rcd-val">譽誠沐光苑</span></div>
      <div class="rcd-row"><span class="rcd-key">報備仲介</span><span class="rcd-val">王大明（信義房屋）</span></div>
      <div class="rcd-row"><span class="rcd-key">報備時間</span><span class="rcd-val">2026/06/18 14:32</span></div>
      <div class="rcd-footer">客戶歸屬已鎖定 · 保障期間 60 天</div>
    </div>
  </div>"""

html = html.replace(OLD_HR_RIGHT, NEW_HR_RIGHT, 1)
print("1. Hero reg card:", "OK" if OLD_HR_RIGHT not in html else "MISS")

# ── 2. 大設計升級 CSS ────────────────────────────────────────────────────────
DESIGN_CSS = """
/* ══════════════════════════════════════════════════════════
   FIX14 — DESIGN SYSTEM REFRESH
   官方文件 × 現代金融風格
   純白 × 深海軍藍 × 黃銅金
══════════════════════════════════════════════════════════ */

/* ── 移除所有霓虹發光效果 ─────────────────────────── */
*, *::before, *::after {
  text-shadow: none !important;
}
.section-label::before {
  box-shadow: none !important;
  animation: none !important;
  background: #C8A96E !important;
}
.hr-title .accent::after { box-shadow: none !important; background: #C8A96E !important; }
.btn-primary { box-shadow: 0 2px 12px rgba(27,58,92,0.22) !important; }
.btn-primary:hover { box-shadow: 0 4px 20px rgba(27,58,92,0.32) !important; }
.btn-gold { box-shadow: 0 2px 10px rgba(200,169,110,0.3) !important; }
.btn-gold:hover { box-shadow: 0 4px 18px rgba(200,169,110,0.4) !important; }
.btn-white:hover { box-shadow: none !important; }
.btn-outline:hover { box-shadow: none !important; }
.nav-links a::after { box-shadow: none !important; }
.hamburger span { box-shadow: none !important; }
.nav-logo-icon { filter: none !important; }
.hr-eyebrow::before { box-shadow: none !important; }
.hr-stat-num { text-shadow: none !important; }
.project-tag { border: none !important; }

/* ── 設計語言系統 ─────────────────────────────────── */
:root {
  --d-white:   #FFFFFF;
  --d-bg:      #F8F7F2;
  --d-bg-alt:  #EEF2F7;
  --d-ink:     #0F1923;
  --d-ink-2:   #3A4E63;
  --d-ink-3:   #7A8FA6;
  --d-navy:    #1E3A5F;
  --d-gold:    #C19A4E;
  --d-gold-lt: #F0E5C8;
  --d-line:    rgba(15,25,35,0.09);
  --d-shadow:  0 4px 24px rgba(15,25,35,0.08);
  --d-shadow-lg: 0 12px 48px rgba(15,25,35,0.12);
  --d-radius:  14px;
}

html, body { background: var(--d-bg) !important; }

/* ── Scrollbar ───────────────────────────────────── */
::-webkit-scrollbar-track { background: #F0EDE6 !important; }
::-webkit-scrollbar-thumb { background: #C8A96E !important; border-radius: 5px !important; }

/* ── Navbar ─────────────────────────────────────── */
#navbar {
  background: rgba(248,247,242,0.88) !important;
  border-bottom: 1px solid var(--d-line) !important;
  backdrop-filter: blur(20px) !important;
}
#navbar.scrolled {
  background: rgba(248,247,242,0.97) !important;
  box-shadow: 0 1px 0 var(--d-line), 0 4px 20px rgba(15,25,35,0.06) !important;
}
.nav-link, .nav-links a { color: var(--d-ink-2) !important; }
.nav-links a:hover { color: var(--d-ink) !important; }
.nav-links a::after { background: var(--d-navy) !important; }
.nav-logo-cn { color: var(--d-ink) !important; font-size: 1.18rem !important; letter-spacing: .1em !important; }
.nav-logo-en { color: var(--d-gold) !important; letter-spacing: .28em !important; }
.btn.btn-gold {
  background: var(--d-navy) !important;
  color: #fff !important;
  font-weight: 600 !important;
  letter-spacing: .08em !important;
}
.btn.btn-gold:hover { background: #16304F !important; transform: translateY(-1px) !important; }
.btn.nav-broker-btn {
  background: transparent !important;
  border: 1.5px solid var(--d-navy) !important;
  color: var(--d-navy) !important;
}
.btn.nav-broker-btn:hover { background: var(--d-navy) !important; color: #fff !important; transform: none !important; }
.hamburger span { background: var(--d-ink) !important; }

/* ── Section label 重設計 ────────────────────────── */
.section-label {
  color: var(--d-gold) !important;
  font-size: .63rem !important;
  letter-spacing: .42em !important;
  font-weight: 700 !important;
}
.section-label::before {
  width: 6px !important; height: 6px !important;
  background: var(--d-gold) !important;
  border-radius: 50% !important;
}
.section-label::after {
  width: 36px !important;
  background: linear-gradient(to right, rgba(193,154,78,.5), transparent) !important;
}

/* ── Section title 重設計 ────────────────────────── */
.section-title {
  font-size: clamp(1.85rem, 3.2vw, 2.75rem) !important;
  color: var(--d-ink) !important;
  -webkit-text-fill-color: var(--d-ink) !important;
  background: none !important;
  letter-spacing: .06em !important;
  font-weight: 700 !important;
  line-height: 1.3 !important;
}
.section-title em {
  color: var(--d-navy) !important;
  -webkit-text-fill-color: var(--d-navy) !important;
  font-style: italic !important;
}

/* ── Buttons 全面精緻化 ──────────────────────────── */
.btn {
  border-radius: 8px !important;
  font-weight: 600 !important;
  letter-spacing: .06em !important;
  transition: all .22s cubic-bezier(.22,1,.36,1) !important;
}
.btn-outline {
  background: transparent !important;
  color: var(--d-navy) !important;
  border: 1.5px solid rgba(30,58,95,.35) !important;
}
.btn-outline:hover {
  background: var(--d-navy) !important;
  color: #fff !important;
  border-color: var(--d-navy) !important;
  transform: translateY(-1px) !important;
}

/* ── HERO ────────────────────────────────────────── */
#hero { background: var(--d-bg) !important; }
.hr-ghost {
  -webkit-text-stroke: 1px rgba(30,58,95,0.05) !important;
  color: transparent !important;
}
.hr-eyebrow {
  color: var(--d-gold) !important;
  background: rgba(193,154,78,.1) !important;
  border: 1px solid rgba(193,154,78,.2) !important;
  border-radius: 4px !important;
  padding: .3rem .8rem !important;
  display: inline-flex !important;
  font-size: .64rem !important;
  letter-spacing: .32em !important;
}
.hr-eyebrow::before { background: var(--d-gold) !important; width: 5px !important; }
.hr-title { color: var(--d-ink) !important; font-size: clamp(2.6rem,4.2vw,4.1rem) !important; line-height: 1.18 !important; letter-spacing: .02em !important; }
.hr-title .accent {
  color: var(--d-navy) !important;
  position: relative !important;
}
.hr-title .accent::after {
  background: var(--d-gold) !important;
  height: 3px !important;
  bottom: .02em !important;
  border-radius: 2px !important;
  opacity: .7 !important;
}
.hr-sub { color: var(--d-ink-2) !important; line-height: 1.9 !important; letter-spacing: .04em !important; font-size: .95rem !important; }
.hr-sub strong { color: var(--d-ink) !important; border-bottom: 1.5px solid var(--d-gold) !important; padding-bottom: 1px !important; font-weight: 600 !important; }

/* Stats bar */
.hr-stats { border-top: 1px solid var(--d-line) !important; padding-top: 1.6rem !important; }
.hr-stat:not(:last-child)::after { background: linear-gradient(to bottom, transparent, var(--d-line), transparent) !important; }
.hr-stat-num { font-size: 1.9rem !important; color: var(--d-ink) !important; font-weight: 800 !important; }
.hr-stat-num span { color: var(--d-gold) !important; font-size: .55em !important; }
.hr-stat-label { color: var(--d-ink-3) !important; font-size: .68rem !important; letter-spacing: .14em !important; }

/* Hero image side */
.hr-right { position: relative !important; }
.hero-slide { position: absolute !important; inset: 0 !important; }
.hero-bg { width: 100% !important; height: 100% !important; object-fit: cover !important; }
.hr-frame {
  position: absolute !important; inset: 1.5rem !important;
  border: 1px solid rgba(193,154,78,.3) !important;
  border-radius: 4px !important; pointer-events: none !important;
}
.hr-vert {
  color: rgba(15,25,35,0.18) !important;
  font-size: .65rem !important;
  letter-spacing: .32em !important;
}
.hero-dot { background: rgba(255,255,255,.4) !important; }
.hero-dot.active { background: var(--d-gold) !important; }

/* ── 報備卡 Signature Element ─────────────────────── */
.reg-card-demo {
  position: absolute;
  bottom: 2.8rem;
  left: -2.2rem;
  width: 300px;
  background: #fff;
  border-radius: 16px;
  padding: 1.4rem 1.6rem;
  box-shadow: 0 20px 60px rgba(15,25,35,0.18), 0 4px 16px rgba(15,25,35,0.08);
  border: 1px solid rgba(15,25,35,0.06);
  z-index: 10;
  animation: cardFloat 6s ease-in-out infinite;
}
@keyframes cardFloat {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-8px); }
}
.rcd-top {
  display: flex; justify-content: space-between; align-items: center;
  margin-bottom: .9rem;
}
.rcd-badge {
  font-size: .7rem; font-weight: 700;
  color: #16A34A; background: #F0FDF4;
  border: 1px solid #BBF7D0;
  border-radius: 20px; padding: .2rem .65rem;
  letter-spacing: .04em;
}
.rcd-platform {
  font-size: .62rem; color: #9AA5B4; letter-spacing: .06em;
}
.rcd-no {
  font-family: 'Space Grotesk', monospace;
  font-size: .78rem; font-weight: 700;
  color: var(--d-gold);
  letter-spacing: .12em;
  margin-bottom: .15rem;
}
.rcd-label-main {
  font-size: .72rem; color: #9AA5B4;
  letter-spacing: .1em; margin-bottom: .9rem;
}
.rcd-divider {
  height: 1px; background: rgba(15,25,35,0.07);
  margin-bottom: .85rem;
}
.rcd-row {
  display: flex; justify-content: space-between;
  margin-bottom: .5rem; font-size: .78rem;
}
.rcd-key { color: #9AA5B4; letter-spacing: .06em; }
.rcd-val { color: var(--d-ink); font-weight: 600; }
.rcd-footer {
  margin-top: .9rem; padding-top: .7rem;
  border-top: 1px solid rgba(15,25,35,0.07);
  font-size: .66rem; color: #9AA5B4;
  text-align: center; letter-spacing: .06em;
}

/* ── 跑馬燈 ─────────────────────────────────────── */
.mq { background: var(--d-ink) !important; }
.mq-track span { color: rgba(255,255,255,0.55) !important; font-size: .72rem !important; letter-spacing: .22em !important; }
.mq-track span::before { background: var(--d-gold) !important; opacity: .6 !important; }

/* ── 建案卡片 ────────────────────────────────────── */
.pj-tile, .project-card {
  border-radius: 12px !important;
  overflow: hidden !important;
  box-shadow: var(--d-shadow) !important;
  border: 1px solid var(--d-line) !important;
  transition: transform .3s cubic-bezier(.22,1,.36,1), box-shadow .3s !important;
}
.pj-tile:hover, .project-card:hover {
  transform: translateY(-6px) !important;
  box-shadow: var(--d-shadow-lg) !important;
}
.pj-name { color: var(--d-ink) !important; font-weight: 700 !important; font-size: 1.05rem !important; }
.pj-loc { color: var(--d-ink-3) !important; font-size: .72rem !important; letter-spacing: .08em !important; }
.pj-price { color: var(--d-navy) !important; font-size: 1.35rem !important; font-weight: 800 !important; }
.pj-badge {
  background: rgba(30,58,95,.08) !important;
  color: var(--d-navy) !important;
  border-radius: 4px !important;
  font-size: .65rem !important;
  letter-spacing: .1em !important;
  font-weight: 600 !important;
}

/* ── Slider buttons ──────────────────────────────── */
.slider-btn {
  background: #fff !important;
  color: var(--d-ink) !important;
  border: 1px solid var(--d-line) !important;
  box-shadow: 0 2px 8px rgba(15,25,35,0.08) !important;
  border-radius: 50% !important;
}
.slider-btn:hover {
  background: var(--d-navy) !important;
  color: #fff !important;
  border-color: var(--d-navy) !important;
  transform: scale(1.08) !important;
}
.slider-dot { background: rgba(15,25,35,0.15) !important; }
.slider-dot.active { background: var(--d-gold) !important; }

/* ── 仲介專區 ────────────────────────────────────── */
#broker { background: var(--d-ink) !important; }
#broker .section-label { color: var(--d-gold) !important; }
#broker .section-title { color: #fff !important; -webkit-text-fill-color: #fff !important; }
#broker .bro-desc { color: rgba(255,255,255,.65) !important; line-height: 1.9 !important; }
.bro-cell {
  background: rgba(255,255,255,.05) !important;
  border: 1px solid rgba(255,255,255,.09) !important;
  border-radius: 12px !important;
  padding: 1.8rem !important;
  transition: background .22s, border-color .22s !important;
}
.bro-cell:hover {
  background: rgba(255,255,255,.09) !important;
  border-color: rgba(193,154,78,.35) !important;
}
.bro-no { color: var(--d-gold) !important; font-size: 2rem !important; font-weight: 800 !important; }
.bro-title { color: #fff !important; font-size: 1rem !important; font-weight: 700 !important; margin: .5rem 0 .4rem !important; }
.bro-desc2 { color: rgba(255,255,255,.55) !important; font-size: .83rem !important; line-height: 1.8 !important; }
#broker .btn-white {
  background: #fff !important;
  color: var(--d-ink) !important;
  font-weight: 700 !important;
}
#broker .btn-outline {
  background: transparent !important;
  border: 1.5px solid rgba(255,255,255,.3) !important;
  color: #fff !important;
}
#broker .btn-outline:hover {
  background: rgba(255,255,255,.1) !important;
  border-color: rgba(255,255,255,.6) !important;
  transform: translateY(-1px) !important;
}

/* ── 比較區塊 ────────────────────────────────────── */
#comparison { background: var(--d-bg-alt) !important; }
.comparison-text .section-title { color: var(--d-ink) !important; -webkit-text-fill-color: var(--d-ink) !important; }
.comparison-desc { color: var(--d-ink-2) !important; line-height: 1.9 !important; }
.comparison-feature { color: var(--d-ink) !important; font-size: .88rem !important; }
.feature-icon {
  background: var(--d-navy) !important;
  color: #fff !important;
  width: 22px !important; height: 22px !important;
  border-radius: 50% !important;
  font-size: .72rem !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
}

/* ── Process ─────────────────────────────────────── */
#process { background: var(--d-bg) !important; }
.process-step {
  background: #fff !important;
  box-shadow: var(--d-shadow) !important;
  border-radius: var(--d-radius) !important;
  border: 1px solid var(--d-line) !important;
}
.step-num { color: rgba(30,58,95,.08) !important; font-size: 4rem !important; font-weight: 800 !important; }
.step-title { color: var(--d-ink) !important; font-weight: 700 !important; }
.step-desc { color: var(--d-ink-2) !important; }

/* ── Footer ─────────────────────────────────────── */
footer { background: var(--d-ink) !important; }
.footer-logo { color: #fff !important; font-size: 1.3rem !important; letter-spacing: .12em !important; }
.footer-tagline { color: rgba(255,255,255,.5) !important; line-height: 1.9 !important; }
.footer-col-title { color: var(--d-gold) !important; font-size: .7rem !important; letter-spacing: .28em !important; }
.footer-links a { color: rgba(255,255,255,.55) !important; }
.footer-links a:hover { color: var(--d-gold) !important; }
.footer-contact-item { color: rgba(255,255,255,.55) !important; }
.footer-copy { color: rgba(255,255,255,.3) !important; font-size: .72rem !important; }
.footer-legal a { color: rgba(255,255,255,.35) !important; }
.footer-legal a:hover { color: var(--d-gold) !important; }

/* ── Mobile nav ──────────────────────────────────── */
.mobile-nav { background: rgba(248,247,242,.98) !important; backdrop-filter: blur(16px) !important; }
.mobile-nav > a { color: var(--d-ink) !important; }
.mobile-nav > a:hover { color: var(--d-navy) !important; }
.mobile-nav-close { color: var(--d-ink) !important; }

/* ── 選取色 ──────────────────────────────────────── */
::selection { background: var(--d-gold) !important; color: #fff !important; }

/* Mobile 報備卡隱藏 */
@media (max-width: 900px) {
  .reg-card-demo { display: none !important; }
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + DESIGN_CSS + '\n' + html[style_end:]
print("2. Design CSS:", "OK")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix14 done.")
