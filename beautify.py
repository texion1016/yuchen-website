# -*- coding: utf-8 -*-
"""
Beautification update:
1. Fix reel icons (centered, large, glass pill style)
2. Add scenic background images to Projects + Reels sections
3. Visual polish: decorative dots, accent lines, dark moody reels bg
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. PROJECTS SECTION: add scenic background + decorative elements ──────────
OLD_PROJ_CSS = """    #projects {
      padding: 6rem 0 4rem;
      background: var(--cream);
    }"""

NEW_PROJ_CSS = """    #projects {
      padding: 6rem 0 5rem;
      background:
        linear-gradient(180deg, rgba(242,238,232,0.90) 0%, rgba(234,240,236,0.93) 60%, rgba(242,238,232,0.90) 100%),
        url('https://images.unsplash.com/photo-1501854140801-50d01698950b?w=1920&h=900&fit=crop&auto=format') center/cover no-repeat;
      position: relative;
      overflow: hidden;
    }
    /* Dot grid top-right */
    #projects::before {
      content: '';
      position: absolute;
      top: 0; right: 0;
      width: 340px; height: 340px;
      background-image: radial-gradient(circle, rgba(44,74,62,0.13) 1.5px, transparent 1.5px);
      background-size: 20px 20px;
      pointer-events: none;
      z-index: 0;
    }
    /* Large watermark text */
    #projects::after {
      content: '精選';
      position: absolute;
      bottom: -1rem; right: 2rem;
      font-size: 9rem;
      font-weight: 900;
      color: rgba(44,74,62,0.045);
      letter-spacing: 0.05em;
      pointer-events: none;
      font-family: 'Noto Serif TC', serif;
      line-height: 1;
      z-index: 0;
    }
    .projects-inner { position: relative; z-index: 1; }"""

html = html.replace(OLD_PROJ_CSS, NEW_PROJ_CSS)

# ── 2. REELS SECTION: dark moody scenic background + new header style ─────────
OLD_REELS_CSS = """    #reels {
      padding: 6rem 0;
      background: var(--cream);
    }
    .reels-head {
      padding: 0 2.5rem;
      margin-bottom: 2.5rem;
    }"""

NEW_REELS_CSS = """    #reels {
      padding: 6rem 0 5rem;
      background:
        linear-gradient(160deg, rgba(12,25,20,0.92) 0%, rgba(20,38,30,0.88) 50%, rgba(12,25,20,0.94) 100%),
        url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&h=1080&fit=crop&auto=format') center/cover fixed no-repeat;
      position: relative;
      overflow: hidden;
    }
    /* Decorative circle bottom-left */
    #reels::before {
      content: '';
      position: absolute;
      bottom: -120px; left: -80px;
      width: 400px; height: 400px;
      border-radius: 50%;
      border: 1px solid rgba(200,169,110,0.12);
      pointer-events: none;
    }
    /* Second decorative circle */
    #reels::after {
      content: '';
      position: absolute;
      bottom: -60px; left: -20px;
      width: 260px; height: 260px;
      border-radius: 50%;
      border: 1px solid rgba(200,169,110,0.18);
      pointer-events: none;
    }
    .reels-head {
      padding: 0 2.5rem;
      margin-bottom: 2.5rem;
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
    }
    .reels-head-right {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: rgba(255,255,255,0.25);
      font-size: 0.72rem;
      letter-spacing: 0.15em;
      padding-bottom: 0.2rem;
    }
    .reels-head-line {
      width: 32px; height: 1px;
      background: var(--gold);
      opacity: 0.5;
    }"""

html = html.replace(OLD_REELS_CSS, NEW_REELS_CSS)

# Update reels section-label and section-title colors for dark background
OLD_REELS_HEAD_HTML = """  <div class="reels-head">
    <div class="section-label">LIFESTYLE REELS</div>
    <h2 class="section-title">感受真實生活感</h2>
  </div>"""

NEW_REELS_HEAD_HTML = """  <div class="reels-head">
    <div>
      <div class="section-label" style="color:var(--gold);opacity:0.85;">LIFESTYLE REELS</div>
      <h2 class="section-title" style="color:#fff;">感受真實<em style="color:var(--gold);">生活感</em></h2>
    </div>
    <div class="reels-head-right">
      <div class="reels-head-line"></div>
      SCROLL TO EXPLORE
    </div>
  </div>"""

html = html.replace(OLD_REELS_HEAD_HTML, NEW_REELS_HEAD_HTML)

# Update slider-controls for reels to light style (dark bg)
OLD_REELS_CTRL = """  <div class="slider-controls">
    <button class="slider-btn" onclick="slideReels(-1)">‹</button>
    <button class="slider-btn" onclick="slideReels(1)">›</button>
  </div>
</section>

<!-- ━━ BROKER SECTION ━━ -->"""

NEW_REELS_CTRL = """  <div class="slider-controls" style="margin-top:1rem;">
    <button class="slider-btn" onclick="slideReels(-1)" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2);color:#fff;">‹</button>
    <div class="reels-counter" id="reelsCounter" style="font-size:0.78rem;color:rgba(255,255,255,0.4);letter-spacing:0.12em;min-width:48px;text-align:center;">01 / 06</div>
    <button class="slider-btn" onclick="slideReels(1)" style="background:rgba(255,255,255,0.08);border-color:rgba(255,255,255,0.2);color:#fff;">›</button>
  </div>
</section>

