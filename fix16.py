# -*- coding: utf-8 -*-
"""
fix16.py — 四大介面 UI 精緻化
1. 建案詳情 overlay
2. 裝潢風格 overlay
3. 仲介登入 overlay
4. 管理後台 overlay
統一色系：深海軍藍 #1A3A5F × 黃銅金 #C19A4E
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

OVERLAY_CSS = """
/* ══════════════════════════════════════════════════════════
   FIX16 — FOUR OVERLAY UI UPGRADE
   統一設計語言：深海軍藍 × 黃銅金 × 純白
══════════════════════════════════════════════════════════ */

/* ── 共用 overlay 變數 ── */
:root {
  --ov-navy:   #1A3A5F;
  --ov-navy2:  #14304F;
  --ov-gold:   #C19A4E;
  --ov-gold-lt:#F5EDD6;
  --ov-bg:     #F6F4EF;
  --ov-white:  #FFFFFF;
  --ov-ink:    #0F1923;
  --ov-ink2:   #3A4E63;
  --ov-ink3:   #8A9AB5;
  --ov-line:   rgba(15,25,35,0.09);
  --ov-shadow: 0 4px 24px rgba(15,25,35,0.10);
}

/* ══════════════════════════
   1. 建案詳情 Overlay
══════════════════════════ */
#projDetailOverlay {
  background: var(--ov-bg) !important;
  font-family: 'Noto Sans TC', sans-serif !important;
}

/* Top bar */
#pdTopBar {
  background: rgba(246,244,239,0.96) !important;
  backdrop-filter: blur(20px) !important;
  border-bottom: 1px solid var(--ov-line) !important;
  padding: .9rem 2rem !important;
}
#pdTopBar button:first-child {
  border-color: var(--ov-line) !important;
  color: var(--ov-ink2) !important;
  border-radius: 50% !important;
  transition: all .2s !important;
}
#pdTopBar button:first-child:hover {
  background: var(--ov-navy) !important;
  color: #fff !important;
  border-color: var(--ov-navy) !important;
}
#pdBarName {
  color: var(--ov-ink) !important;
  font-family: 'Noto Serif TC', serif !important;
  font-size: .98rem !important;
  font-weight: 700 !important;
  letter-spacing: .04em !important;
}
#pdBarLoc { color: var(--ov-ink3) !important; }
#pdTopBar button[onclick="openBookingOverlay()"] {
  background: var(--ov-navy) !important;
  border-radius: 8px !important;
  letter-spacing: .06em !important;
  font-weight: 600 !important;
  padding: .55rem 1.3rem !important;
  transition: all .2s !important;
  font-size: .8rem !important;
}
#pdTopBar button[onclick="openBookingOverlay()"]:hover {
  background: var(--ov-gold) !important;
  transform: translateY(-1px) !important;
}

/* Hero 圖 */
#pdHero { border-radius: 0 !important; }
#pdHero > div:first-child {
  background: linear-gradient(to bottom,
    rgba(10,18,35,0.1) 0%,
    rgba(10,18,35,0.6) 100%) !important;
}
#pdHeroName {
  font-size: 2.2rem !important;
  font-weight: 800 !important;
  letter-spacing: .03em !important;
  text-shadow: 0 2px 20px rgba(0,0,0,0.4) !important;
}
#pdHeroPrice {
  color: var(--ov-gold) !important;
  font-size: 2rem !important;
  text-shadow: none !important;
}

/* Gallery strip */
#pdGallery {
  background: var(--ov-navy2) !important;
  padding: .5rem !important;
  gap: .5rem !important;
}
#pdGallery img {
  height: 72px !important;
  aspect-ratio: 4/3 !important;
  object-fit: cover !important;
  border-radius: 6px !important;
  cursor: pointer !important;
  opacity: .75 !important;
  transition: opacity .2s, transform .2s !important;
  border: 2px solid transparent !important;
}
#pdGallery img:hover { opacity: 1 !important; transform: scale(1.04) !important; }
#pdGallery img.active { opacity: 1 !important; border-color: var(--ov-gold) !important; }

