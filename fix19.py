# -*- coding: utf-8 -*-
"""
fix19.py — 純文字顏色對比修正（不改背景）
只修 color 屬性，所有 background 保持不動
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

CONTRAST_CSS = """
/* ══════════════════════════════════════════════════════
   FIX19 — TEXT CONTRAST ONLY (no background changes)
   Rule: only color / text-shadow / opacity on text
══════════════════════════════════════════════════════ */

/* ── Hero 區深色背景上的淡色文字 ── */
.hr-stat-label   { color: #A8C0D8 !important; }
.hr-stat-num     { color: #FFFFFF !important; }
.hr-eyebrow      { color: rgba(255,255,255,0.75) !important; }

/* ── 主站各 section 深色背景上的小字 ── */
/* pj = 建案、st = 特色、sc = 服務卡、bro = 仲介說明 */
.pj-note, .pj-addr, .pj-status-txt { color: rgba(255,255,255,0.70) !important; }
.st-note, .st-desc                  { color: rgba(255,255,255,0.72) !important; }
.sc-hint                            { color: rgba(255,255,255,0.68) !important; }
.bro-desc2, .bro-note               { color: rgba(255,255,255,0.72) !important; }
.tl-desc                            { color: rgba(255,255,255,0.72) !important; }
.lcta-perk                          { color: rgba(255,255,255,0.80) !important; }

/* ── Footer — 深色底上所有文字一律提亮 ── */
.footer-tagline        { color: rgba(255,255,255,0.60) !important; }
.footer-links a        { color: rgba(255,255,255,0.65) !important; }
.footer-links a:hover  { color: #C19A4E !important; }
.footer-copy           { color: rgba(255,255,255,0.50) !important; }
.footer-legal a        { color: rgba(255,255,255,0.55) !important; }
.footer-legal a:hover  { color: #C19A4E !important; }
.footer-contact-item   { color: rgba(255,255,255,0.65) !important; }
.footer-brand-name     { color: #FFFFFF !important; }
.footer-brand-sub      { color: rgba(255,255,255,0.55) !important; }

/* ── 仲介登入 Overlay 白色卡片上的文字 ── */
/* "或" 分隔線在白色卡片上 */
.bov-divider           { color: #6A7E93 !important; }
/* 表單 label */
.bov-field label       { color: #2A3E52 !important; }
/* placeholder 顏色 */
.bov-field input::placeholder,
.bov-field textarea::placeholder { color: #9AAABB !important; }
/* 空白提示在白色背景 */
.bov-empty             { color: #5A7088 !important; }

/* ── 仲介登入 Overlay 頂部深色玻璃區域 ── */
#brokerOverlay .bov-logo  { color: #FFFFFF !important; }
#brokerOverlay .bov-close { color: rgba(255,255,255,0.75) !important; }
/* 深色區域的 tab 未選中文字 */
#brokerOverlay .bov-tab:not(.active) { color: rgba(255,255,255,0.80) !important; }

/* ── 管理後台側邊欄 — 白色底上文字 ── */
.adm-nav-btn              { color: #2A3E52 !important; }   /* 從 #3D5A76 加深 */
.adm-nav-btn:hover        { color: #1A3A5F !important; }
.adm-nav-btn.active       { color: #1A3A5F !important; }

/* ── 管理後台統計卡 — 白色卡片上 ── */
.adm-stat-label           { color: #4A6280 !important; }   /* 從 #7A96B0 加深 */
.adm-stat-num             { color: #1A3A5F !important; }

/* ── 管理後台表格文字 ── */
.adm-table th             { color: #4A6280 !important; }
.adm-table td             { color: #1A2D40 !important; }

/* ── 管理後台 title ── */
.adm-title                { color: #1A2D40 !important; }

/* ── 舊版 broker sidebar（若仍存在） ── */
.bo-sb-label              { color: rgba(255,255,255,0.65) !important; }
.bo-sb-role               { color: rgba(255,255,255,0.65) !important; }
.bo-sb-sec                { color: rgba(255,255,255,0.60) !important; }
.bo-ni                    { color: rgba(255,255,255,0.75) !important; }
.bo-stat-lbl              { color: #4A6280 !important; }   /* #aaa → 可讀深灰 */
.bo-stat-val              { color: #1A2D40 !important; }

/* ── 報備紀錄表格內的次要文字 ── */
.bov-reg-table td         { color: #1A2D40 !important; }
.bov-reg-table th         { color: #4A6280 !important; }
/* view_time 次要字 */
.bov-reg-table span[style*="ov-ink3"] { color: #4A6280 !important; }

/* ── 建案詳情 Overlay 白色卡片上的次要文字 ── */
#projDetailOverlay .spec-label { color: #4A6280 !important; }
#projDetailOverlay p           { color: #2A3E52 !important; }

/* ── 裝潢 Overlay 白色面板上 ── */
#decoTrack p               { color: #2A3E52 !important; }
#decoTrack [style*="letter-spacing:.22em"] { color: #9B7520 !important; }

/* ── 一般深色 section 中 section-sub / section-desc ── */
.section-sub, .section-desc { color: rgba(255,255,255,0.72) !important; }
.tl-side-desc               { color: rgba(255,255,255,0.72) !important; }

/* ── 確保 bov-status badge 文字在淺色 badge 背景上可讀 ── */
.bov-status.pending   { color: #7A5A10 !important; }
.bov-status.confirmed { color: #0E2E4E !important; }

/* ── 確保 adm-badge 可讀 ── */
.adm-badge.pending    { color: #7A5A10 !important; }
.adm-badge.active     { color: #0E2E4E !important; }
.adm-badge.new        { color: #3A3080 !important; }
"""

last_style = html.rfind('</style>')
html = html[:last_style] + CONTRAST_CSS + '\n' + html[last_style:]

with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix19 done.")
