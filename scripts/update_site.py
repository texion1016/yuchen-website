# -*- coding: utf-8 -*-
"""
Comprehensive site update:
1. Set hero.jpg as the background image
2. Add 3D Coverflow effect to projects section
3. Replace reels video cards with real images + 3D Coverflow
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. Hero: replace placeholder slide gradients with real image ──────────────
OLD_HERO_CSS = """    /* Placeholder hero backgrounds with CSS gradients */
    .slide-1 { background: linear-gradient(135deg, #2C4A3E 0%, #5C8A75 40%, #8BB8A0 100%); }
    .slide-2 { background: linear-gradient(135deg, #1A2E25 0%, #3D6B5C 40%, #6B9E8A 100%); }
    .slide-3 { background: linear-gradient(135deg, #1A1A2E 0%, #2C3E6B 40%, #5C7FB8 100%); }"""

NEW_HERO_CSS = """    /* Hero slides use real photo background */
    .slide-1 .hero-bg, .slide-2 .hero-bg, .slide-3 .hero-bg { display:block; }
    .slide-2::before { background: linear-gradient(135deg, rgba(10,30,50,0.65) 0%, rgba(10,30,50,0.22) 100%); }
    .slide-3::before { background: linear-gradient(135deg, rgba(60,30,10,0.60) 0%, rgba(60,30,10,0.18) 100%); }"""

html = html.replace(OLD_HERO_CSS, NEW_HERO_CSS)

# ── 2. Hero HTML slides: add real image ──────────────────────────────────────
OLD_HERO_SLIDES = """  <div class="hero-slides">
    <div class="hero-slide slide-1 active">
      <div class="comp-visual" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;">
        <div style="text-align:center;opacity:0.12;color:white;">
          <div style="font-size:8rem;">🛋️</div>
        </div>
      </div>
    </div>
    <div class="hero-slide slide-2">
      <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0.1;color:white;font-size:8rem;">🌃</div>
    </div>
    <div class="hero-slide slide-3">
      <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;opacity:0.1;color:white;font-size:8rem;">🏙️</div>
    </div>
  </div>"""

NEW_HERO_SLIDES = """  <div class="hero-slides">
    <div class="hero-slide slide-1 active">
      <img src="hero.jpg" class="hero-bg" alt="豪華客廳城市景觀">
    </div>
    <div class="hero-slide slide-2">
      <img src="hero.jpg" class="hero-bg" alt="城市夜景" style="object-position:70% center;">
    </div>
    <div class="hero-slide slide-3">
      <img src="hero2.jpg" class="hero-bg" alt="高層景觀">
    </div>
  </div>"""

html = html.replace(OLD_HERO_SLIDES, NEW_HERO_SLIDES)

# ── 3. Projects: update CSS for 3D Coverflow ─────────────────────────────────
OLD_PROJ_WRAP_CSS = """    .projects-slider-wrap {
      overflow: hidden;
      padding: 0 2.5rem 1.5rem;
    }
    .projects-slider {
      display: flex;
      gap: 1.5rem;
      transition: transform 0.5s cubic-bezier(0.4,0,0.2,1);
      will-change: transform;
    }"""

NEW_PROJ_WRAP_CSS = """    .projects-slider-wrap {
      overflow: hidden;
      padding: 1rem 0 2rem;
      perspective: 1400px;
      position: relative;
      height: 510px;
    }
    .projects-slider {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      align-items: center;
      transform-style: preserve-3d;
      gap: 0;
    }"""

html = html.replace(OLD_PROJ_WRAP_CSS, NEW_PROJ_WRAP_CSS)

# Update project-card CSS
OLD_PROJ_CARD_CSS = """    .project-card {
      flex: 0 0 300px;
      background: var(--white);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow);
      transition: var(--transition);
      cursor: pointer;
    }
    .project-card:hover { transform: translateY(-6px); box-shadow: var(--shadow-lg); }"""

NEW_PROJ_CARD_CSS = """    .project-card {
      flex: 0 0 300px;
      background: var(--white);
      border-radius: var(--radius);
      overflow: hidden;
      box-shadow: var(--shadow);
      transition: transform 0.55s cubic-bezier(0.25,0.46,0.45,0.94),
                  opacity 0.55s ease, filter 0.55s ease, box-shadow 0.55s ease;
      cursor: pointer;
      transform-origin: center center;
      user-select: none;
    }"""

html = html.replace(OLD_PROJ_CARD_CSS, NEW_PROJ_CARD_CSS)

# Update project image backgrounds with Unsplash URLs
PROJ_IMGS = [
    ('style="height:100%;background:linear-gradient(135deg,#3D6B5C 0%,#8BB8A0 100%);display:flex;align-items:center;justify-content:center;font-size:3.5rem;opacity:0.7;">🏢',
     'style="height:100%;background:url(\'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=600&h=400&fit=crop\') center/cover no-repeat;">'),
    ('style="height:100%;background:linear-gradient(135deg,#1A2E3A 0%,#3D6B8A 100%);display:flex;align-items:center;justify-content:center;font-size:3.5rem;opacity:0.7;">🌆',
     'style="height:100%;background:url(\'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=600&h=400&fit=crop\') center/cover no-repeat;">'),
    ('style="height:100%;background:linear-gradient(135deg,#4A3E2E 0%,#8A7A5C 100%);display:flex;align-items:center;justify-content:center;font-size:3.5rem;opacity:0.7;">🏠',
     'style="height:100%;background:url(\'https://images.unsplash.com/photo-1512917774080-9991b1c3d4b7?w=600&h=400&fit=crop\') center/cover no-repeat;">'),
    ('style="height:100%;background:linear-gradient(135deg,#2A1A3A 0%,#6B5C8A 100%);display:flex;align-items:center;justify-content:center;font-size:3.5rem;opacity:0.7;">🌙',
     'style="height:100%;background:url(\'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=600&h=400&fit=crop\') center/cover no-repeat;">'),
    ('style="height:100%;background:linear-gradient(135deg,#2C4A3E 0%,#6B9E8A 100%);display:flex;align-items:center;justify-content:center;font-size:3.5rem;opacity:0.7;">🌿',
     'style="height:100%;background:url(\'https://images.unsplash.com/photo-1416331108676-a22ccb276e35?w=600&h=400&fit=crop\') center/cover no-repeat;">'),
]
for old, new in PROJ_IMGS:
    html = html.replace(old, new, 1)

# ── 4. Reels: update CSS ─────────────────────────────────────────────────────
OLD_REELS_WRAP_CSS = """    .reels-slider-wrap {
      overflow: hidden;
      padding: 0 2.5rem 1rem;
    }
    .reels-slider {
      display: flex;
      gap: 1.2rem;
      transition: transform 0.5s cubic-bezier(0.4,0,0.2,1);
    }"""

NEW_REELS_WRAP_CSS = """    .reels-slider-wrap {
      overflow: hidden;
      padding: 1rem 0 2rem;
      perspective: 1200px;
      position: relative;
      height: 460px;
    }
    .reels-slider {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      align-items: center;
      transform-style: preserve-3d;
      gap: 0;
    }"""

html = html.replace(OLD_REELS_WRAP_CSS, NEW_REELS_WRAP_CSS)

OLD_REEL_CARD_CSS = """    .reel-card {
      flex: 0 0 240px;
      aspect-ratio: 9/16;
      border-radius: var(--radius);
      overflow: hidden;
      position: relative;
      cursor: pointer;
      box-shadow: var(--shadow);
    }
    .reel-bg {
      position: absolute;
      inset: 0;
      transition: transform 0.5s ease;
    }
    .reel-card:hover .reel-bg { transform: scale(1.05); }
    .reel-bg-1 { background: linear-gradient(160deg, #3D6B5C 0%, #8BB8A0 100%); }
    .reel-bg-2 { background: linear-gradient(160deg, #1A2E3A 0%, #3D6B8A 100%); }
    .reel-bg-3 { background: linear-gradient(160deg, #4A3E2E 0%, #8A7A5C 100%); }
    .reel-bg-4 { background: linear-gradient(160deg, #2A1A3A 0%, #6B5C8A 100%); }"""

NEW_REEL_CARD_CSS = """    .reel-card {
      flex: 0 0 200px;
      height: 356px;
      border-radius: var(--radius);
      overflow: hidden;
      position: relative;
      cursor: pointer;
      box-shadow: var(--shadow);
      transition: transform 0.55s cubic-bezier(0.25,0.46,0.45,0.94),
                  opacity 0.55s ease, filter 0.55s ease, box-shadow 0.55s ease;
      transform-origin: center center;
    }
    .reel-bg-img {
      position: absolute;
      inset: 0;
      width: 100%; height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
    }
    .reel-card-active .reel-bg-img { transform: scale(1.03); }"""

html = html.replace(OLD_REEL_CARD_CSS, NEW_REEL_CARD_CSS)

# Remove reel-play related CSS (we no longer need play buttons for static images)
OLD_REEL_PLAY_CSS = """    .reel-play {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      width: 52px; height: 52px;
      border-radius: 50%;
      background: rgba(255,255,255,0.2);
      border: 2px solid rgba(255,255,255,0.6);
      backdrop-filter: blur(4px);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--white);
      font-size: 1.2rem;
      transition: var(--transition);
    }
    .reel-card:hover .reel-play { background: rgba(200,169,110,0.8); border-color: var(--gold); transform: translate(-50%, -50%) scale(1.1); }"""

html = html.replace(OLD_REEL_PLAY_CSS, """    /* reel-play removed – static image display */""")

# ── 5. Reels HTML: replace gradient bg with Unsplash images ──────────────────
OLD_REELS_HTML = """    <div class="reels-slider" id="reelsSlider">

      <div class="reel-card fade-up">
        <div class="reel-bg reel-bg-1"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🛋️</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">LIVING ROOM</div>
          <div class="reel-title">客廳動態 × 自然採光</div>
        </div>
      </div>

      <div class="reel-card fade-up fade-up-delay-1">
        <div class="reel-bg reel-bg-2"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🌃</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">NIGHT VIEW</div>
          <div class="reel-title">城市夜景 × 頂樓視野</div>
        </div>
      </div>

      <div class="reel-card fade-up fade-up-delay-2">
        <div class="reel-bg reel-bg-3"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🍳</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">KITCHEN</div>
          <div class="reel-title">廚房空間 × 輕食生活</div>
        </div>
      </div>

      <div class="reel-card fade-up fade-up-delay-3">
        <div class="reel-bg reel-bg-4"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🌙</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">BEDROOM</div>
          <div class="reel-title">臥室氛圍 × 沉浸入眠</div>
        </div>
      </div>

      <div class="reel-card">
        <div class="reel-bg" style="background:linear-gradient(160deg,#3A2C1A 0%, #8A6B3E 100%);"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🌅</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">BALCONY</div>
          <div class="reel-title">陽台晨光 × 一杯咖啡</div>
        </div>
      </div>

      <div class="reel-card">
        <div class="reel-bg" style="background:linear-gradient(160deg,#1A3A2C 0%, #3E8A6B 100%);"></div>
        <div class="reel-overlay"></div>
        <div class="reel-icon">🚿</div>
        <div class="reel-play">▶</div>
        <div class="reel-info">
          <div class="reel-category">BATHROOM</div>
          <div class="reel-title">衛浴設計 × 飯店級享受</div>
        </div>
      </div>

    </div>"""

NEW_REELS_HTML = """    <div class="reels-slider" id="reelsSlider">

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400&h=712&fit=crop&auto=format" alt="客廳" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">LIVING ROOM</div>
          <div class="reel-title">客廳動態 × 自然採光</div>
        </div>
      </div>

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=400&h=712&fit=crop&auto=format" alt="城市夜景" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">NIGHT VIEW</div>
          <div class="reel-title">城市夜景 × 頂樓視野</div>
        </div>
      </div>

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?w=400&h=712&fit=crop&auto=format" alt="廚房" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">KITCHEN</div>
          <div class="reel-title">廚房空間 × 輕食生活</div>
        </div>
      </div>

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1540518614846-7eded433c457?w=400&h=712&fit=crop&auto=format" alt="臥室" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">BEDROOM</div>
          <div class="reel-title">臥室氛圍 × 沉浸入眠</div>
        </div>
      </div>

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1464146072230-91cabc968266?w=400&h=712&fit=crop&auto=format" alt="陽台" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">BALCONY</div>
          <div class="reel-title">陽台晨光 × 一杯咖啡</div>
        </div>
      </div>

      <div class="reel-card">
        <img class="reel-bg-img" src="https://images.unsplash.com/photo-1552321554-5fefe8c9ef14?w=400&h=712&fit=crop&auto=format" alt="衛浴" loading="lazy">
        <div class="reel-overlay"></div>
        <div class="reel-info">
          <div class="reel-category">BATHROOM</div>
          <div class="reel-title">衛浴設計 × 飯店級享受</div>
        </div>
      </div>

    </div>"""

html = html.replace(OLD_REELS_HTML, NEW_REELS_HTML)

# ── 6. Replace JavaScript slider functions ────────────────────────────────────
OLD_PROJ_JS = """  /* ── Projects slider ── */
  let projIndex = 0;
  const projSlider = document.getElementById('projectsSlider');
  const projDotEls = document.querySelectorAll('#projDots .slider-dot');
  function getCardWidth() {
    const card = projSlider.querySelector('.project-card');
    return card ? card.offsetWidth + 24 : 324;
  }
  function updateProjSlider() {
    projSlider.style.transform = `translateX(-${projIndex * getCardWidth()}px)`;
    projDotEls.forEach((d, i) => d.classList.toggle('active', i === projIndex));
  }
  function slideProjects(dir) {
    const max = projSlider.querySelectorAll('.project-card').length - 1;
    projIndex = Math.max(0, Math.min(max, projIndex + dir));
    updateProjSlider();
  }
  function goToProject(n) { projIndex = n; updateProjSlider(); }

  /* ── Reels slider ── */
  let reelIndex = 0;
  const reelSlider = document.getElementById('reelsSlider');
  function getReelWidth() {
    const card = reelSlider.querySelector('.reel-card');
    return card ? card.offsetWidth + 19 : 259;
  }
  function slideReels(dir) {
    const max = reelSlider.querySelectorAll('.reel-card').length - 1;
    reelIndex = Math.max(0, Math.min(max, reelIndex + dir));
    reelSlider.style.transform = `translateX(-${reelIndex * getReelWidth()}px)`;
  }"""

NEW_PROJ_JS = """  /* ── 3D Coverflow: Projects ── */
  let projCFIdx = 0;
  function renderProjectsCF() {
    const cards = [...document.querySelectorAll('#projectsSlider .project-card')];
    cards.forEach((card, i) => {
      const off = i - projCFIdx;
      const abs = Math.abs(off), sign = Math.sign(off) || 1;
      if (abs === 0) {
        card.style.cssText += ';transform:translateX(0) translateZ(0) rotateY(0deg) scale(1);opacity:1;z-index:10;filter:none;box-shadow:0 16px 48px rgba(44,74,62,.22)';
      } else if (abs === 1) {
        card.style.cssText += `;transform:translateX(${sign*340}px) translateZ(-90px) rotateY(${-sign*52}deg) scale(0.88);opacity:0.72;z-index:7;filter:brightness(0.75);box-shadow:var(--shadow)`;
      } else if (abs === 2) {
        card.style.cssText += `;transform:translateX(${sign*590}px) translateZ(-170px) rotateY(${-sign*68}deg) scale(0.72);opacity:0.45;z-index:4;filter:brightness(0.6);box-shadow:none`;
      } else {
        card.style.cssText += `;transform:translateX(${sign*780}px) translateZ(-240px) rotateY(${-sign*80}deg) scale(0.55);opacity:0.18;z-index:1;filter:brightness(0.45);box-shadow:none`;
      }
    });
    document.querySelectorAll('#projDots .slider-dot').forEach((d,i)=>d.classList.toggle('active',i===projCFIdx));
  }
  function slideProjects(dir) {
    const max = document.querySelectorAll('#projectsSlider .project-card').length - 1;
    projCFIdx = Math.max(0, Math.min(max, projCFIdx + dir));
    renderProjectsCF();
  }
  function goToProject(n) { projCFIdx = n; renderProjectsCF(); }
  renderProjectsCF();

  /* ── 3D Coverflow: Reels ── */
  let reelCFIdx = 0;
  function renderReelsCF() {
    const cards = [...document.querySelectorAll('#reelsSlider .reel-card')];
    cards.forEach((card, i) => {
      const off = i - reelCFIdx;
      const abs = Math.abs(off), sign = Math.sign(off) || 1;
      card.classList.toggle('reel-card-active', abs === 0);
      if (abs === 0) {
        card.style.cssText += ';transform:translateX(0) translateZ(0) rotateY(0deg) scale(1);opacity:1;z-index:10;filter:none;box-shadow:0 16px 48px rgba(0,0,0,.30)';
      } else if (abs === 1) {
        card.style.cssText += `;transform:translateX(${sign*220}px) translateZ(-70px) rotateY(${-sign*48}deg) scale(0.88);opacity:0.70;z-index:7;filter:brightness(0.72);box-shadow:var(--shadow)`;
      } else if (abs === 2) {
        card.style.cssText += `;transform:translateX(${sign*390}px) translateZ(-140px) rotateY(${-sign*66}deg) scale(0.72);opacity:0.42;z-index:4;filter:brightness(0.58);box-shadow:none`;
      } else {
        card.style.cssText += `;transform:translateX(${sign*520}px) translateZ(-200px) rotateY(${-sign*78}deg) scale(0.55);opacity:0.18;z-index:1;filter:brightness(0.42);box-shadow:none`;
      }
    });
  }
  function slideReels(dir) {
    const max = document.querySelectorAll('#reelsSlider .reel-card').length - 1;
    reelCFIdx = Math.max(0, Math.min(max, reelCFIdx + dir));
    renderReelsCF();
  }
  renderReelsCF();"""

html = html.replace(OLD_PROJ_JS, NEW_PROJ_JS)

# Save
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done! All changes applied.")
