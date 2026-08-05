# -*- coding: utf-8 -*-
"""
fix3.py — four improvements:
1. Project detail overlay "預約賞屋" → close detail first, then open booking
2. Hero background → better Unsplash images (luxury interior / cityscape night)
3. Projects slider → infinite circular loop
4. Reels slider  → infinite circular loop
5. Beautify both sections (projects + reels)
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. Project detail "預約賞屋" → close overlay first then open booking
# ─────────────────────────────────────────────────────────────────────────────
OLD_PD_BOOKING = """  // Show overlay
  const overlay = document.getElementById('projDetailOverlay');
  overlay.style.display = 'block';
  overlay.scrollTop = 0;
  document.body.style.overflow = 'hidden';"""

NEW_PD_BOOKING = """  // Fill project in booking form
  try {
    const sel = document.getElementById('bkProject');
    if (sel) {
      for (let i = 0; i < sel.options.length; i++) {
        if (sel.options[i].text.includes(name) || name.includes(sel.options[i].text)) {
          sel.value = sel.options[i].value; break;
        }
      }
    }
  } catch(e) {}

  // Show overlay
  const overlay = document.getElementById('projDetailOverlay');
  overlay.style.display = 'block';
  overlay.scrollTop = 0;
  document.body.style.overflow = 'hidden';"""

# Remove the duplicate pre-fill block that was already at the bottom
OLD_DUP_PREFILL = """  // Also pre-fill project in booking overlay
  try {
    const sel = document.getElementById('bkProject');
    if (sel) {
      for (let i = 0; i < sel.options.length; i++) {
        if (sel.options[i].text.includes(name) || name.includes(sel.options[i].text)) {
          sel.value = sel.options[i].value;
          break;
        }
      }
    }
  } catch(e) {}
}"""

NEW_DUP_PREFILL = """}"""

# Wire booking button in project detail to close detail then open booking
OLD_PD_BTN_WIRE = """function openBookingOverlay(){
  document.getElementById('bookingOverlay').classList.add('open');
  document.body.style.overflow='hidden';
  setTimeout(updateClientBkBadge, 100);
  setTimeout(updateOvBookings, 120);
}"""

NEW_PD_BTN_WIRE = """function openBookingOverlay(){
  // Close project detail overlay if open
  const pd = document.getElementById('projDetailOverlay');
  if (pd && pd.style.display !== 'none') pd.style.display = 'none';
  document.getElementById('bookingOverlay').classList.add('open');
  document.body.style.overflow='hidden';
  setTimeout(updateClientBkBadge, 100);
  setTimeout(updateOvBookings, 120);
}"""

html = html.replace(OLD_PD_BOOKING, NEW_PD_BOOKING, 1)
print("1a. PD pre-fill move:", "OK" if OLD_PD_BOOKING not in html else "MISS")

if OLD_DUP_PREFILL in html:
    html = html.replace(OLD_DUP_PREFILL, NEW_DUP_PREFILL, 1)
    print("1b. Dup prefill removed: OK")
else:
    print("1b. Dup prefill: SKIP (not found)")

html = html.replace(OLD_PD_BTN_WIRE, NEW_PD_BTN_WIRE, 1)
print("1c. openBookingOverlay hook:", "OK" if OLD_PD_BTN_WIRE not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 2. Hero background images → better Unsplash photos
# ─────────────────────────────────────────────────────────────────────────────
OLD_HERO_SLIDES = """    <div class="hero-slide slide-1 active">
      <img src="hero.jpg" class="hero-bg" alt="豪華客廳城市景觀">
    </div>
    <div class="hero-slide slide-2">
      <img src="hero.jpg" class="hero-bg" alt="城市夜景" style="object-position:70% center;">
    </div>
    <div class="hero-slide slide-3">
      <img src="hero2.jpg" class="hero-bg" alt="高層景觀">
    </div>"""

# Slide 1: Luxe living room with city view (warm, golden hour)
# Slide 2: High-rise modern apartment interior at dusk
# Slide 3: Aerial city nightscape / luxury tower
NEW_HERO_SLIDES = """    <div class="hero-slide slide-1 active">
      <img src="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=1920&h=1080&fit=crop&auto=format" class="hero-bg" alt="豪華客廳城市景觀">
    </div>
    <div class="hero-slide slide-2">
      <img src="https://images.unsplash.com/photo-1512917774080-9991b1c3d4b7?w=1920&h=1080&fit=crop&auto=format" class="hero-bg" alt="現代豪宅外觀" style="object-position:center 60%;">
    </div>
    <div class="hero-slide slide-3">
      <img src="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1920&h=1080&fit=crop&auto=format" class="hero-bg" alt="夜景城市高樓">
    </div>"""

html = html.replace(OLD_HERO_SLIDES, NEW_HERO_SLIDES, 1)
print("2. Hero images:", "OK" if OLD_HERO_SLIDES not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 3. Projects slider → circular (infinite loop)
# ─────────────────────────────────────────────────────────────────────────────
OLD_SLIDE_PROJECTS = """  function slideProjects(dir) {
    const max = document.querySelectorAll('#projectsSlider .project-card').length - 1;
    projCFIdx = Math.max(0, Math.min(max, projCFIdx + dir));
    renderProjectsCF();
  }
  function goToProject(n) { projCFIdx = n; renderProjectsCF(); }"""

NEW_SLIDE_PROJECTS = """  function slideProjects(dir) {
    const max = document.querySelectorAll('#projectsSlider .project-card').length;
    projCFIdx = (projCFIdx + dir + max) % max;   // ← circular
    renderProjectsCF();
  }
  function goToProject(n) { projCFIdx = n; renderProjectsCF(); }"""

html = html.replace(OLD_SLIDE_PROJECTS, NEW_SLIDE_PROJECTS, 1)
print("3. Projects circular:", "OK" if OLD_SLIDE_PROJECTS not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 4. Reels slider → circular (infinite loop)
# ─────────────────────────────────────────────────────────────────────────────
OLD_SLIDE_REELS = """  function slideReels(dir) {
    const max = document.querySelectorAll('#reelsSlider .reel-card').length - 1;
    reelCFIdx = Math.max(0, Math.min(max, reelCFIdx + dir));
    renderReelsCF();
    const counter = document.getElementById('reelsCounter');
    if(counter) counter.textContent = String(reelCFIdx+1).padStart(2,'0') + ' / ' + String(max+1).padStart(2,'0');
  }"""

NEW_SLIDE_REELS = """  function slideReels(dir) {
    const total = document.querySelectorAll('#reelsSlider .reel-card').length;
    reelCFIdx = (reelCFIdx + dir + total) % total;   // ← circular
    renderReelsCF();
    const counter = document.getElementById('reelsCounter');
    if(counter) counter.textContent = String(reelCFIdx+1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
  }"""

html = html.replace(OLD_SLIDE_REELS, NEW_SLIDE_REELS, 1)
print("4. Reels circular:", "OK" if OLD_SLIDE_REELS not in html else "MISS")

# ─────────────────────────────────────────────────────────────────────────────
# 5. Beautify Projects section
# ─────────────────────────────────────────────────────────────────────────────

# 5a. Add richer project section CSS
PROJ_BEAUTY_CSS = """
/* ── PROJECTS SECTION ENHANCEMENTS ─────────────────────── */
#projects {
  padding: 7rem 0 5rem;
}
.projects-section-head {
  text-align: center;
  margin-bottom: 3.5rem;
  position: relative;
}
.projects-section-head::after {
  content: '';
  display: block;
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  margin: 1rem auto 0;
}

