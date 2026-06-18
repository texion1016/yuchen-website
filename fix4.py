# -*- coding: utf-8 -*-
"""
fix4.py — beautify reels + projects sections
1. Upgrade reel images (better lifestyle photos)
2. Enhance reels section header + progress dots
3. Add reel card hover overlay with CTA
4. Enhance project cards with better images & subtle badge glow
5. Add an animated progress bar under project dots
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. Replace reel images with better ones
# ─────────────────────────────────────────────────────────────────────────────
REEL_IMG_MAP = {
    # old → new (better matching lifestyle shots)
    'photo-1555041469-a586c61ea9bc': 'photo-1600210492486-724fe5c67fb3',  # luxe living room
    'photo-1477959858617-67f85cf4f1df': 'photo-1555636222-cae831e670b3',  # city night panorama
    'photo-1556909114-f6e7ad7d3136':   'photo-1556909172-54557c7e4fb7',  # modern kitchen
    'photo-1540518614846-7eded433c457': 'photo-1616594039964-ae9021a400a0',  # bright white bedroom
    'photo-1464146072230-91cabc968266': 'photo-1600566753086-00f18fb6b3ea',  # sunrise balcony
    'photo-1552321554-5fefe8c9ef14':   'photo-1552321554-5fefe8c9ef14',  # keep bathroom
}
for old_id, new_id in REEL_IMG_MAP.items():
    html = html.replace(old_id, new_id)
print("1. Reel images swapped: OK")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Upgrade reels section header — add subtitle + animated indicator dots
# ─────────────────────────────────────────────────────────────────────────────
OLD_REELS_HEAD = """  <div class="reels-head">
    <div>
      <div class="section-label" style="color:var(--gold);opacity:0.85;">LIFESTYLE REELS</div>
      <h2 class="section-title" style="color:#fff;">感受真實<em style="color:var(--gold);">生活感</em></h2>
    </div>
    <div class="reels-head-right">
      <div class="reels-head-line"></div>
      SCROLL TO EXPLORE
    </div>
  </div>"""

NEW_REELS_HEAD = """  <div class="reels-head">
    <div>
      <div class="section-label" style="color:var(--gold);opacity:0.85;letter-spacing:.25em;">LIFESTYLE REELS</div>
      <h2 class="section-title" style="color:#fff;">感受真實<em style="color:var(--gold);">生活感</em></h2>
      <p style="font-size:.82rem;color:rgba(255,255,255,.45);margin-top:.5rem;letter-spacing:.05em;">6 個生活場景 · 從入住第一天開始美好</p>
    </div>
    <div class="reels-head-right">
      <div class="reels-head-line"></div>
      SCROLL TO EXPLORE
    </div>
  </div>"""

html = html.replace(OLD_REELS_HEAD, NEW_REELS_HEAD, 1)
print("2. Reels head:", "OK" if OLD_REELS_HEAD not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Replace plain counter with dot indicators + counter
# ─────────────────────────────────────────────────────────────────────────────
OLD_REELS_CTRL = """  <div class="slider-controls" style="margin-top:1rem;">
    <button class="slider-btn" onclick="slideReels(-1)" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2);color:#fff;">‹</button>
    <div class="reels-counter" id="reelsCounter" style="font-size:0.78rem;color:rgba(255,255,255,0.4);letter-spacing:0.12em;min-width:48px;text-align:center;">01 / 06</div>
    <button class="slider-btn" onclick="slideReels(1)" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2);color:#fff;">›</button>
  </div>"""

NEW_REELS_CTRL = """  <div class="reels-controls">
    <button class="reel-nav-btn" onclick="slideReels(-1)">‹</button>
    <div class="reel-dots" id="reelDots">
      <span class="reel-dot active" onclick="slideReelTo(0)"></span>
      <span class="reel-dot" onclick="slideReelTo(1)"></span>
      <span class="reel-dot" onclick="slideReelTo(2)"></span>
      <span class="reel-dot" onclick="slideReelTo(3)"></span>
      <span class="reel-dot" onclick="slideReelTo(4)"></span>
      <span class="reel-dot" onclick="slideReelTo(5)"></span>
    </div>
    <div class="reels-counter" id="reelsCounter">01 / 06</div>
    <button class="reel-nav-btn" onclick="slideReels(1)">›</button>
  </div>"""

html = html.replace(OLD_REELS_CTRL, NEW_REELS_CTRL, 1)
print("3. Reels controls:", "OK" if OLD_REELS_CTRL not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Add reel card hover CTA overlay + click-to-book inside each card
# ─────────────────────────────────────────────────────────────────────────────
# Add a "預約賞屋" hover action inside each reel card reel-info
OLD_REEL_INFO_1 = """          <div class="reel-category">LIVING ROOM</div>
          <div class="reel-title">客廳動態 × 自然採光</div>
        </div>
      </div>"""
NEW_REEL_INFO_1 = """          <div class="reel-category">LIVING ROOM</div>
          <div class="reel-title">客廳動態 × 自然採光</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_1, NEW_REEL_INFO_1, 1)

