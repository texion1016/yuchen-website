# -*- coding: utf-8 -*-
"""
Fix pass 2:
1. Remove duplicate position:relative from .reel-card (causes drift bug)
2. Make both section backgrounds more visible (reduce overlay opacity)
3. Artistic treatment for all big section titles
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. FIX REEL CARD DRIFT: remove the duplicate position:relative ────────────
OLD_REEL_CARD = """    .reel-card {
      position: absolute;
      left: 50%;
      top: 50%;
      width: 200px;
      height: 356px;
      margin-left: -100px;
      margin-top: -178px;
      border-radius: var(--radius);
      overflow: hidden;
      position: relative;
      cursor: pointer;"""

NEW_REEL_CARD = """    .reel-card {
      position: absolute;
      left: 50%;
      top: 50%;
      width: 200px;
      height: 356px;
      margin-left: -100px;
      margin-top: -178px;
      border-radius: var(--radius);
      overflow: hidden;
      cursor: pointer;"""

html = html.replace(OLD_REEL_CARD, NEW_REEL_CARD)
print("1. Reel card position fix:", "OK" if OLD_REEL_CARD not in html else "MISS")

# ── 2a. PROJECTS: lighter overlay so mountain shows through more ──────────────
OLD_PROJ_BG = """      background:
        linear-gradient(180deg, rgba(242,238,232,0.90) 0%, rgba(234,240,236,0.93) 60%, rgba(242,238,232,0.90) 100%),
        url('https://images.unsplash.com/photo-1501854140801-50d01698950b?w=1920&h=900&fit=crop&auto=format') center/cover no-repeat;"""

NEW_PROJ_BG = """      background:
        linear-gradient(180deg, rgba(242,238,232,0.65) 0%, rgba(234,240,236,0.68) 60%, rgba(242,238,232,0.65) 100%),
        url('https://images.unsplash.com/photo-1501854140801-50d01698950b?w=1920&h=900&fit=crop&auto=format') center/cover no-repeat;"""

html = html.replace(OLD_PROJ_BG, NEW_PROJ_BG)
print("2a. Projects bg opacity:", "OK" if OLD_PROJ_BG not in html else "MISS")

# ── 2b. REELS: lighter dark overlay so mountains show more ───────────────────
OLD_REELS_BG = """      background:
        linear-gradient(160deg, rgba(12,25,20,0.92) 0%, rgba(20,38,30,0.88) 50%, rgba(12,25,20,0.94) 100%),
        url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&h=1080&fit=crop&auto=format') center/cover fixed no-repeat;"""

NEW_REELS_BG = """      background:
        linear-gradient(160deg, rgba(12,25,20,0.76) 0%, rgba(20,38,30,0.68) 50%, rgba(12,25,20,0.80) 100%),
        url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&h=1080&fit=crop&auto=format') center/cover fixed no-repeat;"""

html = html.replace(OLD_REELS_BG, NEW_REELS_BG)
print("2b. Reels bg opacity:", "OK" if OLD_REELS_BG not in html else "MISS")

# ── 3. ARTISTIC SECTION TITLES ────────────────────────────────────────────────
# 3a. Upgrade base .section-title: bigger, letter-spaced, text-shadow
OLD_SECTION_TITLE_CSS = """    .section-title {
      font-family: 'Noto Serif TC', serif;
      font-size: clamp(1.6rem, 3vw, 2.4rem);
      font-weight: 700;
      color: var(--green-dark);
      line-height: 1.35;
    }"""

NEW_SECTION_TITLE_CSS = """    .section-title {
      font-family: 'Noto Serif TC', serif;
      font-size: clamp(1.9rem, 3.5vw, 2.9rem);
      font-weight: 700;
      color: var(--green-dark);
      line-height: 1.25;
      letter-spacing: 0.05em;
      text-shadow: 0 2px 14px rgba(44,74,62,0.13);
    }
    /* Gradient text on light-bg sections */
    #projects .section-title,
    #services .section-title,
    #broker .section-title,
    #flow .section-title,
    #testimonials .section-title,
    #line-cta .section-title {
      background: linear-gradient(135deg, #1a3528 0%, #3d7056 48%, #1e3d2a 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      text-shadow: none;
      filter: drop-shadow(0 3px 8px rgba(44,74,62,0.22));
    }
    /* Glowing white text on dark-bg sections */
    #reels .section-title {
      text-shadow: 0 0 30px rgba(200,169,110,0.30), 0 2px 12px rgba(0,0,0,0.40) !important;
      filter: none;
    }"""

html = html.replace(OLD_SECTION_TITLE_CSS, NEW_SECTION_TITLE_CSS)
print("3a. Section title CSS:", "OK" if OLD_SECTION_TITLE_CSS not in html else "MISS")

# 3b. Enhance .section-label: slightly larger, bolder, gold glow
OLD_SECTION_LABEL_CSS = """    .section-label {
      font-size: 0.72rem;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--gold);
      font-weight: 500;
      margin-bottom: 0.6rem;
    }"""

NEW_SECTION_LABEL_CSS = """    .section-label {
      font-size: 0.72rem;
      letter-spacing: 0.28em;
      text-transform: uppercase;
      color: var(--gold);
      font-weight: 600;
      margin-bottom: 0.7rem;
      opacity: 0.9;
    }"""

html = html.replace(OLD_SECTION_LABEL_CSS, NEW_SECTION_LABEL_CSS)
print("3b. Section label CSS:", "OK" if OLD_SECTION_LABEL_CSS not in html else "MISS")

# 3c. Add decorative quotation marks around hero headline
# Also make the hero h1 bigger and more artistic
OLD_HERO_H1_CSS = """    .hero-title {
      font-family: 'Noto Serif TC', serif;
      font-size: clamp(2.4rem, 6vw, 4.2rem);"""

NEW_HERO_H1_CSS = """    .hero-title {
      font-family: 'Noto Serif TC', serif;
      font-size: clamp(2.6rem, 6.5vw, 4.8rem);"""

if OLD_HERO_H1_CSS in html:
    html = html.replace(OLD_HERO_H1_CSS, NEW_HERO_H1_CSS)
    print("3c. Hero title size: OK")
else:
    print("3c. Hero title size: MISS (skipped)")

# 3d. Add vertical decorative stroke before each section-title
# Insert a ::before pseudo-element for the section-head-text titles
OLD_SECTION_HEAD_TEXT_CSS = """    .section-head-text {
      display: flex;
      flex-direction: column;
    }"""

NEW_SECTION_HEAD_TEXT_CSS = """    .section-head-text {
      display: flex;
      flex-direction: column;
      position: relative;
      padding-left: 1.2rem;
    }
    .section-head-text::before {
      content: '';
      position: absolute;
      left: 0; top: 0; bottom: 0;
      width: 3px;
      background: linear-gradient(180deg, var(--gold) 0%, rgba(200,169,110,0.1) 100%);
      border-radius: 2px;
    }"""

if OLD_SECTION_HEAD_TEXT_CSS in html:
    html = html.replace(OLD_SECTION_HEAD_TEXT_CSS, NEW_SECTION_HEAD_TEXT_CSS)
    print("3d. Section head text: OK")
else:
    print("3d. Section head text: MISS (check existing)")
    # Try alternate
    idx = html.find('.section-head-text {')
    if idx >= 0:
        print("  Found at:", idx, repr(html[idx:idx+100]))

# Save
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done!")