/* Card hover lift */
.project-card {
  transition: transform .35s cubic-bezier(.22,.61,.36,1), box-shadow .35s !important;
  will-change: transform;
}
/* Price styling */
.project-price {
  font-size: 1.5rem !important;
  font-weight: 800 !important;
  font-family: 'Noto Serif TC', serif;
  background: linear-gradient(135deg, var(--gold) 0%, #c8a96e 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: .6rem 0 .2rem !important;
}
.project-price small { -webkit-text-fill-color: var(--gold); font-size:.62em !important; }
.project-price-note { font-size: .73rem !important; color: #999; margin-bottom: .9rem !important; }

/* Slider hint arrows  */
.slider-btn {
  background: rgba(255,255,255,0.92) !important;
  color: var(--green-dark) !important;
  border: 1.5px solid rgba(200,169,110,.3) !important;
  border-radius: 50% !important;
  width: 44px !important;
  height: 44px !important;
  font-size: 1.4rem !important;
  box-shadow: 0 4px 16px rgba(44,74,62,.14) !important;
  transition: all .2s !important;
}
.slider-btn:hover {
  background: var(--gold) !important;
  color: #fff !important;
  border-color: var(--gold) !important;
  transform: scale(1.08) !important;
}

/* Dot progress bar */
.slider-dot {
  width: 8px !important;
  height: 8px !important;
  border-radius: 4px !important;
  transition: all .3s !important;
}
.slider-dot.active {
  width: 28px !important;
  background: var(--gold) !important;
  border-radius: 4px !important;
}

/* Project name serif */
.project-name {
  font-family: 'Noto Serif TC', serif;
  font-size: 1.15rem !important;
  letter-spacing: .04em;
}
.project-location { font-size: .76rem !important; }

/* Shimmer on project tag */
.project-tag {
  font-size: .68rem !important;
  letter-spacing: .12em !important;
}
/* ── REELS SECTION ENHANCEMENTS ─────────────────────────── */
.reels-section-head { text-align: center; margin-bottom: 3rem; }

/* Reel card glow on active */
.reel-card-active .reel-thumb {
  box-shadow: 0 0 0 2px var(--gold), 0 20px 60px rgba(200,169,110,.25) !important;
}

/* Reels counter style */
#reelsCounter {
  font-family: 'Noto Serif TC', serif;
  font-size: .9rem !important;
  letter-spacing: .12em;
  color: rgba(255,255,255,.6);
}

/* Reel nav buttons */
.reel-nav-btn {
  background: rgba(255,255,255,.12) !important;
  border: 1.5px solid rgba(255,255,255,.22) !important;
  border-radius: 50% !important;
  width: 42px !important;
  height: 42px !important;
  font-size: 1.3rem !important;
  color: #fff !important;
  transition: all .25s !important;
  backdrop-filter: blur(4px) !important;
}
.reel-nav-btn:hover {
  background: var(--gold) !important;
  border-color: var(--gold) !important;
  transform: scale(1.1) !important;
}

/* Reels section decorative gradient line */
#reels::before {
  content: '';
  display: block;
  width: 80px;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--gold), transparent);
  margin: 0 auto 2rem;
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + PROJ_BEAUTY_CSS + '\n' + html[style_end:]
print("5. Beauty CSS:", "OK")

# 5b. Add section head markup to projects (centered title with subtitle)
OLD_PROJ_INNER = """  <div class="projects-inner">
    <div class="section-head">"""

NEW_PROJ_INNER = """  <div class="projects-inner">
    <div class="projects-section-head">
      <div class="section-label" style="text-align:center;display:block;margin-bottom:.6rem;">FEATURED PROJECTS</div>
    </div>
    <div class="section-head">"""

if OLD_PROJ_INNER in html:
    html = html.replace(OLD_PROJ_INNER, NEW_PROJ_INNER, 1)
    print("5b. Projects section head: OK")
else:
    print("5b. Projects section head: SKIP")

# ─────────────────────────────────────────────────────────────────────────────
# 6. Add reels nav button classes + section head text
# ─────────────────────────────────────────────────────────────────────────────
# Check what the reel nav buttons look like
OLD_REEL_NAV = """<button class="reel-nav-btn" onclick="slideReels(-1)">"""
NEW_REEL_NAV = """<button class="reel-nav-btn" onclick="slideReels(-1)">"""
# They already use reel-nav-btn class from the CSS above - just verify it's there
count_reel_btn = html.count('reel-nav-btn')
print(f"6. Reel nav btns found: {count_reel_btn}")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done!")