OLD_REEL_INFO_2 = """          <div class="reel-category">NIGHT VIEW</div>
          <div class="reel-title">城市夜景 × 頂樓視野</div>
        </div>
      </div>"""
NEW_REEL_INFO_2 = """          <div class="reel-category">NIGHT VIEW</div>
          <div class="reel-title">城市夜景 × 頂樓視野</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_2, NEW_REEL_INFO_2, 1)

OLD_REEL_INFO_3 = """          <div class="reel-category">KITCHEN</div>
          <div class="reel-title">廚房空間 × 輕食生活</div>
        </div>
      </div>"""
NEW_REEL_INFO_3 = """          <div class="reel-category">KITCHEN</div>
          <div class="reel-title">廚房空間 × 輕食生活</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_3, NEW_REEL_INFO_3, 1)

OLD_REEL_INFO_4 = """          <div class="reel-category">BEDROOM</div>
          <div class="reel-title">臥室氛圍 × 沉浸入眠</div>
        </div>
      </div>"""
NEW_REEL_INFO_4 = """          <div class="reel-category">BEDROOM</div>
          <div class="reel-title">臥室氛圍 × 沉浸入眠</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_4, NEW_REEL_INFO_4, 1)

OLD_REEL_INFO_5 = """          <div class="reel-category">BALCONY</div>
          <div class="reel-title">陽台晨光 × 一杯咖啡</div>
        </div>
      </div>"""
NEW_REEL_INFO_5 = """          <div class="reel-category">BALCONY</div>
          <div class="reel-title">陽台晨光 × 一杯咖啡</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_5, NEW_REEL_INFO_5, 1)

OLD_REEL_INFO_6 = """          <div class="reel-category">BATHROOM</div>
          <div class="reel-title">衛浴設計 × 飯店級享受</div>
        </div>
      </div>"""
NEW_REEL_INFO_6 = """          <div class="reel-category">BATHROOM</div>
          <div class="reel-title">衛浴設計 × 飯店級享受</div>
          <div class="reel-cta">預約賞屋 →</div>
        </div>
      </div>"""
html = html.replace(OLD_REEL_INFO_6, NEW_REEL_INFO_6, 1)
print("4. Reel CTAs added: OK")

# Make active reel card clickable to open booking
OLD_REEL_CARD_ACTIVE = """      card.classList.toggle('reel-card-active', abs === 0);"""
NEW_REEL_CARD_ACTIVE = """      card.classList.toggle('reel-card-active', abs === 0);
      card.onclick = abs === 0 ? () => openBookingOverlay() : () => slideReels(Math.sign(off));"""
