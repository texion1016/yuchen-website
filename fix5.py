# -*- coding: utf-8 -*-
"""
fix5.py — Three sweeping changes:
1. 裝潢方案 full overlay with 6 styles + galleries
2. Color scheme → light blue (replace green palette)
3. More artistic global style touches
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ═══════════════════════════════════════════════════════════════════════════════
# PART A: COLOR SCHEME → LIGHT BLUE
# ═══════════════════════════════════════════════════════════════════════════════

# 1a. CSS variable palette swap
OLD_ROOT = """    :root {
      --cream: #F7F4EF;
      --white: #FFFFFF;
      --green-dark: #2C4A3E;
      --green-mid: #3D6B5C;
      --green-light: #EAF0EC;
      --gold: #C8A96E;
      --gold-light: #F0E6D3;
      --text-dark: #1A1A1A;
      --text-mid: #4A4A4A;
      --text-light: #888888;
      --border: #E0DAD0;
      --shadow: 0 4px 24px rgba(44,74,62,0.10);
      --shadow-lg: 0 12px 48px rgba(44,74,62,0.16);
      --radius: 12px;
      --transition: 0.35s cubic-bezier(0.4,0,0.2,1);
    }"""

NEW_ROOT = """    :root {
      --cream: #F2F6FB;
      --white: #FFFFFF;
      --green-dark: #1B3A5C;
      --green-mid: #2E6CA4;
      --green-light: #DCE9F7;
      --gold: #C8A96E;
      --gold-light: #F0E6D3;
      --text-dark: #0D1B2A;
      --text-mid: #3A5068;
      --text-light: #7A8FA6;
      --border: #C8DAEA;
      --shadow: 0 4px 24px rgba(27,58,92,0.10);
      --shadow-lg: 0 12px 48px rgba(27,58,92,0.18);
      --radius: 12px;
      --transition: 0.35s cubic-bezier(0.4,0,0.2,1);
      /* ── Blue palette extras ── */
      --blue-pale: #EBF4FF;
      --blue-accent: #4A90C4;
      --blue-navy: #0F2744;
    }"""

html = html.replace(OLD_ROOT, NEW_ROOT)
print("A1. Root vars:", "OK" if OLD_ROOT not in html else "MISS")

# 1b. Direct hex replacements (hardcoded colors scattered in the file)
COLOR_MAP = {
    # dark greens → navy blues
    '#2C4A3E': '#1B3A5C',
    '#1B3228': '#0F2744',
    '#2c4a3e': '#1b3a5c',
    '#1b3228': '#0f2744',
    # mid greens → steel blues
    '#3D6B5C': '#2E6CA4',
    '#3d6b5c': '#2e6ca4',
    '#3d7056': '#2E6CA4',
    '#2c4a3e': '#1b3a5c',
    # light green tints → light blue
    '#EAF0EC': '#DCE9F7',
    '#eaf0ec': '#dce9f7',
    'rgba(44,74,62': 'rgba(27,58,92',
    'rgba(27,50,40': 'rgba(15,39,68',
    'rgba(20,38,30': 'rgba(10,28,55',
    'rgba(12,25,20': 'rgba(8,20,45',
    'rgba(28,50,40': 'rgba(15,35,65',
    'rgba(61,112,86': 'rgba(46,108,164',
    'rgba(44,74,62)': 'rgba(27,58,92)',
    # section bg greens
    'rgba(234,240,236': 'rgba(220,233,247',
    'rgba(242,238,232': 'rgba(235,244,255',
    # broker dark bg
    '#0C1914': '#071828',
    '#0c1914': '#071828',
    '#111E18': '#0A1E35',
    '#111e18': '#0a1e35',
    # body bg
    '#F7F4EF': '#F2F6FB',
    # border
    '#E0DAD0': '#C8DAEA',
    '#e0dbd2': '#c8daea',
    '#ECEAE6': '#DCE9F7',
    '#eceae6': '#dce9f7',
    # bo-panel backgrounds
    '#F9F7F3': '#F2F7FD',
    '#f9f7f3': '#f2f7fd',
    '#F5F3EF': '#EEF5FC',
    '#f5f3ef': '#eef5fc',
}
replaced = 0
for old, new in COLOR_MAP.items():
    count = html.count(old)
    if count:
        html = html.replace(old, new)
        replaced += count
print(f"A2. Inline colors replaced: {replaced} instances")

# 1c. Additional artistic global CSS
ARTISTIC_CSS = """
/* ══════════════════════════════════════════════════
   BLUE THEME + ARTISTIC GLOBAL OVERRIDES
══════════════════════════════════════════════════ */