<!-- ━━ BROKER SECTION ━━ -->"""

html = html.replace(OLD_REELS_CTRL, NEW_REELS_CTRL)

# ── 3. REEL ICONS: fix alignment + size + glass style ─────────────────────────
OLD_REEL_ICON_CSS = """    .reel-icon {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -80%);
      font-size: 3rem;
      opacity: 0.15;
    }"""

NEW_REEL_ICON_CSS = """    .reel-icon {
      position: absolute;
      top: 38%;
      left: 50%;
      transform: translate(-50%, -50%);
      font-size: 2.2rem;
      width: 64px;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(255,255,255,0.14);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1.5px solid rgba(255,255,255,0.28);
      border-radius: 50%;
      z-index: 2;
      transition: transform 0.4s ease, background 0.4s ease;
    }
    .reel-card-active .reel-icon {
      background: rgba(200,169,110,0.25);
      border-color: var(--gold);
      transform: translate(-50%, -50%) scale(1.08);
    }"""

html = html.replace(OLD_REEL_ICON_CSS, NEW_REEL_ICON_CSS)

# ── 4. Add icons back to each reel card HTML ──────────────────────────────────
icons = ['🛋️', '🌃', '🍳', '🌙', '🌅', '🚿']
categories = ['LIVING ROOM', 'NIGHT VIEW', 'KITCHEN', 'BEDROOM', 'BALCONY', 'BATHROOM']

for icon in icons:
    # Add icon div after reel-overlay (before reel-info)
    old = f"""        <div class="reel-overlay"></div>
        <div class="reel-info">"""
    new = f"""        <div class="reel-overlay"></div>
        <div class="reel-icon">{icon}</div>
        <div class="reel-info">"""
    # Only replace first occurrence matching this icon's card
    html = html.replace(old, new, 1)

# ── 5. Add projects-inner wrapper to HTML ────────────────────────────────────
OLD_PROJ_HTML_SECTION = """<section id="projects">
  <div class="section-head">"""

NEW_PROJ_HTML_SECTION = """<section id="projects">
  <div class="projects-inner">
  <div class="section-head">"""

html = html.replace(OLD_PROJ_HTML_SECTION, NEW_PROJ_HTML_SECTION)

# Close the projects-inner div before end of section
OLD_PROJ_END = """  <div class="slider-controls">
    <button class="slider-btn" id="projPrev" onclick="slideProjects(-1)">‹</button>
    <div class="slider-progress" id="projDots">
      <div class="slider-dot active" onclick="goToProject(0)"></div>
      <div class="slider-dot" onclick="goToProject(1)"></div>
      <div class="slider-dot" onclick="goToProject(2)"></div>
      <div class="slider-dot" onclick="goToProject(3)"></div>
      <div class="slider-dot" onclick="goToProject(4)"></div>
    </div>
    <button class="slider-btn" id="projNext" onclick="slideProjects(1)">›</button>
  </div>
</section>"""

NEW_PROJ_END = """  <div class="slider-controls">
    <button class="slider-btn" id="projPrev" onclick="slideProjects(-1)">‹</button>
    <div class="slider-progress" id="projDots">
      <div class="slider-dot active" onclick="goToProject(0)"></div>
      <div class="slider-dot" onclick="goToProject(1)"></div>
      <div class="slider-dot" onclick="goToProject(2)"></div>
      <div class="slider-dot" onclick="goToProject(3)"></div>
      <div class="slider-dot" onclick="goToProject(4)"></div>
    </div>
    <button class="slider-btn" id="projNext" onclick="slideProjects(1)">›</button>
  </div>
  </div><!-- /projects-inner -->
</section>"""

html = html.replace(OLD_PROJ_END, NEW_PROJ_END)

# ── 6. Update section-head for projects: add decorative underline accent ──────
OLD_PROJ_HEAD_HTML = """  <div class="section-head">
    <div class="section-head-text">
      <div class="section-label">FEATURED PROJECTS</div>
      <h2 class="section-title">精選建案</h2>
    </div>
    <a href="#" class="view-all">查看全部建案 →</a>
  </div>"""

NEW_PROJ_HEAD_HTML = """  <div class="section-head">
    <div class="section-head-text">
      <div class="section-label">FEATURED PROJECTS</div>
      <h2 class="section-title">精選建案</h2>
      <div style="width:40px;height:3px;background:linear-gradient(90deg,var(--gold),transparent);margin-top:0.6rem;border-radius:2px;"></div>
    </div>
    <div style="text-align:right;">
      <a href="#" class="view-all">查看全部建案 →</a>
      <div style="font-size:0.7rem;color:var(--text-light);letter-spacing:0.1em;margin-top:0.4rem;">5 個精選案場</div>
    </div>
  </div>"""

html = html.replace(OLD_PROJ_HEAD_HTML, NEW_PROJ_HEAD_HTML)

# ── 7. Update reels JS to update counter ──────────────────────────────────────
OLD_REEL_JS = """  function slideReels(dir) {
    const max = document.querySelectorAll('#reelsSlider .reel-card').length - 1;
    reelCFIdx = Math.max(0, Math.min(max, reelCFIdx + dir));
    renderReelsCF();
  }
  renderReelsCF();"""

NEW_REEL_JS = """  function slideReels(dir) {
    const max = document.querySelectorAll('#reelsSlider .reel-card').length - 1;
    reelCFIdx = Math.max(0, Math.min(max, reelCFIdx + dir));
    renderReelsCF();
    const counter = document.getElementById('reelsCounter');
    if(counter) counter.textContent = String(reelCFIdx+1).padStart(2,'0') + ' / ' + String(max+1).padStart(2,'0');
  }
  renderReelsCF();"""

html = html.replace(OLD_REEL_JS, NEW_REEL_JS)

# Save
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Beautification done!")
