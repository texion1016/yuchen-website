# -*- coding: utf-8 -*-
"""
fix6.py:
1. Broker section → snowy mountain bg, remove dark inner bg
2. Comparison text → dark blue (visible on light bg)
3. Delete testimonials section + nav refs
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ─────────────────────────────────────────────────────────────────────────────
# 1. BROKER SECTION: mountain bg + light overlay, remove dark inner bg
# ─────────────────────────────────────────────────────────────────────────────

# 1a. Replace #broker CSS background
OLD_BROKER_CSS = """    #broker {
      padding: 6rem 2.5rem;
      background: var(--gold-light);
    }"""

NEW_BROKER_CSS = """    #broker {
      padding: 6rem 2.5rem;
      background:
        linear-gradient(160deg, rgba(242,246,251,0.72) 0%, rgba(220,233,247,0.65) 50%, rgba(242,246,251,0.72) 100%),
        url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&h=1080&fit=crop&auto=format') center/cover fixed no-repeat;
    }"""

html = html.replace(OLD_BROKER_CSS, NEW_BROKER_CSS, 1)
print("1a. Broker bg:", "OK" if OLD_BROKER_CSS not in html else "MISS")

# 1b. Remove the override that adds dark gradient to broker-inner
OLD_BROKER_INNER_OVERRIDE = """/* Broker section dark bg update */
#broker .broker-inner {
  background: linear-gradient(135deg, #0A1E35 0%, #0F2744 60%, #071828 100%) !important;
}"""

NEW_BROKER_INNER_OVERRIDE = """/* Broker section: transparent inner */
#broker .broker-inner {
  background: transparent !important;
}"""

html = html.replace(OLD_BROKER_INNER_OVERRIDE, NEW_BROKER_INNER_OVERRIDE, 1)
print("1b. Broker inner:", "OK" if OLD_BROKER_INNER_OVERRIDE not in html else "MISS")

# 1c. Broker text colours → dark blue (they were white for dark bg)
OLD_BROKER_TITLE_OVERRIDE = """#broker .section-title,"""
# This is in a multi-line block — let's target it differently
# Find the broker section-title gradient and update it to blue-on-light instead
# The section-title gradient for broker is already in the light sections block - check
# Actually broker .section-title IS in the light sections block already, so gradient should show fine

# 1d. Fix broker text paragraph color (was white for dark)
OLD_BROKER_P = """      <p style="color:var(--text-mid);line-height:1.85;font-size:0.95rem;margin:1.2rem 0 0;">
        提供仲介夥伴最完整的即時資訊與服務支援，
        讓每一次帶看都更有效率，撮合更快速。
      </p>"""

NEW_BROKER_P = """      <p style="color:#1B3A5C;line-height:1.85;font-size:0.95rem;margin:1.2rem 0 0;">
        提供仲介夥伴最完整的即時資訊與服務支援，
        讓每一次帶看都更有效率，撮合更快速。
      </p>"""

html = html.replace(OLD_BROKER_P, NEW_BROKER_P, 1)
print("1d. Broker p color:", "OK" if OLD_BROKER_P not in html else "MISS")

# 1e. Broker feature cards — keep white bg (already fine for light background)
# Also ensure btn colors look right on light bg — already using btn-primary (dark blue) which is fine

# ─────────────────────────────────────────────────────────────────────────────
# 2. COMPARISON SECTION: make text dark blue (not white)
# ─────────────────────────────────────────────────────────────────────────────

# 2a. comparison-desc paragraph
OLD_COMP_P = """      <p class="comparison-desc">
        我們深知裝潢是多數購屋者最大的壓力來源。
        譽誠提供多款輕裝修方案，從選材到完工，
        全程協助，讓您拿到鑰匙就能立刻入住。
      </p>"""

NEW_COMP_P = """      <p class="comparison-desc" style="color:#1B3A5C;">
        我們深知裝潢是多數購屋者最大的壓力來源。
        譽誠提供多款輕裝修方案，從選材到完工，
        全程協助，讓您拿到鑰匙就能立刻入住。
      </p>"""

html = html.replace(OLD_COMP_P, NEW_COMP_P, 1)
print("2a. Comp desc:", "OK" if OLD_COMP_P not in html else "MISS")

# 2b. comparison-feature text (the ✓ items)
OLD_COMP_FEATURES = """      <div class="comparison-features">
        <div class="comparison-feature">
          <div class="feature-icon">✓</div>
          多款輕裝修風格自由選擇
        </div>
        <div class="comparison-feature">
          <div class="feature-icon">✓</div>
          專業設計師 1 對 1 規劃
        </div>
        <div class="comparison-feature">
          <div class="feature-icon">✓</div>
          30 天極速施工完成
        </div>
        <div class="comparison-feature">
          <div class="feature-icon">✓</div>
          保固 2 年，安心無憂
        </div>
      </div>"""