/* --- Body & scrollbar --- */
body { background: var(--cream) !important; }
::-webkit-scrollbar-thumb { background: var(--blue-accent) !important; }

/* --- Navbar blue tint --- */
#navbar.scrolled {
  background: rgba(242,246,251,0.97) !important;
  border-bottom: 1px solid var(--border) !important;
  box-shadow: 0 2px 20px rgba(27,58,92,.08) !important;
}
#navbar.scrolled .nav-logo { color: var(--green-dark) !important; }

/* --- Section backgrounds --- */
#projects {
  background: linear-gradient(180deg,
    rgba(220,233,247,0.45) 0%,
    rgba(235,244,255,0.60) 60%,
    rgba(220,233,247,0.45) 100%),
    url('https://images.unsplash.com/photo-1501854140801-50d01698950b?w=1920&h=900&fit=crop&auto=format') center/cover no-repeat !important;
}
#comparison {
  background: linear-gradient(135deg, #EEF5FC 0%, #DCE9F7 60%, #EEF5FC 100%) !important;
}

/* --- Section label color --- */
.section-label { color: var(--blue-accent) !important; }

/* --- Section title gradient (light sections) --- */
#projects .section-title,
#services .section-title,
#broker .section-title,
#flow .section-title,
#testimonials .section-title,
#line-cta .section-title,
#comparison .section-title {
  background: linear-gradient(135deg, #0F2744 0%, #2E6CA4 50%, #1B3A5C 100%) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  filter: drop-shadow(0 3px 8px rgba(27,58,92,0.18)) !important;
}

/* --- Buttons --- */
.btn-primary {
  background: var(--green-dark) !important;
}
.btn-primary:hover { background: var(--green-mid) !important; }
.btn-outline {
  color: var(--green-dark) !important;
  border-color: var(--green-dark) !important;
}
.btn-outline:hover { background: var(--green-dark) !important; color: #fff !important; }

/* --- Gold accent bar --- */
.section-head-text::before {
  background: linear-gradient(180deg, var(--gold) 0%, rgba(200,169,110,0.08) 100%) !important;
}

/* --- Feature icons --- */
.feature-icon {
  color: var(--blue-accent) !important;
  background: rgba(74,144,196,0.12) !important;
  border: 1.5px solid rgba(74,144,196,0.25) !important;
}

/* --- Comparison widget --- */
.comp-visual-room {
  background: linear-gradient(160deg, #1B3A5C 0%, #2E6CA4 100%) !important;
}

/* --- Project tags --- */
.project-tag { background: rgba(27,58,92,0.82) !important; }
.project-tag.new { background: var(--gold) !important; }

/* --- Project card btn --- */
.project-card .btn-primary { background: var(--green-dark) !important; }

/* --- Floating btns --- */
.float-btn.float-phone { background: var(--blue-accent) !important; }
.float-btn.float-line  { background: #00B900 !important; }

/* --- Slider dots --- */
.slider-dot.active { background: var(--blue-accent) !important; }
.reel-dot.active   { background: var(--gold) !important; }

/* --- Reel section: keep dark but with blue tone --- */
#reels {
  background:
    linear-gradient(160deg, rgba(8,20,45,0.80) 0%, rgba(10,30,65,0.72) 50%, rgba(8,20,45,0.84) 100%),
    url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&h=1080&fit=crop&auto=format') center/cover fixed no-repeat !important;
}

/* --- Testimonials --- */
.testimonial-card {
  border-color: var(--border) !important;
  background: var(--white) !important;
}
.testimonial-stars { color: var(--gold) !important; }

/* ─── ARTISTIC TOUCHES ──────────────────────────── */

/* Watermark text behind section titles */
.section-head { position: relative; overflow: visible; }
.section-head-text > .section-title::before {
  content: attr(data-en);
  position: absolute;
  left: -1.2rem; top: -1.4rem;
  font-size: 3.5rem;
  font-family: 'Noto Serif TC', serif;
  color: rgba(27,58,92,0.04);
  font-weight: 900;
  white-space: nowrap;
  pointer-events: none;
  letter-spacing: .02em;
  z-index: 0;
}

/* Subtle diagonal background pattern on cream sections */
#services::before,
#flow::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, rgba(74,144,196,0.05) 1px, transparent 1px);
  background-size: 32px 32px;
  pointer-events: none;
  z-index: 0;
}
#services, #flow { position: relative; }
#services > *, #flow > * { position: relative; z-index: 1; }

/* Thin artistic top border on sections */
#services::after,
#testimonials::after {
  content: '';
  position: absolute;
  top: 0; left: 10%; right: 10%;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(74,144,196,0.25), transparent);
}
#services, #testimonials { position: relative; }