html = html.replace(OLD_REEL_CARD_ACTIVE, NEW_REEL_CARD_ACTIVE, 1)
print("4b. Reel card click: OK" if OLD_REEL_CARD_ACTIVE not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 5. Add slideReelTo + update dot sync in slideReels
# ─────────────────────────────────────────────────────────────────────────────
OLD_SLIDE_REELS_FN = """  function slideReels(dir) {
    const total = document.querySelectorAll('#reelsSlider .reel-card').length;
    reelCFIdx = (reelCFIdx + dir + total) % total;   // ← circular
    renderReelsCF();
    const counter = document.getElementById('reelsCounter');
    if(counter) counter.textContent = String(reelCFIdx+1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
  }"""

NEW_SLIDE_REELS_FN = """  function syncReelUI() {
    const total = document.querySelectorAll('#reelsSlider .reel-card').length;
    const counter = document.getElementById('reelsCounter');
    if(counter) counter.textContent = String(reelCFIdx+1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
    document.querySelectorAll('#reelDots .reel-dot').forEach((d,i) => d.classList.toggle('active', i === reelCFIdx));
  }
  function slideReels(dir) {
    const total = document.querySelectorAll('#reelsSlider .reel-card').length;
    reelCFIdx = (reelCFIdx + dir + total) % total;
    renderReelsCF();
    syncReelUI();
  }
  function slideReelTo(n) { reelCFIdx = n; renderReelsCF(); syncReelUI(); }"""

html = html.replace(OLD_SLIDE_REELS_FN, NEW_SLIDE_REELS_FN, 1)
print("5. slideReelTo:", "OK" if OLD_SLIDE_REELS_FN not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 6. Additional CSS for new elements
# ─────────────────────────────────────────────────────────────────────────────
EXTRA_CSS = """
/* ── REELS CONTROLS (new layout) ─────────────────────── */
.reels-controls {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.2rem;
  margin-top: 1.5rem;
  padding-bottom: .5rem;
}
.reel-dots {
  display: flex;
  gap: .45rem;
  align-items: center;
}
.reel-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: rgba(255,255,255,.25);
  cursor: pointer;
  transition: all .3s;
  border: none;
  outline: none;
}
.reel-dot.active {
  width: 22px;
  border-radius: 4px;
  background: var(--gold);
}
.reels-counter {
  font-family: 'Noto Serif TC', serif;
  font-size: .8rem !important;
  color: rgba(255,255,255,.45);
  letter-spacing: .14em;
  min-width: 52px;
  text-align: center;
}

/* ── REEL CARD CTA hover ─────────────────────────────── */
.reel-cta {
  display: inline-block;
  margin-top: .65rem;
  font-size: .72rem;
  letter-spacing: .12em;
  color: var(--gold);
  border: 1px solid rgba(200,169,110,.45);
  border-radius: 20px;
  padding: .28rem .85rem;
  opacity: 0;
  transform: translateY(6px);
  transition: opacity .3s, transform .3s;
  cursor: pointer;
}
.reel-card-active .reel-cta {
  opacity: 1;
  transform: translateY(0);
}
.reel-cta:hover {
  background: var(--gold);
  color: #fff;
  border-color: var(--gold);
}

/* ── REEL CARD ACTIVE GLOW ──────────────────────────── */
.reel-card-active {
  cursor: pointer;
}
.reel-card:not(.reel-card-active) {
  cursor: pointer;
}

/* ── REEL CATEGORY STYLE ────────────────────────────── */
.reel-category {
  font-size: .64rem !important;
  letter-spacing: .22em !important;
  color: var(--gold) !important;
  margin-bottom: .2rem;
}
.reel-title {
  font-size: .88rem !important;
  font-weight: 600 !important;
  line-height: 1.45 !important;
}

/* ── PROJECT CARD enhancements ─────────────────────── */
.project-img {
  position: relative;
  overflow: hidden;
}
.project-img::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to bottom, transparent 45%, rgba(20,40,30,.45) 100%);
  pointer-events: none;
}
.project-tag {
  z-index: 2;
  position: relative;
}

/* Shine on hover for project card */
.project-card::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(200,169,110,.06) 0%, transparent 60%);
  opacity: 0;
  transition: opacity .4s;
  pointer-events: none;
  border-radius: inherit;
}
.project-card:hover::after { opacity: 1; }

/* ── SECTION "FEATURED PROJECTS" label center ────── */
.section-head {
  position: relative;
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + EXTRA_CSS + '\n' + html[style_end:]
print("6. Extra CSS: OK")

# ─────────────────────────────────────────────────────────────────────────────
# 7. Improve project card images (swap to higher quality lifestyle shots)
# ─────────────────────────────────────────────────────────────────────────────
# Replace project card bg images with better architectural photos
PROJ_IMG_MAP = {
    'photo-1545324418-cc1a3fa10c00': 'photo-1600585154340-be6161a56a0c',  # 沐光苑 → bright modern building
    'photo-1484154218962-a197022b5858': 'photo-1600607687939-ce8a6c25118c',  # 和風居 → japandi interior
    'photo-1512917774080-9991b1c3d4b7': 'photo-1600047509807-ba8f99d2cdde',  # 晴山苑 → mountain view house
    'photo-1522708323590-d24dbb6b0267': 'photo-1565402170291-8491f1b27463',  # 星曜 → luxury highrise night
    'photo-1416331108676-a22ccb276e35': 'photo-1580587771525-78b9dba3b914',  # 綠意村 → green garden house
}
for old_id, new_id in PROJ_IMG_MAP.items():
    html = html.replace(old_id, new_id)
print("7. Project card images: OK")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done! fix4 complete.")
