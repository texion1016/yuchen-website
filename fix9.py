# -*- coding: utf-8 -*-
"""
fix9.py  — Redesign deco overlay with:
  1. Light blue (#F2F6FB) background theme
  2. Natural photo aspect-ratio (no forced height)
  3. Content proportions matching the reference layout
     Left 42%: info panel (white card)  |  Right 58%: photos grid (scrollable)
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# Build helpers
# ─────────────────────────────────────────────────────────────────────────────

FEAT_STYLE = ("background:rgba(27,58,92,.09);color:#1B3A5C;"
              "border-radius:20px;padding:.28rem .75rem;font-size:.71rem;")
def feat(label):
    return f'<span style="{FEAT_STYLE}">{label}</span>'

# Photos: 1 large (full width, 16:9) + 2×2 grid (4:3 each)
# Total 5 images per style — img[0] large, img[1-4] in 2-col grid
def build_photos(imgs):
    large = imgs[0]
    rest  = imgs[1:]
    large_html = (
        f'<img src="{large}" '
        'style="width:100%;aspect-ratio:16/9;object-fit:cover;'
        'border-radius:8px;display:block;" loading="lazy">'
    )
    grid_items = ''.join(
        f'<img src="{u}" '
        'style="width:100%;aspect-ratio:4/3;object-fit:cover;'
        'border-radius:8px;display:block;" loading="lazy">'
        for u in rest
    )
    grid_html = (
        f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:.7rem;">'
        f'{grid_items}</div>'
    )
    return large_html + '\n' + grid_html

def build_slide(d):
    feats_html  = '\n          '.join(feat(f) for f in d['feats'])
    photos_html = build_photos(d['imgs'])
    return f"""    <!-- SLIDE {d['num']} -->
    <div style="width:16.6667%;height:100%;display:flex;flex-shrink:0;overflow:hidden;background:#F2F6FB;">
      <!-- Info panel (white card) -->
      <div style="width:42%;height:100%;overflow-y:auto;background:#fff;padding:2.5rem 2.2rem 2.5rem 2.5rem;box-sizing:border-box;border-right:1px solid #DCE9F7;">
        <div style="font-size:5rem;font-family:'Noto Serif TC',serif;font-weight:700;color:rgba(15,39,68,.07);line-height:1;user-select:none;margin-bottom:.3rem;">{d['num']}</div>
        <h3 style="font-family:'Noto Serif TC',serif;font-size:2rem;font-weight:700;color:#0F2744;margin:.1rem 0 .3rem;">{d['cn']}</h3>
        <div style="font-size:.7rem;letter-spacing:.22em;color:#4A90C4;margin-bottom:1.4rem;">{d['en'].upper()}</div>
        <p style="font-size:.86rem;color:#4A6580;line-height:1.95;margin-bottom:1.7rem;">{d['desc']}</p>
        <div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:2rem;">
          {feats_html}
        </div>
        <div style="background:#F2F6FB;border:1px solid #DCE9F7;border-radius:12px;padding:1.1rem 1.3rem;margin-bottom:1.5rem;display:flex;align-items:center;justify-content:space-between;">
          <div>
            <div style="font-family:'Noto Serif TC',serif;font-size:1.5rem;font-weight:700;color:#C8A96E;">{d['price']}</div>
            <div style="font-size:.7rem;color:#7A8FA6;margin-top:.2rem;">{d['note']}</div>
          </div>
        </div>
        <button onclick="openBookingOverlay()" style="width:100%;background:linear-gradient(135deg,#1B3A5C,#2E6CA4);color:#fff;border:none;border-radius:10px;padding:.85rem;font-size:.85rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;">預約設計諮詢 →</button>
      </div>
      <!-- Photos panel (scrollable) -->
      <div style="width:58%;height:100%;overflow-y:auto;background:#EBF4FF;padding:1.5rem 1.8rem 1.5rem 1.2rem;box-sizing:border-box;display:flex;flex-direction:column;gap:.9rem;">
        {photos_html}
      </div>
    </div>"""

SLIDE_DATA = [
    {
        "num": "01", "cn": "現代簡約", "en": "Modern Minimalist",
        "desc": "以「少即是多」為核心哲學，運用純白、灰調、木紋等中性色系，搭配幾何線條與無印風傢飾，打造乾淨俐落的都市感居所。空間開闊通透，讓生活回歸本質。",
        "feats": ["開放式格局","隱藏收納","純白牆面","木質地板","燈光設計"],
        "price": "$18萬起", "note": "含基礎傢飾軟裝",
        "imgs": [
            "https://images.unsplash.com/photo-1618219908412-a29a1bb7b86e?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600210492486-724fe5c67fb3?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=600&h=450&fit=crop&auto=format",
        ]
    },
    {
        "num": "02", "cn": "日式和風", "en": "Japanese Wabi-Sabi",
        "desc": "取法日本侘寂美學，以榻榻米、清水模、竹編、紙拉門等自然素材構築靜謐氛圍。淡雅的米色系搭配手工質感，在忙碌城市中找回身心平靜的歸宿。",
        "feats": ["榻榻米臥室","竹編格柵","清水模牆","枯山水元素","和室書房"],
        "price": "$22萬起", "note": "含和室訂製工程",
        "imgs": [
            "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1614846384571-1e31322c0c9b?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1584622650111-993a426fbf0a?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1603827457577-609e6f42a45e?w=600&h=450&fit=crop&auto=format",
        ]
    },
    {
        "num": "03", "cn": "輕奢北歐", "en": "Nordic Luxe",
        "desc": "融合北歐功能主義與輕奢質感，以燕麥白、暖灰、霧金為主色調，輔以大理石紋路、黃銅五金、絨布傢飾，在簡潔中蘊藏低調品味。",
        "feats": ["大理石島台","黃銅燈飾","絨布沙發","圓弧線條","植栽造景"],
        "price": "$28萬起", "note": "含精選傢飾家電",
        "imgs": [
            "https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1616594039964-ae9021a400a0?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1540518614846-7eded433c457?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600585154526-990dced4db0d?w=600&h=450&fit=crop&auto=format",
        ]
    },
    {
        "num": "04", "cn": "工業美式", "en": "Industrial Loft",
        "desc": "保留建築原始肌理，以裸露磚牆、混凝土天花、金屬管線為設計語言，搭配皮革沙發、復古地毯與黑鐵燈架，打造剛柔並濟的 Loft 生活態度。",
        "feats": ["裸露磚牆","金屬吊燈","水泥地坪","開放書架","皮革傢飾"],
        "price": "$25萬起", "note": "含特殊工法塗料",
        "imgs": [
            "https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1565182999561-18d7dc61c393?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560185008-b033106af5c3?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&h=450&fit=crop&auto=format",
        ]
    },
    {
        "num": "05", "cn": "台式人文", "en": "Taiwanese Humanistic",
        "desc": "以台灣本土文化為底蘊，融合閩南磁磚、檜木窗花、編織藺草等傳統工藝，以現代手法重新詮釋，展現溫暖敦厚的人文情懷。",
        "feats": ["花磁磚牆面","檜木格柵","藺草編織","陶藝擺設","老件傢具"],
        "price": "$20萬起", "note": "含在地工藝訂製",
        "imgs": [
            "https://images.unsplash.com/photo-1600566753086-00f18fb6b3ea?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1598928636135-d146006ff4be?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560185127-6ed189bf02f4?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1545241047-6083a3684587?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1616046229478-9901c5536a45?w=600&h=450&fit=crop&auto=format",
        ]
    },
    {
        "num": "06", "cn": "古典歐式", "en": "Classical European",
        "desc": "以法式新古典為靈感，雕刻線板、水晶吊燈、鍍金壁鏡、大理石壁爐構成奢華舞台。深邃的酒紅、孔雀綠、香檳金交織出時光沉澱的貴族氣韻。",
        "feats": ["雕刻線板","水晶吊燈","大理石地坪","訂製壁爐","絲絨窗簾"],
        "price": "$45萬起", "note": "含進口建材傢飾",
        "imgs": [
            "https://images.unsplash.com/photo-1600121848594-d8644e57abab?w=900&h=506&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1618219740975-d40978bb7378?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600047509807-ba8f99d2cdde?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600&h=450&fit=crop&auto=format",
            "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=600&h=450&fit=crop&auto=format",
        ]
    },
]

slides_html = '\n'.join(build_slide(d) for d in SLIDE_DATA)

dots_init = '\n        '.join(
    '<span class="deco-sdot" onclick="slideDecoToIdx({i})" '
    'style="display:inline-block;height:8px;border-radius:4px;'
    'background:#1B3A5C;cursor:pointer;transition:all .3s;'
    'width:{w};opacity:{op};"></span>'.format(
        i=i, w="20px" if i == 0 else "8px", op="0.9" if i == 0 else "0.25"
    )
    for i in range(6)
)

# Header button styles (light theme)
HDR_BTN = ("width:32px;height:32px;border-radius:50%;"
           "background:rgba(27,58,92,.08);border:1.5px solid #C8DAEA;"
           "color:#1B3A5C;cursor:pointer;display:flex;align-items:center;"
           "justify-content:center;font-size:1.05rem;transition:background .2s;")
SIDE_BTN = ("position:absolute;top:50%;transform:translateY(-50%);z-index:15;"
            "width:44px;height:44px;border-radius:50%;"
            "background:rgba(255,255,255,.85);border:1.5px solid #C8DAEA;"
            "color:#1B3A5C;font-size:1.5rem;cursor:pointer;"
            "display:flex;align-items:center;justify-content:center;"
            "box-shadow:0 4px 16px rgba(27,58,92,.14);transition:all .2s;")

NEW_DECO_OVERLAY = f"""<!-- ═══ DECORATION STYLES OVERLAY ═══ -->
<div id="decoOverlay" style="display:none;position:fixed;inset:0;z-index:9200;overflow:hidden;background:#F2F6FB;">

  <!-- ── Header ── -->
  <div style="position:absolute;top:0;left:0;right:0;height:62px;z-index:20;background:rgba(242,246,251,0.97);backdrop-filter:blur(16px);border-bottom:1px solid #C8DAEA;padding:0 1.8rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;box-sizing:border-box;">
    <!-- back + title -->
    <div style="display:flex;align-items:center;gap:.8rem;flex-shrink:0;">
      <button onclick="closeDecoOverlay()" style="{HDR_BTN}" onmouseover="this.style.background='rgba(27,58,92,.15)'" onmouseout="this.style.background='rgba(27,58,92,.08)'">←</button>
      <div>
        <div style="font-family:'Noto Serif TC',serif;font-size:.92rem;font-weight:700;color:#0F2744;">裝潢風格方案</div>
        <div style="font-size:.67rem;color:#7A8FA6;letter-spacing:.07em;">6 種精選風格 · 30 天極速完工 · 保固 2 年</div>
      </div>
    </div>
    <!-- dots + counter -->
    <div style="display:flex;align-items:center;gap:.55rem;">
      <button onclick="slideDecoStyle(-1)" style="{HDR_BTN}" onmouseover="this.style.background='rgba(27,58,92,.15)'" onmouseout="this.style.background='rgba(27,58,92,.08)'">‹</button>
      <div id="decoDots" style="display:flex;align-items:center;gap:5px;">
        {dots_init}
      </div>
      <button onclick="slideDecoStyle(1)" style="{HDR_BTN}" onmouseover="this.style.background='rgba(27,58,92,.15)'" onmouseout="this.style.background='rgba(27,58,92,.08)'">›</button>
      <span id="decoCtr" style="font-size:.75rem;color:#7A8FA6;letter-spacing:.07em;min-width:3.2rem;text-align:center;">01 / 06</span>
    </div>
    <!-- CTA -->
    <button onclick="openBookingOverlay()" style="flex-shrink:0;background:linear-gradient(135deg,#1B3A5C,#2E6CA4);color:#fff;border:none;border-radius:8px;padding:.48rem 1.2rem;font-size:.78rem;font-weight:600;cursor:pointer;font-family:inherit;white-space:nowrap;letter-spacing:.03em;">🏠 預約諮詢</button>
  </div>

  <!-- ── Slide Track ── -->
  <div id="decoTrack" style="position:absolute;top:62px;left:0;bottom:0;display:flex;width:600%;transition:transform .48s cubic-bezier(.25,.46,.45,.94);">
{slides_html}
  </div>

  <!-- ── Floating side arrows ── -->
  <button onclick="slideDecoStyle(-1)" style="{SIDE_BTN}left:1rem;" onmouseover="this.style.background='#1B3A5C';this.style.color='#fff';this.style.borderColor='#1B3A5C'" onmouseout="this.style.background='rgba(255,255,255,.85)';this.style.color='#1B3A5C';this.style.borderColor='#C8DAEA'">‹</button>
  <button onclick="slideDecoStyle(1)"  style="{SIDE_BTN}right:1rem;" onmouseover="this.style.background='#1B3A5C';this.style.color='#fff';this.style.borderColor='#1B3A5C'" onmouseout="this.style.background='rgba(255,255,255,.85)';this.style.color='#1B3A5C';this.style.borderColor='#C8DAEA'">›</button>

</div>"""

# Replace the overlay in the file
start_marker = '<!-- ═══ DECORATION STYLES OVERLAY ═══ -->'
end_marker   = '</div>\n\n</body>'
start_pos = html.find(start_marker)
end_pos   = html.find(end_marker)

if start_pos != -1 and end_pos != -1:
    html = html[:start_pos] + NEW_DECO_OVERLAY + '\n\n</body>' + html[end_pos + len(end_marker):]
    print("Deco overlay replaced: OK")
else:
    print(f"MISS — start={start_pos}, end={end_pos}")

with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("fix9 done!")