/* Number counter color */
.stat-num, .bo-stat-num { color: var(--blue-accent) !important; }

/* Broker section dark bg update */
#broker .broker-inner {
  background: linear-gradient(135deg, #0A1E35 0%, #0F2744 60%, #071828 100%) !important;
}

/* Line CTA section */
#line-cta {
  background: linear-gradient(135deg, #0F2744 0%, #1B3A5C 50%, #0F2744 100%) !important;
}

/* Hero gradient overlays */
.hero-slide::before {
  background: linear-gradient(135deg, rgba(15,39,68,0.72) 0%, rgba(15,39,68,0.28) 100%) !important;
}
.hero-slide.slide-2::before {
  background: linear-gradient(135deg, rgba(8,20,45,0.65) 0%, rgba(8,20,45,0.22) 100%) !important;
}
.hero-slide.slide-3::before {
  background: linear-gradient(135deg, rgba(10,30,60,0.60) 0%, rgba(10,30,60,0.18) 100%) !important;
}

/* Booking overlay: left panel blue */
.bk-left {
  background: linear-gradient(160deg, #0F2744 0%, #1B3A5C 60%, #0F2744 100%) !important;
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + ARTISTIC_CSS + '\n' + html[style_end:]
print("A3. Artistic CSS: OK")

# ═══════════════════════════════════════════════════════════════════════════════
# PART B: 裝潢方案 OVERLAY
# ═══════════════════════════════════════════════════════════════════════════════

DECO_OVERLAY_HTML = """
<!-- ═══ DECORATION STYLES OVERLAY ═══ -->
<div id="decoOverlay" style="display:none;position:fixed;inset:0;z-index:9200;background:#F2F6FB;overflow-y:auto;">

  <!-- Sticky header -->
  <div style="position:sticky;top:0;z-index:20;background:rgba(242,246,251,0.97);backdrop-filter:blur(16px);border-bottom:1px solid #C8DAEA;padding:.9rem 2.5rem;display:flex;align-items:center;justify-content:space-between;">
    <div style="display:flex;align-items:center;gap:1rem;">
      <button onclick="closeDecoOverlay()" style="width:38px;height:38px;border-radius:50%;border:1.5px solid #C8DAEA;background:none;cursor:pointer;font-size:1.1rem;color:#3A5068;display:flex;align-items:center;justify-content:center;transition:all .2s;" onmouseover="this.style.background='#1B3A5C';this.style.color='#fff';this.style.borderColor='#1B3A5C'" onmouseout="this.style.background='none';this.style.color='#3A5068';this.style.borderColor='#C8DAEA'">←</button>
      <div>
        <div style="font-family:'Noto Serif TC',serif;font-size:.95rem;font-weight:700;color:#0F2744;">裝潢風格方案</div>
        <div style="font-size:.72rem;color:#7A8FA6;letter-spacing:.08em;">6 種精選風格 · 30 天極速完工 · 保固 2 年</div>
      </div>
    </div>
    <button onclick="openBookingOverlay()" style="background:var(--gold);color:#fff;border:none;border-radius:10px;padding:.5rem 1.3rem;font-size:.8rem;font-weight:600;cursor:pointer;font-family:inherit;">🏠 預約賞屋</button>
  </div>

  <!-- Hero banner -->
  <div style="width:100%;height:320px;background:linear-gradient(135deg,rgba(15,39,68,0.88) 0%,rgba(27,58,92,0.72) 100%),url('https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1920&h=600&fit=crop&auto=format') center/cover no-repeat;display:flex;align-items:center;justify-content:center;text-align:center;">
    <div>
      <div style="font-size:.72rem;letter-spacing:.3em;color:var(--gold);margin-bottom:.8rem;text-transform:uppercase;">Interior Design Plans</div>
      <h2 style="font-family:'Noto Serif TC',serif;font-size:2.2rem;font-weight:700;color:#fff;text-shadow:0 2px 20px rgba(0,0,0,.3);margin-bottom:.8rem;">選擇您的理想生活風格</h2>
      <p style="font-size:.88rem;color:rgba(255,255,255,.7);max-width:560px;line-height:1.8;">從清新北歐到典雅日式，每一種風格都由專業設計師精心規劃，<br/>30 天內完工，讓您入住即享受美好生活。</p>
    </div>
  </div>

  <!-- Price banner -->
  <div style="background:linear-gradient(90deg,#0F2744,#1B3A5C,#0F2744);padding:1rem 2.5rem;display:flex;align-items:center;justify-content:center;gap:3rem;flex-wrap:wrap;">
    <div style="text-align:center;color:#fff;"><div style="font-size:1.1rem;font-weight:700;color:var(--gold);">$8萬起</div><div style="font-size:.7rem;color:rgba(255,255,255,.55);letter-spacing:.08em;margin-top:.2rem;">輕裝修方案</div></div>
    <div style="width:1px;height:32px;background:rgba(255,255,255,.15);"></div>
    <div style="text-align:center;color:#fff;"><div style="font-size:1.1rem;font-weight:700;color:var(--gold);">$18萬起</div><div style="font-size:.7rem;color:rgba(255,255,255,.55);letter-spacing:.08em;margin-top:.2rem;">標準裝修方案</div></div>
    <div style="width:1px;height:32px;background:rgba(255,255,255,.15);"></div>
    <div style="text-align:center;color:#fff;"><div style="font-size:1.1rem;font-weight:700;color:var(--gold);">$35萬起</div><div style="font-size:.7rem;color:rgba(255,255,255,.55);letter-spacing:.08em;margin-top:.2rem;">精裝全包方案</div></div>
    <div style="width:1px;height:32px;background:rgba(255,255,255,.15);"></div>
    <div style="text-align:center;color:#fff;"><div style="font-size:1.1rem;font-weight:700;color:#fff;">30天</div><div style="font-size:.7rem;color:rgba(255,255,255,.55);letter-spacing:.08em;margin-top:.2rem;">極速完工</div></div>
    <div style="width:1px;height:32px;background:rgba(255,255,255,.15);"></div>
    <div style="text-align:center;color:#fff;"><div style="font-size:1.1rem;font-weight:700;color:#fff;">2年</div><div style="font-size:.7rem;color:rgba(255,255,255,.55);letter-spacing:.08em;margin-top:.2rem;">完工保固</div></div>
  </div>

  <!-- Style cards -->
  <div style="max-width:1140px;margin:0 auto;padding:3rem 2rem 5rem;">

    <!-- Header -->
    <div style="text-align:center;margin-bottom:3rem;">
      <div style="font-size:.72rem;letter-spacing:.25em;color:var(--gold);text-transform:uppercase;margin-bottom:.6rem;">Our Design Styles</div>
      <h3 style="font-family:'Noto Serif TC',serif;font-size:1.6rem;font-weight:700;color:#0F2744;">精選六大裝潢風格</h3>
      <div style="width:50px;height:2px;background:linear-gradient(90deg,transparent,var(--gold),transparent);margin:1rem auto;"></div>
    </div>

    <!-- STYLE 1: 現代簡約 -->
    <div class="deco-style-card">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1600210492486-724fe5c67fb3?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1615529182904-14819c35db37?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">01</div>
        <h4 class="deco-style-name">現代簡約</h4>
        <div class="deco-style-en">Modern Minimalist</div>
        <p class="deco-style-desc">以「少即是多」為核心哲學，運用純白、灰調、木紋等中性色系，搭配幾何線條與無印風傢飾，打造乾淨俐落的都市感居所。空間開闊通透，讓生活回歸本質。</p>
        <div class="deco-features">
          <span class="deco-feat">開放式格局</span>
          <span class="deco-feat">隱藏收納</span>
          <span class="deco-feat">純白牆面</span>
          <span class="deco-feat">木質地板</span>
          <span class="deco-feat">燈光設計</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$18萬起</div><div class="deco-price-note">含基礎傢飾軟裝</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- STYLE 2: 日式和風 -->
    <div class="deco-style-card deco-reverse">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1614846384571-1e31322c0c9b?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1603827457577-609e6f42a45e?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">02</div>
        <h4 class="deco-style-name">日式和風</h4>
        <div class="deco-style-en">Japanese Wabi-Sabi</div>
        <p class="deco-style-desc">取法日本侘寂美學，以榻榻米、清水模、竹編、紙拉門等自然素材構築靜謐氛圍。淡雅的米色系搭配不完美的手工質感，在忙碌城市中找回身心平靜的歸宿。</p>
        <div class="deco-features">
          <span class="deco-feat">榻榻米臥室</span>
          <span class="deco-feat">竹編格柵</span>
          <span class="deco-feat">清水模牆</span>
          <span class="deco-feat">枯山水元素</span>
          <span class="deco-feat">和室書房</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$22萬起</div><div class="deco-price-note">含和室訂製工程</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- STYLE 3: 輕奢北歐 -->
    <div class="deco-style-card">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1540518614846-7eded433c457?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1484154218962-a197022b5858?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">03</div>
        <h4 class="deco-style-name">輕奢北歐</h4>
        <div class="deco-style-en">Nordic Luxe</div>
        <p class="deco-style-desc">融合北歐功能主義與輕奢質感，以燕麥白、暖灰、霧金為主色調，輔以大理石紋路、黃銅五金、絨布傢飾，在簡潔中蘊藏低調品味，散發溫柔而高雅的生活氣息。</p>
        <div class="deco-features">
          <span class="deco-feat">大理石島台</span>
          <span class="deco-feat">黃銅燈飾</span>
          <span class="deco-feat">絨布沙發</span>
          <span class="deco-feat">圓弧線條</span>
          <span class="deco-feat">植栽造景</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$28萬起</div><div class="deco-price-note">含精選傢飾家電</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- STYLE 4: 工業美式 -->
    <div class="deco-style-card deco-reverse">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1565182999561-18d7dc61c393?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1560185008-b033106af5c3?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">04</div>
        <h4 class="deco-style-name">工業美式</h4>
        <div class="deco-style-en">Industrial Loft</div>
        <p class="deco-style-desc">保留建築原始肌理，以裸露磚牆、混凝土天花、金屬管線為設計語言，搭配皮革沙發、復古地毯與黑鐵燈架，打造剛柔並濟的 Loft 生活態度，適合喜愛個性空間的都市人。</p>
        <div class="deco-features">
          <span class="deco-feat">裸露磚牆</span>
          <span class="deco-feat">金屬吊燈</span>
          <span class="deco-feat">水泥地坪</span>
          <span class="deco-feat">開放書架</span>
          <span class="deco-feat">皮革傢飾</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$25萬起</div><div class="deco-price-note">含特殊工法塗料</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- STYLE 5: 台式人文 -->
    <div class="deco-style-card">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1598928636135-d146006ff4be?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1545241047-6083a3684587?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">05</div>
        <h4 class="deco-style-name">台式人文</h4>
        <div class="deco-style-en">Taiwanese Humanistic</div>
        <p class="deco-style-desc">以台灣本土文化為底蘊，融合閩南磁磚、檜木窗花、編織藺草等傳統工藝，以現代手法重新詮釋，展現溫暖敦厚的人文情懷。適合珍視在地記憶、尋找歸屬感的家庭。</p>
        <div class="deco-features">
          <span class="deco-feat">花磁磚牆面</span>
          <span class="deco-feat">檜木格柵</span>
          <span class="deco-feat">藺草編織</span>
          <span class="deco-feat">陶藝擺設</span>
          <span class="deco-feat">老件傢具</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$20萬起</div><div class="deco-price-note">含在地工藝訂製</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- STYLE 6: 古典歐式 -->
    <div class="deco-style-card deco-reverse">
      <div class="deco-gallery">
        <div class="deco-gallery-main" style="background-image:url('https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=800&h=520&fit=crop&auto=format')"></div>
        <div class="deco-gallery-side">
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1618219740975-d40978bb7378?w=400&h=260&fit=crop&auto=format')"></div>
          <div class="deco-gallery-thumb" style="background-image:url('https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=400&h=260&fit=crop&auto=format')"></div>
        </div>
        <div class="deco-gallery-strip">
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=300&h=200&fit=crop&auto=format')"></div>
          <div class="deco-gallery-strip-img" style="background-image:url('https://images.unsplash.com/photo-1497366216548-37526070297c?w=300&h=200&fit=crop&auto=format')"></div>
        </div>
      </div>
      <div class="deco-info">
        <div class="deco-style-tag">06</div>
        <h4 class="deco-style-name">古典歐式</h4>
        <div class="deco-style-en">Classical European</div>
        <p class="deco-style-desc">以法式新古典為靈感，雕刻線板、水晶吊燈、鍍金壁鏡、大理石壁爐構成奢華舞台。深邃的酒紅、孔雀綠、香檳金交織出時光沉澱的貴族氣韻，適合追求永恆典雅的品味人士。</p>
        <div class="deco-features">
          <span class="deco-feat">雕刻線板</span>
          <span class="deco-feat">水晶吊燈</span>
          <span class="deco-feat">大理石地坪</span>
          <span class="deco-feat">訂製壁爐</span>
          <span class="deco-feat">絲絨窗簾</span>
        </div>
        <div class="deco-price-row">
          <div><div class="deco-price">$45萬起</div><div class="deco-price-note">含進口建材傢飾</div></div>
          <button onclick="openBookingOverlay()" class="deco-cta-btn">預約諮詢</button>
        </div>
      </div>
    </div>

    <!-- Bottom CTA -->
    <div style="margin-top:3rem;background:linear-gradient(135deg,#0F2744,#1B3A5C);border-radius:20px;padding:3rem;text-align:center;color:#fff;">
      <div style="font-family:'Noto Serif TC',serif;font-size:1.3rem;font-weight:700;margin-bottom:.6rem;">找不到心目中的風格？</div>
      <div style="font-size:.85rem;color:rgba(255,255,255,.65);margin-bottom:1.5rem;line-height:1.8;">我們的設計師可以為您量身打造專屬風格，<br/>結合您的生活習慣與美學偏好，創造獨一無二的家。</div>
      <div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;">
        <button onclick="openBookingOverlay()" style="background:var(--gold);color:#fff;border:none;border-radius:12px;padding:.8rem 2.2rem;font-size:.88rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;">🏠 預約賞屋 × 設計諮詢</button>
        <a href="tel:0800-888-888" style="background:rgba(255,255,255,.1);color:#fff;border:1.5px solid rgba(255,255,255,.3);border-radius:12px;padding:.8rem 2.2rem;font-size:.88rem;font-weight:500;cursor:pointer;font-family:inherit;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;">📞 立即致電洽詢</a>
      </div>
    </div>
  </div>
</div>
"""

body_end = html.rfind('</body>')
html = html[:body_end] + '\n' + DECO_OVERLAY_HTML + '\n' + html[body_end:]
print("B1. Deco overlay HTML: OK")

# ─── Deco overlay CSS
DECO_CSS = """
/* ── DECORATION OVERLAY ───────────────────────── */
#decoOverlay {
  scrollbar-width: thin;
  scrollbar-color: var(--gold) transparent;
}
.deco-style-card {
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 2.5rem;
  margin-bottom: 4rem;
  align-items: start;
  padding-bottom: 3.5rem;
  border-bottom: 1px solid #C8DAEA;
}
.deco-style-card.deco-reverse {
  grid-template-columns: 1fr 1.1fr;
  direction: rtl;
}
.deco-style-card.deco-reverse > * { direction: ltr; }
.deco-gallery { display: flex; flex-direction: column; gap: .5rem; }
.deco-gallery-main {
  width: 100%;
  height: 320px;
  background-size: cover;
  background-position: center;
  border-radius: 14px;
  cursor: zoom-in;
  transition: transform .4s;
  overflow: hidden;
}
.deco-gallery-main:hover { transform: scale(1.015); }
.deco-gallery-side {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: .5rem;
}
.deco-gallery-thumb {
  height: 140px;
  background-size: cover;
  background-position: center;
  border-radius: 10px;
  cursor: pointer;
  transition: transform .3s, box-shadow .3s;
  overflow: hidden;
}
.deco-gallery-thumb:hover { transform: scale(1.03); box-shadow: 0 8px 24px rgba(27,58,92,.2); }
.deco-gallery-strip {
  display: grid;
  grid-template-columns: repeat(3,1fr);
  gap: .5rem;
}
.deco-gallery-strip-img {
  height: 90px;
  background-size: cover;
  background-position: center;
  border-radius: 8px;
  cursor: pointer;
  transition: transform .3s;
}
.deco-gallery-strip-img:hover { transform: scale(1.04); }
.deco-info {
  padding: .5rem 0;
  display: flex;
  flex-direction: column;
  gap: .6rem;
}
.deco-style-tag {
  font-size: 3rem;
  font-family: 'Noto Serif TC', serif;
  font-weight: 900;
  color: rgba(27,58,92,0.08);
  line-height: 1;
  margin-bottom: -.6rem;
  letter-spacing: -.02em;
}
.deco-style-name {
  font-family: 'Noto Serif TC', serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: #0F2744;
  margin: 0;
}
.deco-style-en {
  font-size: .72rem;
  letter-spacing: .2em;
  color: var(--gold);
  text-transform: uppercase;
  margin-top: -.2rem;
}
.deco-style-desc {
  font-size: .87rem;
  color: #3A5068;
  line-height: 2;
  margin: .4rem 0;
}
.deco-features {
  display: flex;
  flex-wrap: wrap;
  gap: .4rem;
  margin: .2rem 0;
}
.deco-feat {
  font-size: .72rem;
  background: rgba(27,58,92,.07);
  color: #1B3A5C;
  border-radius: 20px;
  padding: .28rem .75rem;
  font-weight: 500;
  border: 1px solid rgba(27,58,92,.12);
}
.deco-price-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: .8rem;
  padding-top: .8rem;
  border-top: 1px solid #C8DAEA;
}
.deco-price {
  font-size: 1.4rem;
  font-weight: 800;
  font-family: 'Noto Serif TC', serif;
  background: linear-gradient(135deg, var(--gold), #b8953e);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}
.deco-price-note { font-size: .72rem; color: #7A8FA6; margin-top: .15rem; }
.deco-cta-btn {
  background: linear-gradient(135deg, #1B3A5C, #2E6CA4);
  color: #fff;
  border: none;
  border-radius: 10px;
  padding: .65rem 1.5rem;
  font-size: .82rem;
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
  letter-spacing: .04em;
  transition: all .25s;
}
.deco-cta-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(27,58,92,.25);
}

/* Gallery lightbox on click */
.deco-gallery-main:active { transform: scale(0.99); }

@media (max-width: 768px) {
  .deco-style-card,
  .deco-style-card.deco-reverse { grid-template-columns: 1fr; direction: ltr; }
  .deco-gallery-main { height: 220px; }
  .deco-gallery-thumb { height: 100px; }
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + DECO_CSS + '\n' + html[style_end:]
print("B2. Deco CSS: OK")

# ─── Deco overlay JS
DECO_JS = """
/* ===== DECORATION OVERLAY ===== */
function openDecoOverlay() {
  const el = document.getElementById('decoOverlay');
  el.style.display = 'block';
  el.scrollTop = 0;
  document.body.style.overflow = 'hidden';
}
function closeDecoOverlay() {
  document.getElementById('decoOverlay').style.display = 'none';
  document.body.style.overflow = '';
}
// Gallery main image swap on thumb click
document.querySelectorAll('.deco-gallery-thumb, .deco-gallery-strip-img').forEach(thumb => {
  thumb.addEventListener('click', function() {
    const main = this.closest('.deco-gallery').querySelector('.deco-gallery-main');
    const bg = this.style.backgroundImage;
    const old = main.style.backgroundImage;
    main.style.backgroundImage = bg;
    this.style.backgroundImage = old;
  });
});
"""

script_end = html.rfind('</script>', 0, html.rfind('</body>'))
html = html[:script_end] + '\n' + DECO_JS + '\n' + html[script_end:]
print("B3. Deco JS: OK")

# ─── Wire the button
OLD_DECO_BTN = """<a href="#" class="btn btn-gold">了解裝潢方案</a>"""
NEW_DECO_BTN = """<a href="#" onclick="openDecoOverlay();return false;" class="btn btn-gold">了解裝潢方案</a>"""
html = html.replace(OLD_DECO_BTN, NEW_DECO_BTN, 1)
print("B4. Button wired:", "OK" if OLD_DECO_BTN not in html else "MISS")

# Save
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done! fix5 complete.")