NEW_COMP_FEATURES = """      <div class="comparison-features">
        <div class="comparison-feature" style="color:#1B3A5C;">
          <div class="feature-icon">✓</div>
          多款輕裝修風格自由選擇
        </div>
        <div class="comparison-feature" style="color:#1B3A5C;">
          <div class="feature-icon">✓</div>
          專業設計師 1 對 1 規劃
        </div>
        <div class="comparison-feature" style="color:#1B3A5C;">
          <div class="feature-icon">✓</div>
          30 天極速施工完成
        </div>
        <div class="comparison-feature" style="color:#1B3A5C;">
          <div class="feature-icon">✓</div>
          保固 2 年，安心無憂
        </div>
      </div>"""

html = html.replace(OLD_COMP_FEATURES, NEW_COMP_FEATURES, 1)
print("2b. Comp features:", "OK" if OLD_COMP_FEATURES not in html else "MISS")

# 2c. Also update comparison-desc CSS color if it's set to white somewhere
# Check via CSS patch
COMP_COLOR_CSS = """
/* Comparison section text — dark blue */
.comparison-desc { color: #1B3A5C !important; }
.comparison-feature { color: #1B3A5C !important; }
.comparison-text .section-title { color: #0F2744 !important; }
"""
style_end = html.rfind('</style>')
html = html[:style_end] + COMP_COLOR_CSS + '\n' + html[style_end:]
print("2c. Comp CSS:", "OK")

# ─────────────────────────────────────────────────────────────────────────────
# 3. DELETE TESTIMONIALS SECTION
# ─────────────────────────────────────────────────────────────────────────────

# 3a. Remove the entire section
OLD_TESTIMONIALS = """<!-- ━━ TESTIMONIALS ━━ -->
<section id="testimonials">
  <div class="testimonials-inner">
    <div class="testimonials-head fade-up">
      <div class="section-label" style="justify-content:center;display:flex;">TESTIMONIALS</div>
      <h2 class="section-title">客戶真實心聲</h2>
    </div>
    <div class="testimonials-grid">

      <div class="testimonial-card fade-up">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">
          「原本最怕裝潢，一想到要找師傅、盯工地就頭大。
          沒想到選了譽誠的輕裝修方案，從簽約到入住只花了28天，
          現在可以直接入住，真的太方便了！」
        </p>
        <div class="testimonial-author">
          <div class="author-avatar"><div class="author-avatar-bg av-1"></div></div>
          <div>
            <div class="author-name">陳小姐</div>
            <div class="author-detail">桃園 × 首購族 × 譽誠沐光苑</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up fade-up-delay-1">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">
          「我是投資客，最需要的就是資訊透明度。
          譽誠的仲介平台讓我隨時掌握可售戶，
          撞客查詢功能也幫我省了很多麻煩，強力推薦！」
        </p>
        <div class="testimonial-author">
          <div class="author-avatar"><div class="author-avatar-bg av-2"></div></div>
          <div>
            <div class="author-name">王先生</div>
            <div class="author-detail">合作仲介 × 3 年老客戶</div>
          </div>
        </div>
      </div>

      <div class="testimonial-card fade-up fade-up-delay-2">
        <div class="testimonial-stars">★★★★★</div>
        <p class="testimonial-text">
          「帶著孩子看屋真的很累，但業務很有耐心地陪我們跑了四個案場。
          最後選了台中的晴山苑，山景超漂亮，孩子每天早上都好期待！」
        </p>
        <div class="testimonial-author">
          <div class="author-avatar"><div class="author-avatar-bg av-3"></div></div>
          <div>
            <div class="author-name">林太太</div>
            <div class="author-detail">台中 × 換屋族 × 譽誠晴山苑</div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>"""

html = html.replace(OLD_TESTIMONIALS, '', 1)
print("3a. Testimonials removed:", "OK" if OLD_TESTIMONIALS not in html else "MISS")

# 3b. Remove nav links to testimonials
OLD_NAV_TEST_MOBILE = """  <a href="#testimonials" onclick="closeMobileNav()">客戶見證</a>"""
html = html.replace(OLD_NAV_TEST_MOBILE, '', 1)

OLD_NAV_TEST_DESK = """    <a href="#testimonials">客戶見證</a>"""
html = html.replace(OLD_NAV_TEST_DESK, '', 1)

OLD_NAV_TEST_FOOTER = """          <li><a href="#testimonials">客戶見證</a></li>"""
html = html.replace(OLD_NAV_TEST_FOOTER, '', 1)

print("3b. Nav links removed: OK")

# 3c. Remove leftover testimonials CSS refs that cause blank space
TESTI_SPACE_CSS = """
/* Remove testimonials section spacing */
#testimonials { display: none !important; }
"""
style_end = html.rfind('</style>')
html = html[:style_end] + TESTI_SPACE_CSS + '\n' + html[style_end:]
print("3c. Testi hide CSS: OK")

# ─────────────────────────────────────────────────────────────────────────────
# Save
# ─────────────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nAll done! fix6 complete.")