/* Content area */
#projDetailOverlay [style*="max-width:1100px"] {
  padding: 2.5rem 2.5rem 5rem !important;
}

/* Section headings */
#projDetailOverlay [style*="Noto Serif TC"][style*="1.05rem"][style*="font-weight:700"] {
  color: var(--ov-navy) !important;
  font-size: 1rem !important;
  letter-spacing: .08em !important;
  padding-bottom: .6rem !important;
  border-bottom: 2px solid var(--ov-gold) !important;
  display: inline-block !important;
  margin-bottom: 1.3rem !important;
}

/* Specs grid */
#pdSpecs {
  border: 1px solid var(--ov-line) !important;
  border-radius: 12px !important;
  overflow: hidden !important;
  background: #fff !important;
}
/* spec cells */
#pdSpecs > div {
  border-color: var(--ov-line) !important;
  padding: 1rem 1.2rem !important;
}
#pdSpecs .spec-label {
  color: var(--ov-ink3) !important;
  font-size: .7rem !important;
  letter-spacing: .1em !important;
}
#pdSpecs .spec-val {
  color: var(--ov-ink) !important;
  font-weight: 700 !important;
  font-size: .95rem !important;
}

/* Unit cards */
#pdUnits > div {
  background: #fff !important;
  border: 1px solid var(--ov-line) !important;
  border-radius: 12px !important;
  padding: 1.2rem !important;
  transition: all .22s !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.05) !important;
}
#pdUnits > div:hover {
  border-color: var(--ov-gold) !important;
  box-shadow: 0 6px 24px rgba(15,25,35,0.1) !important;
  transform: translateY(-2px) !important;
}

/* Transport + Amenities cards */
#projDetailOverlay [style*="background:#fff"][style*="border-radius:14px"] {
  border: 1px solid var(--ov-line) !important;
  border-radius: 14px !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.05) !important;
}

/* Booking CTA at bottom */
#projDetailOverlay .pd-bk-btn,
#projDetailOverlay button[onclick*="openBookingOverlay"] {
  background: var(--ov-navy) !important;
  border-radius: 10px !important;
}


/* ══════════════════════════
   2. 裝潢風格 Overlay
══════════════════════════ */
#decoOverlay {
  background: var(--ov-bg) !important;
  font-family: 'Noto Sans TC', sans-serif !important;
}

/* Deco Header */
#decoOverlay > div:first-child {
  background: rgba(246,244,239,0.97) !important;
  border-bottom: 1px solid var(--ov-line) !important;
  backdrop-filter: blur(20px) !important;
}
/* Title */
#decoOverlay [style*="Noto Serif TC"][style*=".92rem"] {
  color: var(--ov-ink) !important;
  font-size: .95rem !important;
  letter-spacing: .06em !important;
}
/* Subtitle */
#decoOverlay [style*="6 種精選風格"] {
  color: var(--ov-gold) !important;
  letter-spacing: .1em !important;
}
/* Nav buttons */
#decoOverlay button[onclick*="slideDecoStyle"],
#decoOverlay button[onclick*="closeDecoOverlay"] {
  background: var(--ov-white) !important;
  border: 1px solid var(--ov-line) !important;
  color: var(--ov-ink2) !important;
  border-radius: 50% !important;
  transition: all .2s !important;
}
#decoOverlay button[onclick*="slideDecoStyle"]:hover,
#decoOverlay button[onclick*="closeDecoOverlay"]:hover {
  background: var(--ov-navy) !important;
  color: #fff !important;
  border-color: var(--ov-navy) !important;
}
/* Dots */
.deco-sdot {
  background: var(--ov-navy) !important;
  border-radius: 4px !important;
}
/* Counter */
#decoCtr { color: var(--ov-gold) !important; font-weight: 600 !important; }
/* CTA button */
#decoOverlay button[onclick*="openBookingOverlay"] {
  background: var(--ov-navy) !important;
  border-radius: 8px !important;
  letter-spacing: .06em !important;
  transition: all .2s !important;
}
#decoOverlay button[onclick*="openBookingOverlay"]:hover {
  background: var(--ov-gold) !important;
}

