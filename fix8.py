# -*- coding: utf-8 -*-
"""
fix8.py
1. Circular carousel – Projects & Reels show wrapped neighbours
2. Navbar logo (SVG icon) + English name "YUCHEN PROPERTIES"
3. Deco overlay → full-screen slider (one style per slide, vertical photo scroll)
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1.  CIRCULAR CAROUSEL  — fix offset so index 0 wraps to see last card on left
# ─────────────────────────────────────────────────────────────────────────────

OLD_PROJ_RENDER = """  function renderProjectsCF() {
    const cards = [...document.querySelectorAll('#projectsSlider .project-card')];
    cards.forEach((card, i) => {
      const off = i - projCFIdx;
      const abs = Math.abs(off), sign = Math.sign(off) || 1;"""

NEW_PROJ_RENDER = """  function renderProjectsCF() {
    const cards = [...document.querySelectorAll('#projectsSlider .project-card')];
    const n = cards.length;
    cards.forEach((card, i) => {
      let off = i - projCFIdx;
      off = ((off % n) + n) % n; if (off > n / 2) off -= n; // circular
      const abs = Math.abs(off), sign = Math.sign(off) || 1;"""

html = html.replace(OLD_PROJ_RENDER, NEW_PROJ_RENDER, 1)
print("1a. Projects circular offset:", "OK" if OLD_PROJ_RENDER not in html else "MISS")

OLD_REEL_RENDER = """  function renderReelsCF() {
    const cards = [...document.querySelectorAll('#reelsSlider .reel-card')];
    cards.forEach((card, i) => {
      const off = i - reelCFIdx;
      const abs = Math.abs(off), sign = Math.sign(off) || 1;"""

NEW_REEL_RENDER = """  function renderReelsCF() {
    const cards = [...document.querySelectorAll('#reelsSlider .reel-card')];
    const n = cards.length;
    cards.forEach((card, i) => {
      let off = i - reelCFIdx;
      off = ((off % n) + n) % n; if (off > n / 2) off -= n; // circular
      const abs = Math.abs(off), sign = Math.sign(off) || 1;"""

html = html.replace(OLD_REEL_RENDER, NEW_REEL_RENDER, 1)
print("1b. Reels circular offset:", "OK" if OLD_REEL_RENDER not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 2. NAVBAR LOGO + ENGLISH NAME
# ─────────────────────────────────────────────────────────────────────────────

OLD_NAV_LOGO_CSS = """    .nav-logo {
      font-family: 'Noto Serif TC', serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--white);
      letter-spacing: 0.05em;
      transition: var(--transition);
    }
    #navbar.scrolled .nav-logo { color: var(--green-dark); }"""

NEW_NAV_LOGO_CSS = """    .nav-logo {
      display: flex; align-items: center; gap: .65rem;
      text-decoration: none; cursor: pointer;
      transition: var(--transition);
    }
    .nav-logo-icon {
      width: 36px; height: 36px; flex-shrink: 0;
      filter: drop-shadow(0 2px 6px rgba(200,169,110,.35));
    }
    .nav-logo-text { display: flex; flex-direction: column; line-height: 1; }
    .nav-logo-cn {
      font-family: 'Noto Serif TC', serif;
      font-size: 1.2rem; font-weight: 700;
      color: var(--white); letter-spacing: .05em;
      transition: var(--transition);
    }
    .nav-logo-en {
      font-size: .6rem; letter-spacing: .2em;
      color: var(--gold); text-transform: uppercase;
      margin-top: .15rem; font-weight: 500;
      transition: var(--transition);
    }
    #navbar.scrolled .nav-logo-cn { color: var(--green-dark); }
    #navbar.scrolled .nav-logo-en { color: var(--green-mid); }"""

html = html.replace(OLD_NAV_LOGO_CSS, NEW_NAV_LOGO_CSS, 1)
print("2a. Nav logo CSS:", "OK" if OLD_NAV_LOGO_CSS not in html else "MISS")

OLD_NAV_LOGO_HTML = """  <div class="nav-logo">譽誠廣告</div>"""
NEW_NAV_LOGO_HTML = """  <a class="nav-logo" href="#" onclick="window.scrollTo({top:0,behavior:'smooth'});return false;">
    <svg class="nav-logo-icon" viewBox="0 0 36 36" fill="none" xmlns="http://www.w3.org/2000/svg">
      <rect width="36" height="36" rx="8" fill="#1B3A5C"/>
      <!-- building shape -->
      <path d="M18 7L6 16v14h8V22h8v8h8V16L18 7z" fill="#C8A96E" opacity=".9"/>
      <rect x="15" y="22" width="6" height="9" rx="1" fill="#0F2744"/>
      <rect x="10" y="18" width="4" height="4" rx="0.5" fill="rgba(255,255,255,.55)"/>
      <rect x="22" y="18" width="4" height="4" rx="0.5" fill="rgba(255,255,255,.55)"/>
      <path d="M18 7l-2 2 2-2z" fill="#C8A96E"/>
    </svg>
    <div class="nav-logo-text">
      <span class="nav-logo-cn">譽誠廣告</span>
      <span class="nav-logo-en">Yuchen Properties</span>
    </div>
  </a>"""

html = html.replace(OLD_NAV_LOGO_HTML, NEW_NAV_LOGO_HTML, 1)
print("2b. Nav logo HTML:", "OK" if OLD_NAV_LOGO_HTML not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 3. DECO OVERLAY – full rewrite as slider
# ─────────────────────────────────────────────────────────────────────────────

# Helper to build a slide
FEAT_STYLE = "background:rgba(255,255,255,.1);color:rgba(255,255,255,.82);border-radius:20px;padding:.28rem .75rem;font-size:.71rem;"

def feat(label): return f'<span style="{FEAT_STYLE}">{label}</span>'
def feats(*labels): return ''.join(feat(l) for l in labels)

IMG_STYLE = "width:100%;height:240px;object-fit:cover;border-radius:10px;flex-shrink:0;"
def img(url): return f'<img src="{url}" style="{IMG_STYLE}" loading="lazy">'

SLIDE_DATA = [
    {
        "num": "01", "cn": "現代簡約", "en": "Modern Minimalist",
        "desc": "以「少即是多」為核心哲學，運用純白、灰調、木紋等中性色系，搭配幾何線條與無印風傢飾，打造乾淨俐落的都市感居所。空間開闊通透，讓生活回歸本質。",
        "feats": ["開放式格局","隱藏收納","純白牆面","木質地板","燈光設計"],
        "price": "$18萬起", "note": "含基礎傢飾軟裝",
        "imgs": [
            "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600210492486-724fe5c67fb3?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=900&h=540&fit=crop&auto=format",
        ]
    },
    {
        "num": "02", "cn": "日式和風", "en": "Japanese Wabi-Sabi",
        "desc": "取法日本侘寂美學，以榻榻米、清水模、竹編、紙拉門等自然素材構築靜謐氛圍。淡雅的米色系搭配手工質感，在忙碌城市中找回身心平靜的歸宿。",
        "feats": ["榻榻米臥室","竹編格柵","清水模牆","枯山水元素","和室書房"],
        "price": "$22萬起", "note": "含和室訂製工程",
        "imgs": [
            "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1614846384571-1e31322c0c9b?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1603827457577-609e6f42a45e?w=900&h=540&fit=crop&auto=format",
        ]
    },
    {
        "num": "03", "cn": "輕奢北歐", "en": "Nordic Luxe",
        "desc": "融合北歐功能主義與輕奢質感，以燕麥白、暖灰、霧金為主色調，輔以大理石紋路、黃銅五金、絨布傢飾，在簡潔中蘊藏低調品味。",
        "feats": ["大理石島台","黃銅燈飾","絨布沙發","圓弧線條","植栽造景"],
        "price": "$28萬起", "note": "含精選傢飾家電",
        "imgs": [
            "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1540518614846-7eded433c457?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=900&h=540&fit=crop&auto=format",
        ]
    },
    {
        "num": "04", "cn": "工業美式", "en": "Industrial Loft",
        "desc": "保留建築原始肌理，以裸露磚牆、混凝土天花、金屬管線為設計語言，搭配皮革沙發、復古地毯與黑鐵燈架，打造剛柔並濟的 Loft 生活態度。",
        "feats": ["裸露磚牆","金屬吊燈","水泥地坪","開放書架","皮革傢飾"],
        "price": "$25萬起", "note": "含特殊工法塗料",
        "imgs": [
            "https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1565182999561-18d7dc61c393?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560185008-b033106af5c3?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=900&h=540&fit=crop&auto=format",
        ]
    },
    {
        "num": "05", "cn": "台式人文", "en": "Taiwanese Humanistic",
        "desc": "以台灣本土文化為底蘊，融合閩南磁磚、檜木窗花、編織藺草等傳統工藝，以現代手法重新詮釋，展現溫暖敦厚的人文情懷。",
        "feats": ["花磁磚牆面","檜木格柵","藺草編織","陶藝擺設","老件傢具"],
        "price": "$20萬起", "note": "含在地工藝訂製",
        "imgs": [
            "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1598928636135-d146006ff4be?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1545241047-6083a3684587?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=900&h=540&fit=crop&auto=format",
        ]
    },
    {
        "num": "06", "cn": "古典歐式", "en": "Classical European",
        "desc": "以法式新古典為靈感，雕刻線板、水晶吊燈、鍍金壁鏡、大理石壁爐構成奢華舞台。深邃的酒紅、孔雀綠、香檳金交織出時光沉澱的貴族氣韻。",
        "feats": ["雕刻線板","水晶吊燈","大理石地坪","訂製壁爐","絲絨窗簾"],
        "price": "$45萬起", "note": "含進口建材傢飾",
        "imgs": [
            "https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1618219740975-d40978bb7378?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=900&h=540&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=900&h=540&fit=crop&auto=format",
        ]
    },
]

def build_slide(d):
    photos_html = '\n        '.join(img(u) for u in d['imgs'])
    feats_html  = '\n          '.join(feat(f) for f in d['feats'])
    return f"""    <!-- SLIDE {d['num']} -->
    <div style="width:16.6667%;height:100%;display:flex;flex-shrink:0;overflow:hidden;">
      <!-- Info panel -->
      <div style="width:40%;height:100%;overflow-y:auto;background:linear-gradient(170deg,#0F2744 0%,#0A1828 100%);padding:2rem 1.8rem 2rem 2.2rem;box-sizing:border-box;border-right:1px solid rgba(200,218,234,.1);">
        <div style="font-size:4.5rem;font-family:'Noto Serif TC',serif;font-weight:700;color:rgba(200,169,110,.18);line-height:1;user-select:none;">{d['num']}</div>
        <h3 style="font-family:'Noto Serif TC',serif;font-size:1.9rem;font-weight:700;color:#fff;margin:.2rem 0 .25rem;">{d['cn']}</h3>
        <div style="font-size:.72rem;letter-spacing:.2em;color:var(--gold);margin-bottom:1.4rem;">{d['en'].upper()}</div>
        <p style="font-size:.84rem;color:rgba(255,255,255,.68);line-height:1.95;margin-bottom:1.6rem;">{d['desc']}</p>
        <div style="display:flex;flex-wrap:wrap;gap:.4rem;margin-bottom:2rem;">
          {feats_html}
        </div>
        <div style="background:rgba(200,169,110,.12);border:1px solid rgba(200,169,110,.2);border-radius:12px;padding:1.1rem 1.2rem;margin-bottom:1.5rem;">
          <div style="font-family:'Noto Serif TC',serif;font-size:1.5rem;font-weight:700;color:var(--gold);">{d['price']}</div>
          <div style="font-size:.7rem;color:rgba(255,255,255,.45);margin-top:.2rem;">{d['note']}</div>
        </div>
        <button onclick="openBookingOverlay()" style="width:100%;background:var(--gold);color:#fff;border:none;border-radius:10px;padding:.85rem;font-size:.85rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;">預約設計諮詢 →</button>
      </div>
      <!-- Photos panel -->
      <div style="width:60%;height:100%;overflow-y:auto;background:#081420;padding:1.2rem 1.2rem 1.2rem 1rem;box-sizing:border-box;display:flex;flex-direction:column;gap:.9rem;">
        {photos_html}
      </div>
    </div>"""

slides_html = '\n'.join(build_slide(d) for d in SLIDE_DATA)

# Dot markup (JS will init active state)
dots_init = '\n        '.join(
    f'<span class="deco-sdot" onclick="slideDecoToIdx({i})" style="display:inline-block;height:8px;border-radius:4px;background:var(--gold);cursor:pointer;transition:all .3s;width:{"20px" if i==0 else "8px"};opacity:{"1" if i==0 else "0.3"};"></span>'
    for i in range(6)
)

BTN_BASE = "border:1.5px solid rgba(255,255,255,.22);color:#fff;cursor:pointer;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(6px);transition:background .2s;"
HDR_BTN  = f"width:32px;height:32px;border-radius:50%;background:rgba(255,255,255,.1);font-size:1.05rem;{BTN_BASE}"
SIDE_BTN = f"position:absolute;top:50%;transform:translateY(-50%);z-index:15;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.14);font-size:1.5rem;{BTN_BASE}"

NEW_DECO_OVERLAY = f"""<!-- ═══ DECORATION STYLES OVERLAY ═══ -->
<div id="decoOverlay" style="display:none;position:fixed;inset:0;z-index:9200;overflow:hidden;background:#081420;">

  <!-- ── Header ── -->
  <div style="position:absolute;top:0;left:0;right:0;height:62px;z-index:20;background:rgba(8,20,32,.97);backdrop-filter:blur(16px);border-bottom:1px solid rgba(200,218,234,.12);padding:0 1.8rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;box-sizing:border-box;">
    <!-- back + title -->
    <div style="display:flex;align-items:center;gap:.8rem;flex-shrink:0;">
      <button onclick="closeDecoOverlay()" style="width:36px;height:36px;border-radius:50%;{BTN_BASE}background:rgba(255,255,255,.08);" onmouseover="this.style.background='rgba(255,255,255,.18)'" onmouseout="this.style.background='rgba(255,255,255,.08)'">←</button>
      <div>
        <div style="font-family:'Noto Serif TC',serif;font-size:.92rem;font-weight:700;color:#fff;">裝潢風格方案</div>
        <div style="font-size:.67rem;color:rgba(255,255,255,.4);letter-spacing:.07em;">6 種精選風格 · 30 天極速完工 · 保固 2 年</div>
      </div>
    </div>
    <!-- dots + arrows -->
    <div style="display:flex;align-items:center;gap:.55rem;">
      <button onclick="slideDecoStyle(-1)" style="{HDR_BTN}" onmouseover="this.style.background='rgba(200,169,110,.6)'" onmouseout="this.style.background='rgba(255,255,255,.1)'">‹</button>
      <div id="decoDots" style="display:flex;align-items:center;gap:5px;">
        {dots_init}
      </div>
      <button onclick="slideDecoStyle(1)" style="{HDR_BTN}" onmouseover="this.style.background='rgba(200,169,110,.6)'" onmouseout="this.style.background='rgba(255,255,255,.1)'">›</button>
      <span id="decoCtr" style="font-size:.75rem;color:rgba(255,255,255,.45);letter-spacing:.07em;min-width:3.2rem;text-align:center;">01 / 06</span>
    </div>
    <!-- CTA -->
    <button onclick="openBookingOverlay()" style="flex-shrink:0;background:var(--gold);color:#fff;border:none;border-radius:8px;padding:.48rem 1.1rem;font-size:.78rem;font-weight:600;cursor:pointer;font-family:inherit;white-space:nowrap;letter-spacing:.03em;">🏠 預約諮詢</button>
  </div>

  <!-- ── Slide Track ── -->
  <div id="decoTrack" style="position:absolute;top:62px;left:0;bottom:0;display:flex;width:600%;transition:transform .48s cubic-bezier(.25,.46,.45,.94);">
{slides_html}
  </div>

  <!-- ── Floating side arrows ── -->
  <button onclick="slideDecoStyle(-1)" style="{SIDE_BTN}left:1rem;" onmouseover="this.style.background='rgba(200,169,110,.75)'" onmouseout="this.style.background='rgba(255,255,255,.14)'">‹</button>
  <button onclick="slideDecoStyle(1)"  style="{SIDE_BTN}right:1rem;" onmouseover="this.style.background='rgba(200,169,110,.75)'" onmouseout="this.style.background='rgba(255,255,255,.14)'">›</button>

</div>"""

# ── JS for deco slider ──
OLD_DECO_JS = """/* ===== DECORATION OVERLAY ===== */
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
});"""

NEW_DECO_JS = """/* ===== DECORATION OVERLAY ===== */
let decoStyleIdx = 0;
function _decoSync() {
  const track = document.getElementById('decoTrack');
  if (track) track.style.transform = `translateX(-${decoStyleIdx * (100/6)}%)`;
  const ctr = document.getElementById('decoCtr');
  if (ctr) ctr.textContent = String(decoStyleIdx+1).padStart(2,'0') + ' / 06';
  document.querySelectorAll('#decoDots .deco-sdot').forEach((d,i) => {
    d.style.opacity = i === decoStyleIdx ? '1' : '0.3';
    d.style.width   = i === decoStyleIdx ? '20px' : '8px';
  });
}
function slideDecoStyle(dir) {
  decoStyleIdx = (decoStyleIdx + dir + 6) % 6;
  _decoSync();
}
function slideDecoToIdx(n) { decoStyleIdx = n; _decoSync(); }
function openDecoOverlay() {
  const el = document.getElementById('decoOverlay');
  el.style.display = 'block';
  document.body.style.overflow = 'hidden';
  decoStyleIdx = 0; _decoSync();
}
function closeDecoOverlay() {
  document.getElementById('decoOverlay').style.display = 'none';
  document.body.style.overflow = '';
}"""

html = html.replace(OLD_DECO_JS, NEW_DECO_JS, 1)
print("3a. Deco JS:", "OK" if OLD_DECO_JS not in html else "MISS")

# Remove the old deco CSS (no longer needed for the grid layout)
OLD_DECO_CSS_MARKER = """/* ── DECORATION OVERLAY ───────────────────────── */
#decoOverlay {
  scrollbar-width: thin;
  scrollbar-color: var(--gold) transparent;
}"""
NEW_DECO_CSS_MARKER = """/* ── DECORATION OVERLAY ───────────────────────── */
#decoOverlay { scrollbar-width: thin; scrollbar-color: var(--gold) transparent; }"""
html = html.replace(OLD_DECO_CSS_MARKER, NEW_DECO_CSS_MARKER, 1)

# Replace the entire overlay HTML
start_marker = '<!-- ═══ DECORATION STYLES OVERLAY ═══ -->'
end_marker   = '</div>\n\n</body>'
start_pos = html.find(start_marker)
end_pos   = html.find(end_marker)
if start_pos != -1 and end_pos != -1:
    html = html[:start_pos] + NEW_DECO_OVERLAY + '\n\n</body>'  + html[end_pos+len(end_marker):]
    print("3b. Deco overlay HTML: OK")
else:
    print(f"3b. Deco overlay HTML: MISS (start={start_pos}, end={end_pos})")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("\nAll done — fix8 complete.")
