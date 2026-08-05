# -*- coding: utf-8 -*-
"""
fix13.py
1. 恢復裝潢模塊（移除 display:none）
2. 整體改為明亮奢華象牙白風格
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. 恢復裝潢區塊 ──────────────────────────────────────────────────────────
html = html.replace(
    '/* V2: 隱藏 B2C 裝修服務區塊 */\n#comparison, #styles, #process, #reels, #line-cta { display: none !important; }',
    '/* V2: 裝修服務區塊已恢復 */',
    1
)
print("1. 裝潢區塊恢復:", "OK")

# 恢復 nav 連結（如果已被移除就補回來）
# 桌面 nav
if '<a href="#comparison">裝潢服務</a>' not in html:
    html = html.replace(
        '    <a href="#projects">精選建案</a>',
        '    <a href="#projects">精選建案</a>\n    <a href="#comparison">裝潢服務</a>',
        1
    )
    print("1b. 桌面 nav 補回: OK")

# ── 2. 明亮主題 CSS 覆寫 ──────────────────────────────────────────────────────
BRIGHT_CSS = """
/* ════════════════════════════════════════════
   BRIGHT THEME OVERRIDE — 奢華象牙白
   暖白 × 深海軍藍 × 金色點綴
════════════════════════════════════════════ */

/* ── 色彩變數覆寫 ── */
:root {
  --void:    #F7F4ED !important;
  --void-2:  #F0EDE4 !important;
  --panel:   rgba(255,255,255,0.88) !important;
  --panel-2: rgba(255,255,255,0.96) !important;
  --line:    rgba(11,32,53,0.10) !important;
  --line-2:  rgba(11,32,53,0.18) !important;
  --ink:     #0B2035 !important;
  --ink-dim: #3D5A76 !important;
  --ink-faint:#7A96B0 !important;
  --cyan:    #1B5C8C !important;
  --cyan-2:  #2470A8 !important;
  --cyan-deep:#0F3A5C !important;
  --violet:  #5A6FA5 !important;
  --gold:    #C8A96E !important;
  --gold-2:  #A8884E !important;
  --glow-cyan: 0 0 0 1px rgba(27,92,140,0.25), 0 0 20px rgba(27,92,140,0.15) !important;
  --glow-soft: 0 0 40px rgba(27,92,140,0.08) !important;
  --green-dark: #1B3A5C !important;
  --green-mid:  #2B5A8C !important;
  --green-light: rgba(27,58,92,0.07) !important;
  --text-dark:  #0B2035 !important;
  --text-mid:   #3D5A76 !important;
  --text-light: #7A96B0 !important;
  --border:     rgba(11,32,53,0.12) !important;
  --blue-pale:  #EBF2FA !important;
  --blue-accent:#1B5C8C !important;
  --blue-navy:  #0B2035 !important;
  --white:      #FFFFFF !important;
  --cream:      #F7F4ED !important;
  --paper:      #0B2035 !important;
}