/* Info panel */
#decoTrack > div > div:first-child {
  background: var(--ov-white) !important;
  border-right: 1px solid var(--ov-line) !important;
}
/* Large number */
#decoTrack h3 + * + * {
  color: var(--ov-gold) !important;
}
/* Style name */
#decoTrack h3 {
  color: var(--ov-ink) !important;
  font-size: 2.1rem !important;
  font-weight: 800 !important;
  letter-spacing: -.01em !important;
}
/* EN label */
#decoTrack [style*="letter-spacing:.22em"] {
  color: var(--ov-gold) !important;
  font-weight: 700 !important;
  font-size: .65rem !important;
}
/* Description */
#decoTrack p {
  color: var(--ov-ink2) !important;
  line-height: 2 !important;
  font-size: .87rem !important;
}
/* Feature tags */
#decoTrack span[style*="border-radius:20px"] {
  background: rgba(26,58,95,0.07) !important;
  color: var(--ov-navy) !important;
  border-radius: 6px !important;
  font-weight: 500 !important;
}
/* Price box */
#decoTrack [style*="background:#F7F4ED"] {
  background: linear-gradient(135deg, #F6F4EF, #EEF2F7) !important;
  border: 1px solid var(--ov-line) !important;
  border-radius: 12px !important;
}
#decoTrack [style*="C99A57"] {
  color: var(--ov-navy) !important;
  font-size: 1.7rem !important;
  font-weight: 800 !important;
}
/* Booking CTA in deco panel */
#decoTrack button[onclick*="openBookingOverlay"] {
  background: var(--ov-navy) !important;
  border-radius: 10px !important;
  font-weight: 700 !important;
  letter-spacing: .06em !important;
  transition: all .22s !important;
  border: none !important;
  width: 100% !important;
  padding: .85rem !important;
}
#decoTrack button[onclick*="openBookingOverlay"]:hover {
  background: var(--ov-gold) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(193,154,78,0.35) !important;
}

/* Photo panel bg */
#decoTrack > div > div:last-child {
  background: #EEF2F7 !important;
}
/* Photos */
#decoTrack img {
  border-radius: 10px !important;
  box-shadow: 0 4px 20px rgba(15,25,35,0.1) !important;
}

/* Big number watermark */
#decoTrack [style*="5rem"][style*="Noto Serif TC"] {
  color: rgba(26,58,95,0.06) !important;
}


/* ══════════════════════════
   3. 仲介登入 Overlay
══════════════════════════ */
#brokerOverlay {
  background: linear-gradient(150deg, #F6F4EF 0%, #EEF2F7 100%) !important;
}

/* Header */
.bov-header {
  background: var(--ov-white) !important;
  border-bottom: 1px solid var(--ov-line) !important;
  padding: 1rem 2rem !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.05) !important;
}
.bov-logo {
  font-family: 'Noto Serif TC', serif !important;
  font-size: 1rem !important;
  color: var(--ov-navy) !important;
  font-weight: 700 !important;
  letter-spacing: .06em !important;
}
.bov-close {
  width: 32px !important; height: 32px !important;
  border-radius: 50% !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  border: 1px solid var(--ov-line) !important;
  color: var(--ov-ink3) !important;
  transition: all .2s !important;
  background: none !important;
  cursor: pointer !important;
}
.bov-close:hover { background: var(--ov-navy) !important; color: #fff !important; border-color: var(--ov-navy) !important; }

/* Tabs */
.bov-tabs {
  background: var(--ov-white) !important;
  border-bottom: 1px solid var(--ov-line) !important;
  padding: 1rem 2rem .8rem !important;
  gap: .5rem !important;
}
.bov-tab {
  background: transparent !important;
  border: 1.5px solid var(--ov-line) !important;
  color: var(--ov-ink3) !important;
  border-radius: 8px !important;
  padding: .45rem 1.1rem !important;
  font-size: .82rem !important;
  font-weight: 500 !important;
  transition: all .2s !important;
}
.bov-tab:hover { border-color: var(--ov-navy) !important; color: var(--ov-navy) !important; }
.bov-tab.active {
  background: var(--ov-navy) !important;
  color: #fff !important;
  border-color: var(--ov-navy) !important;
  font-weight: 700 !important;
  box-shadow: 0 3px 12px rgba(26,58,95,0.25) !important;
}

/* Panel body */
.bov-body {
  padding: 2.5rem !important;
  max-width: 560px !important;
  margin: 0 auto !important;
}

/* Form title */
.bov-form-title {
  font-family: 'Noto Serif TC', serif !important;
  font-size: 1.5rem !important;
  color: var(--ov-ink) !important;
  font-weight: 700 !important;
  margin-bottom: .4rem !important;
  letter-spacing: .04em !important;
}

/* Subtitle hint */
.bov-panel::before {
  display: block;
  font-size: .8rem;
  color: var(--ov-ink3);
  margin-bottom: 1.6rem;
  letter-spacing: .04em;
}
#bovLogin::before { content: '歡迎回來，請登入您的仲介帳號'; }
#bovRegister::before { content: '加入平台即可即時取得案源，開始報備客戶'; }
#bovReport::before { content: '報備成功後客戶永久歸屬，其他仲介不可查看'; }
#bovMyReg::before { content: '以下為您的所有客戶報備紀錄'; }

/* Fields */
.bov-field label {
  font-size: .73rem !important;
  font-weight: 600 !important;
  color: var(--ov-ink2) !important;
  letter-spacing: .08em !important;
  text-transform: uppercase !important;
  margin-bottom: .5rem !important;
}
.bov-field input,
.bov-field select,
.bov-field textarea {
  background: var(--ov-white) !important;
  border: 1.5px solid var(--ov-line) !important;
  border-radius: 10px !important;
  color: var(--ov-ink) !important;
  font-size: .9rem !important;
  padding: .8rem 1rem !important;
  transition: border-color .2s, box-shadow .2s !important;
  box-shadow: 0 1px 4px rgba(15,25,35,0.04) !important;
}
.bov-field input:focus,
.bov-field select:focus,
.bov-field textarea:focus {
  border-color: var(--ov-navy) !important;
  box-shadow: 0 0 0 3px rgba(26,58,95,0.1) !important;
  outline: none !important;
}

/* Submit button */
.bov-btn {
  background: var(--ov-navy) !important;
  color: #fff !important;
  border-radius: 10px !important;
  font-size: .9rem !important;
  font-weight: 700 !important;
  letter-spacing: .06em !important;
  padding: .9rem !important;
  transition: all .22s !important;
  border: none !important;
  box-shadow: 0 4px 16px rgba(26,58,95,0.22) !important;
}
.bov-btn:hover {
  background: var(--ov-navy2) !important;
  transform: translateY(-1px) !important;
  box-shadow: 0 6px 22px rgba(26,58,95,0.3) !important;
}
.bov-btn-sec {
  background: var(--ov-white) !important;
  color: var(--ov-ink2) !important;
  border: 1.5px solid var(--ov-line) !important;
  box-shadow: none !important;
}
.bov-btn-sec:hover {
  border-color: var(--ov-navy) !important;
  color: var(--ov-navy) !important;
  transform: none !important;
  box-shadow: none !important;
}

/* Messages */
.bov-msg.success {
  background: rgba(26,58,95,0.06) !important;
  border: 1px solid rgba(26,58,95,0.2) !important;
  color: var(--ov-navy) !important;
  border-radius: 8px !important;
}
.bov-msg.error {
  background: rgba(200,50,50,0.06) !important;
  border: 1px solid rgba(200,50,50,0.2) !important;
  color: #C83232 !important;
  border-radius: 8px !important;
}

/* Divider */
.bov-divider { color: var(--ov-ink3) !important; margin: 1.2rem 0 !important; font-size: .75rem !important; }
.bov-divider::before, .bov-divider::after { background: var(--ov-line) !important; }

/* Registration table */
.bov-reg-table { border-collapse: separate !important; border-spacing: 0 !important; }
.bov-reg-table th {
  background: var(--ov-bg) !important;
  color: var(--ov-ink3) !important;
  font-size: .7rem !important;
  letter-spacing: .12em !important;
  text-transform: uppercase !important;
  padding: .8rem 1rem !important;
  border-bottom: 1px solid var(--ov-line) !important;
}
.bov-reg-table td {
  padding: .85rem 1rem !important;
  color: var(--ov-ink) !important;
  border-bottom: 1px solid rgba(15,25,35,0.04) !important;
}
.bov-reg-table tr:hover td { background: rgba(26,58,95,0.03) !important; }
.bov-reg-no {
  font-family: 'Space Grotesk', monospace !important;
  color: var(--ov-gold) !important;
  font-weight: 700 !important;
  font-size: .78rem !important;
  letter-spacing: .1em !important;
}
.bov-status.pending {
  background: rgba(193,154,78,0.12) !important;
  color: #9B7520 !important;
  font-size: .72rem !important;
  font-weight: 600 !important;
  padding: .2rem .65rem !important;
  border-radius: 20px !important;
}
.bov-status.confirmed {
  background: rgba(26,58,95,0.1) !important;
  color: var(--ov-navy) !important;
  font-size: .72rem !important;
  font-weight: 600 !important;
  padding: .2rem .65rem !important;
  border-radius: 20px !important;
}
.bov-empty {
  color: var(--ov-ink3) !important;
  font-size: .88rem !important;
  padding: 4rem 2rem !important;
}


/* ══════════════════════════
   4. 管理後台 Overlay
══════════════════════════ */
#adminOverlay {
  background: #F0F2F5 !important;
}