/* ── 背景 ── */
html, body { background: #F7F4ED !important; color: #0B2035 !important; }
body::before {
  background:
    radial-gradient(ellipse 60% 50% at 85% 5%,  rgba(200,169,110,0.10) 0%, transparent 60%),
    radial-gradient(ellipse 55% 45% at 8%  25%,  rgba(27,92,140,0.07)  0%, transparent 62%),
    radial-gradient(ellipse 50% 40% at 80% 80%,  rgba(200,169,110,0.06) 0%, transparent 60%),
    #F7F4ED !important;
}
body::after { opacity: 0.08 !important; }

/* ── Navbar ── */
#navbar {
  background: rgba(247,244,237,0.82) !important;
  border-bottom: 1px solid rgba(11,32,53,0.08) !important;
  backdrop-filter: blur(18px) !important;
}
#navbar.scrolled {
  background: rgba(247,244,237,0.97) !important;
  box-shadow: 0 2px 20px rgba(11,32,53,0.08) !important;
}
.nav-link { color: #0B2035 !important; }
.nav-logo-cn { color: #0B2035 !important; }
.nav-logo-en { color: var(--gold) !important; }
.btn.btn-gold { background: #C8A96E !important; color: #fff !important; }
.btn.nav-broker-btn {
  background: transparent !important;
  border: 1.5px solid #1B5C8C !important;
  color: #1B5C8C !important;
}
.hamburger span { background: #0B2035 !important; }

/* ── Hero ── */
#hero { background: #F7F4ED !important; }
.hr-left { background: transparent !important; }
.hr-ghost { color: rgba(11,32,53,0.04) !important; }
.hr-eyebrow { color: #1B5C8C !important; background: rgba(27,92,140,0.08) !important; border-color: rgba(27,92,140,0.2) !important; }
.hr-title { color: #0B2035 !important; }
.hr-title .accent { color: #C8A96E !important; }
.hr-sub { color: #3D5A76 !important; }
.hr-stat-num { color: #0B2035 !important; }
.hr-stat-num span { color: #C8A96E !important; }
.hr-stat-label { color: #7A96B0 !important; }
.hr-seam-ring { border-color: rgba(200,169,110,0.2) !important; }
.hr-orb { background: radial-gradient(circle, rgba(200,169,110,0.3), transparent) !important; }
.hr-frame { border-color: rgba(200,169,110,0.25) !important; }
.hr-vert { color: rgba(11,32,53,0.25) !important; }

/* ── Marquee ── */
.mq { background: #0B2035 !important; }
.mq-track span { color: rgba(255,255,255,0.7) !important; }
.mq-track span::before { background: #C8A96E !important; }

/* ── Section labels & titles ── */
.section-label { color: #1B5C8C !important; }
.section-title { color: #0B2035 !important; background: none !important; -webkit-text-fill-color: #0B2035 !important; }
.section-title em { color: #C8A96E !important; -webkit-text-fill-color: #C8A96E !important; }

/* ── Projects ── */
#projects { background: #F7F4ED !important; }
.pj-note { color: #7A96B0 !important; }
.project-card, .pj-tile {
  background: #fff !important;
  box-shadow: 0 4px 24px rgba(11,32,53,0.08) !important;
  border: 1px solid rgba(11,32,53,0.06) !important;
}
.pj-loc { color: #7A96B0 !important; }
.pj-name { color: #0B2035 !important; }
.pj-price { color: #C8A96E !important; }
.pj-badge { background: rgba(27,92,140,0.08) !important; color: #1B5C8C !important; }

/* ── Comparison ── */
#comparison { background: #EBF2FA !important; }
.comparison-text .section-title { color: #0B2035 !important; -webkit-text-fill-color: #0B2035 !important; }
.comparison-desc { color: #3D5A76 !important; }
.comparison-feature { color: #0B2035 !important; }
.feature-icon { background: #C8A96E !important; color: #fff !important; }
.comparison-img-wrap { box-shadow: 0 8px 40px rgba(11,32,53,0.12) !important; }

/* ── Styles / Deco ── */
#styles { background: #F7F4ED !important; }
.style-card { background: #fff !important; box-shadow: 0 4px 20px rgba(11,32,53,0.08) !important; border: 1px solid rgba(11,32,53,0.06) !important; }
.style-name { color: #0B2035 !important; }

/* ── Reels ── */
#reels { background: #0B2035 !important; }

/* ── Process ── */
#process { background: #F0EDE4 !important; }
.process-step { background: #fff !important; box-shadow: 0 4px 20px rgba(11,32,53,0.07) !important; }
.step-num { color: rgba(11,32,53,0.12) !important; }
.step-title { color: #0B2035 !important; }
.step-desc { color: #3D5A76 !important; }

/* ── Broker ── */
#broker { background: #0B2035 !important; }
#broker .section-label { color: #C8A96E !important; }
#broker .section-title { color: #fff !important; -webkit-text-fill-color: #fff !important; }
#broker .bro-desc { color: rgba(255,255,255,0.7) !important; }
.bro-cell { background: rgba(255,255,255,0.07) !important; border-color: rgba(255,255,255,0.12) !important; }
.bro-no { color: #C8A96E !important; }
.bro-title { color: #fff !important; }
.bro-desc2 { color: rgba(255,255,255,0.6) !important; }
.btn-white { background: #fff !important; color: #0B2035 !important; }
.btn-outline { border-color: rgba(255,255,255,0.4) !important; color: #fff !important; }

/* ── Line CTA ── */
#line-cta { background: #C8A96E !important; }
.lcta-title { color: #0B2035 !important; }
.lcta-perk { color: #0B2035 !important; }
.lcta-check { background: #0B2035 !important; color: #C8A96E !important; }
.line-btn { background: #0B2035 !important; color: #fff !important; }
.lcta-note { color: rgba(11,32,53,0.6) !important; }

/* ── Footer ── */
footer { background: #0B2035 !important; border-top: none !important; }
.footer-logo { color: #fff !important; }
.footer-tagline { color: rgba(255,255,255,0.6) !important; }
.footer-col-title { color: #C8A96E !important; }
.footer-links a { color: rgba(255,255,255,0.6) !important; }
.footer-links a:hover { color: #C8A96E !important; }
.footer-contact-item { color: rgba(255,255,255,0.6) !important; }
.footer-copy { color: rgba(255,255,255,0.4) !important; }
.footer-legal a { color: rgba(255,255,255,0.4) !important; }
.footer-legal a:hover { color: #C8A96E !important; }
.social-btn { background: rgba(255,255,255,0.08) !important; color: rgba(255,255,255,0.6) !important; }

/* ── Slider buttons ── */
.slider-btn {
  background: #fff !important;
  color: #0B2035 !important;
  border: 1px solid rgba(11,32,53,0.12) !important;
  box-shadow: 0 2px 12px rgba(11,32,53,0.1) !important;
}
.slider-btn:hover { background: #C8A96E !important; color: #fff !important; border-color: #C8A96E !important; }
.slider-dot { background: rgba(11,32,53,0.2) !important; }
.slider-dot.active { background: #C8A96E !important; }

/* ── 仲介 Overlay ── */
#brokerOverlay { background: #F7F4ED !important; }
.bov-header { background: #fff !important; border-color: rgba(11,32,53,0.1) !important; }
.bov-logo { color: #1B5C8C !important; }
.bov-close { color: #7A96B0 !important; }
.bov-tabs { border-color: rgba(11,32,53,0.1) !important; }
.bov-tab { background: #fff !important; border-color: rgba(11,32,53,0.1) !important; color: #3D5A76 !important; }
.bov-tab.active { background: #1B5C8C !important; color: #fff !important; border-color: #1B5C8C !important; }
.bov-form-title { color: #0B2035 !important; }
.bov-field label { color: #3D5A76 !important; }
.bov-field input, .bov-field select, .bov-field textarea {
  background: #fff !important;
  border-color: rgba(11,32,53,0.15) !important;
  color: #0B2035 !important;
}
.bov-field input:focus, .bov-field select:focus, .bov-field textarea:focus { border-color: #1B5C8C !important; }
.bov-field select option { background: #fff !important; color: #0B2035 !important; }
.bov-btn { background: #1B5C8C !important; color: #fff !important; }
.bov-btn-sec { background: #fff !important; color: #0B2035 !important; border-color: rgba(11,32,53,0.15) !important; }
.bov-msg.success { background: rgba(27,92,140,0.08) !important; border-color: #1B5C8C !important; color: #1B5C8C !important; }
.bov-reg-table th { color: #7A96B0 !important; border-color: rgba(11,32,53,0.1) !important; }
.bov-reg-table td { color: #0B2035 !important; border-color: rgba(11,32,53,0.05) !important; }
.bov-reg-no { color: #C8A96E !important; }
.bov-divider { color: #7A96B0 !important; }
.bov-divider::before, .bov-divider::after { background: rgba(11,32,53,0.1) !important; }
.bov-empty { color: #7A96B0 !important; }

/* ── 管理後台 ── */
#adminOverlay { background: #F0EDE4 !important; }
.adm-header { background: #0B2035 !important; border-color: rgba(255,255,255,0.1) !important; }
.adm-logo { color: #C8A96E !important; }
.adm-close { color: rgba(255,255,255,0.6) !important; }
.adm-sidebar { background: #fff !important; border-color: rgba(11,32,53,0.1) !important; }
.adm-nav-btn { color: #3D5A76 !important; }
.adm-nav-btn:hover, .adm-nav-btn.active { background: #EBF2FA !important; color: #1B5C8C !important; }
.adm-stat-card { background: #fff !important; border-color: rgba(11,32,53,0.08) !important; box-shadow: 0 2px 12px rgba(11,32,53,0.06) !important; }
.adm-stat-num { color: #1B5C8C !important; }
.adm-stat-label { color: #7A96B0 !important; }
.adm-title { color: #0B2035 !important; }
.adm-table th { color: #7A96B0 !important; border-color: rgba(11,32,53,0.1) !important; }
.adm-table td { color: #0B2035 !important; border-color: rgba(11,32,53,0.05) !important; }
.adm-login-box .bov-field label { color: #3D5A76 !important; }

/* ── Mobile Nav ── */
.mobile-nav { background: #fff !important; }
.mobile-nav a { color: #0B2035 !important; border-color: rgba(11,32,53,0.08) !important; }
.mobile-nav-close { color: #0B2035 !important; }

/* ── Cards & Overlays glow 替換 ── */
.project-card:hover { box-shadow: 0 12px 40px rgba(11,32,53,0.14) !important; }

/* ── Section 分隔線改為淺色 ── */
.section-label::before { background: #C8A96E !important; }

/* ── Booking overlay ── */
#bookingOverlay { background: #F7F4ED !important; }
.bk-brand { color: #0B2035 !important; }
.bk-hero-title { color: #0B2035 !important; }
.bk-hero-title em { color: #C8A96E !important; -webkit-text-fill-color: #C8A96E !important; }
.bk-step-num { color: #C8A96E !important; }
.bk-step-label { color: #0B2035 !important; }

/* ── Project Detail Overlay ── */
#projDetailOverlay { background: #F7F4ED !important; }
"""

style_end = html.rfind('</style>')
html = html[:style_end] + BRIGHT_CSS + '\n' + html[style_end:]
print("2. 明亮主題 CSS:", "OK")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix13 done.")