/* Header */
.adm-header {
  background: var(--ov-navy) !important;
  border-bottom: none !important;
  padding: .9rem 2rem !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.2) !important;
}
.adm-logo {
  font-family: 'Noto Serif TC', serif !important;
  color: var(--ov-gold) !important;
  font-size: .95rem !important;
  font-weight: 700 !important;
  letter-spacing: .08em !important;
}
.adm-close {
  background: rgba(255,255,255,0.1) !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
  color: rgba(255,255,255,0.7) !important;
  border-radius: 50% !important;
  width: 32px !important; height: 32px !important;
  display: flex !important; align-items: center !important; justify-content: center !important;
  cursor: pointer !important;
  transition: all .2s !important;
}
.adm-close:hover { background: rgba(255,255,255,0.2) !important; color: #fff !important; }

/* Sidebar */
.adm-sidebar {
  background: var(--ov-white) !important;
  border-right: 1px solid var(--ov-line) !important;
  padding: 1.2rem 0 !important;
  width: 200px !important;
  box-shadow: 2px 0 12px rgba(15,25,35,0.04) !important;
}
.adm-nav-btn {
  display: block !important;
  width: 100% !important;
  padding: .8rem 1.4rem !important;
  text-align: left !important;
  font-size: .83rem !important;
  color: var(--ov-ink2) !important;
  border: none !important;
  background: transparent !important;
  cursor: pointer !important;
  transition: all .18s !important;
  font-weight: 500 !important;
  letter-spacing: .04em !important;
  border-left: 3px solid transparent !important;
}
.adm-nav-btn:hover {
  background: rgba(26,58,95,0.05) !important;
  color: var(--ov-navy) !important;
}
.adm-nav-btn.active {
  background: rgba(26,58,95,0.08) !important;
  color: var(--ov-navy) !important;
  font-weight: 700 !important;
  border-left-color: var(--ov-navy) !important;
}

/* Content area */
.adm-content {
  background: #F0F2F5 !important;
  padding: 2rem 2.5rem !important;
}
.adm-title {
  font-family: 'Noto Serif TC', serif !important;
  font-size: 1.3rem !important;
  color: var(--ov-ink) !important;
  font-weight: 700 !important;
  margin-bottom: 1.5rem !important;
  letter-spacing: .04em !important;
  padding-bottom: .8rem !important;
  border-bottom: 1px solid var(--ov-line) !important;
}

/* Stats cards */
.adm-stats {
  gap: 1.2rem !important;
  margin-bottom: 1.5rem !important;
}
.adm-stat-card {
  background: var(--ov-white) !important;
  border: 1px solid var(--ov-line) !important;
  border-radius: 14px !important;
  padding: 1.4rem 1.6rem !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.05) !important;
  transition: transform .2s, box-shadow .2s !important;
}
.adm-stat-card:hover {
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 28px rgba(15,25,35,0.1) !important;
}
.adm-stat-num {
  font-family: 'Space Grotesk', monospace !important;
  font-size: 2.2rem !important;
  font-weight: 800 !important;
  color: var(--ov-navy) !important;
  line-height: 1 !important;
}
.adm-stat-label {
  font-size: .73rem !important;
  color: var(--ov-ink3) !important;
  margin-top: .5rem !important;
  letter-spacing: .1em !important;
  text-transform: uppercase !important;
  font-weight: 600 !important;
}

/* Tables */
.adm-table {
  width: 100% !important;
  border-collapse: separate !important;
  border-spacing: 0 !important;
  background: var(--ov-white) !important;
  border-radius: 12px !important;
  overflow: hidden !important;
  box-shadow: 0 2px 12px rgba(15,25,35,0.06) !important;
  border: 1px solid var(--ov-line) !important;
}
.adm-table th {
  background: #F6F4EF !important;
  color: var(--ov-ink3) !important;
  font-size: .7rem !important;
  letter-spacing: .14em !important;
  text-transform: uppercase !important;
  font-weight: 700 !important;
  padding: .9rem 1.1rem !important;
  border-bottom: 1px solid var(--ov-line) !important;
}
.adm-table td {
  padding: .9rem 1.1rem !important;
  color: var(--ov-ink) !important;
  font-size: .83rem !important;
  border-bottom: 1px solid rgba(15,25,35,0.04) !important;
  vertical-align: middle !important;
}
.adm-table tr:last-child td { border-bottom: none !important; }
.adm-table tr:hover td { background: rgba(26,58,95,0.025) !important; }

/* Badges */
.adm-badge {
  border-radius: 20px !important;
  padding: .22rem .7rem !important;
  font-size: .7rem !important;
  font-weight: 700 !important;
  letter-spacing: .06em !important;
}
.adm-badge.pending { background: rgba(193,154,78,0.12) !important; color: #9B7520 !important; }
.adm-badge.active  { background: rgba(26,58,95,0.1) !important; color: var(--ov-navy) !important; }
.adm-badge.new     { background: rgba(100,80,180,0.1) !important; color: #5045A0 !important; }

/* Login box */
.adm-login-box {
  max-width: 400px !important;
  background: var(--ov-white) !important;
  border-radius: 18px !important;
  padding: 2.5rem !important;
  box-shadow: 0 20px 60px rgba(15,25,35,0.12) !important;
  border: 1px solid var(--ov-line) !important;
}
#admLoginWrap {
  background: linear-gradient(150deg, #F6F4EF 0%, #EEF2F7 100%) !important;
}

/* Empty state */
.adm-empty {
  color: var(--ov-ink3) !important;
  font-size: .88rem !important;
  padding: 4rem 2rem !important;
  background: var(--ov-white) !important;
  border-radius: 12px !important;
  border: 1px dashed var(--ov-line) !important;
  letter-spacing: .06em !important;
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + OVERLAY_CSS + '\n' + html[style_end:]
print("1. Overlay CSS:", "OK")

# ── 修正 projDetailOverlay 背景 ──────────────────────────────────────────────
html = html.replace(
    'id="projDetailOverlay" style="display:none;position:fixed;inset:0;z-index:9500;background:#F2F0E6;overflow-y:auto;"',
    'id="projDetailOverlay" style="display:none;position:fixed;inset:0;z-index:9500;background:#F6F4EF;overflow-y:auto;"',
    1
)

# ── 修正 decoOverlay 背景 ──────────────────────────────────────────────────
html = html.replace(
    'id="decoOverlay" style="display:none;position:fixed;inset:0;z-index:9200;overflow:hidden;background:#F7F4ED;"',
    'id="decoOverlay" style="display:none;position:fixed;inset:0;z-index:9200;overflow:hidden;background:#F6F4EF;"',
    1
)
print("2. Overlay backgrounds:", "OK")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix16 done.")
