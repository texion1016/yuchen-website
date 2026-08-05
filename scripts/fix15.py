# -*- coding: utf-8 -*-
"""
fix15.py — 全站設計大升級
1. 移除報備卡
2. Hero 幾何裝飾環
3. 建案卡片 3D 傾斜
4. Section 曲線分隔
5. 玻璃擬態仲介卡
6. 滾動觸發動畫
7. 環境光暈
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. 移除報備卡 ─────────────────────────────────────────────────────────────
import re
html = re.sub(
    r'\s*<!-- 報備卡 signature element -->.*?</div>\s*(?=\s*</div>\s*<div class="hr-seam)',
    '\n  ',
    html, flags=re.DOTALL, count=1
)
print("1. 報備卡移除:", "OK" if 'reg-card-demo' not in html else "MISS")

# ── 2. 主 CSS 升級 ────────────────────────────────────────────────────────────
UPGRADE_CSS = """
/* ══════════════════════════════════════════════
   FIX15 — IMMERSIVE DESIGN UPGRADE
══════════════════════════════════════════════ */

/* ── 全站字體微調 ── */
body { font-family: 'Noto Sans TC','Space Grotesk',sans-serif !important; }

/* ── Hero 幾何裝飾環 ── */
.hr-right { overflow: hidden !important; }
.hr-right::before {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  width: 520px; height: 520px;
  border: 1px solid rgba(193,154,78,0.22);
  border-radius: 50%;
  pointer-events: none;
  z-index: 5;
  animation: ringPulse 8s ease-in-out infinite;
}
.hr-right::after {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%,-50%);
  width: 340px; height: 340px;
  border: 1px solid rgba(193,154,78,0.14);
  border-radius: 50%;
  pointer-events: none;
  z-index: 5;
  animation: ringPulse 8s ease-in-out infinite 1.5s;
}
@keyframes ringPulse {
  0%,100% { opacity:.8; transform:translate(-50%,-50%) scale(1); }
  50%      { opacity:.4; transform:translate(-50%,-50%) scale(1.04); }
}
/* 照片上方漸層 */
.hero-slide::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(135deg, rgba(30,58,95,0.35) 0%, transparent 55%, rgba(15,25,35,0.2) 100%);
  pointer-events: none;
}

/* ── Hero 左側背景裝飾格線 ── */
.hr-left::before {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(193,154,78,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(193,154,78,0.04) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
  z-index: 0;
}

/* ── Hero title 超大化 ── */
.hr-title {
  font-size: clamp(2.8rem, 5vw, 4.8rem) !important;
  line-height: 1.12 !important;
  letter-spacing: -.01em !important;
  font-weight: 800 !important;
}
.hr-title .accent {
  position: relative;
  display: inline-block;
}
.hr-title .accent::after {
  content: '';
  position: absolute;
  left: 0; right: 0;
  bottom: 4px;
  height: 4px;
  background: linear-gradient(90deg, var(--d-gold), rgba(193,154,78,0));
  border-radius: 2px;
  transform: scaleX(0);
  transform-origin: left;
  animation: underlineIn 1s cubic-bezier(.22,1,.36,1) 1.2s forwards;
}
@keyframes underlineIn { to { transform: scaleX(1); } }

/* ── Section 曲線分隔 ── */
#projects { position: relative !important; }
#projects::before {
  content: '';
  position: absolute;
  top: -40px; left: 0; right: 0;
  height: 80px;
  background: var(--d-bg, #F8F7F2);
  clip-path: ellipse(60% 100% at 50% 0%);
  z-index: 1;
}

.mq + #projects::before { display: none; }

#broker { position: relative !important; }
#broker::before {
  content: '';
  position: absolute;
  top: -50px; left: 0; right: 0;
  height: 100px;
  background: var(--d-ink, #0F1923);
  clip-path: ellipse(55% 100% at 50% 0%);
  z-index: 1;
}

/* ── 建案卡片 3D 視差 ── */
.pj-tile {
  transform-style: preserve-3d !important;
  transform: perspective(1000px) rotateX(0) rotateY(0) !important;
  will-change: transform !important;
  cursor: pointer !important;
}
.pj-tile .pj-img {
  transition: transform .6s cubic-bezier(.22,1,.36,1) !important;
}
.pj-tile:hover .pj-img {
  transform: scale(1.06) !important;
}
/* 建案卡片 hover 光澤掃過 */
.pj-tile::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(135deg,
    transparent 30%,
    rgba(255,255,255,0.08) 50%,
    transparent 70%);
  opacity: 0;
  transition: opacity .3s, transform .5s;
  transform: translateX(-100%) skewX(-10deg);
  pointer-events: none;
  z-index: 10;
}
.pj-tile:hover::after {
  opacity: 1;
  transform: translateX(100%) skewX(-10deg);
}
/* 建案卡片底部漸層 */
.pj-shade {
  background: linear-gradient(to top, rgba(10,18,30,0.92) 0%, rgba(10,18,30,0.45) 50%, transparent 100%) !important;
}

/* ── 仲介區玻璃擬態卡片 ── */
.bro-cell {
  background: rgba(255,255,255,0.06) !important;
  backdrop-filter: blur(16px) saturate(1.4) !important;
  -webkit-backdrop-filter: blur(16px) saturate(1.4) !important;
  border: 1px solid rgba(255,255,255,0.12) !important;
  border-radius: 16px !important;
  position: relative !important;
  overflow: hidden !important;
  transition: all .32s cubic-bezier(.22,1,.36,1) !important;
}
.bro-cell::before {
  content: '';
  position: absolute;
  top: -40%; left: -30%;
  width: 120%; height: 120%;
  background: radial-gradient(circle, rgba(193,154,78,0.08) 0%, transparent 65%);
  pointer-events: none;
  transition: opacity .4s;
  opacity: 0;
}
.bro-cell:hover {
  border-color: rgba(193,154,78,0.4) !important;
  transform: translateY(-6px) !important;
  box-shadow: 0 20px 60px rgba(0,0,0,0.3), 0 0 0 1px rgba(193,154,78,0.2) !important;
}
.bro-cell:hover::before { opacity: 1; }
.bro-no {
  font-size: 2.8rem !important;
  font-weight: 900 !important;
  opacity: .18 !important;
  line-height: 1 !important;
  margin-bottom: .4rem !important;
}

/* ── 仲介區背景裝飾 ── */
#broker {
  overflow: hidden !important;
  position: relative !important;
}
#broker > .bro-inner {
  position: relative !important;
  z-index: 2 !important;
}
/* 大圓裝飾 */
.bro-inner::before {
  content: '';
  position: absolute;
  right: -15%; top: -30%;
  width: 500px; height: 500px;
  border: 1px solid rgba(193,154,78,0.1);
  border-radius: 50%;
  pointer-events: none;
}
.bro-inner::after {
  content: '';
  position: absolute;
  right: -5%; top: -15%;
  width: 300px; height: 300px;
  border: 1px solid rgba(193,154,78,0.08);
  border-radius: 50%;
  pointer-events: none;
}

/* ── 滾動觸發動畫系統 ── */
.reveal {
  opacity: 0;
  transform: translateY(32px);
  transition: opacity .7s cubic-bezier(.22,1,.36,1), transform .7s cubic-bezier(.22,1,.36,1);
}
.reveal.visible { opacity: 1 !important; transform: translateY(0) !important; }
.reveal-delay-1 { transition-delay: .12s !important; }
.reveal-delay-2 { transition-delay: .22s !important; }
.reveal-delay-3 { transition-delay: .34s !important; }
.reveal-delay-4 { transition-delay: .46s !important; }

/* ── 環境光暈 ── */
#projects {
  background: var(--d-bg, #F8F7F2) !important;
  position: relative !important;
}
#projects::after {
  content: '';
  position: absolute;
  top: 0; right: -10%;
  width: 55%; height: 70%;
  background: radial-gradient(ellipse, rgba(193,154,78,0.06) 0%, transparent 65%);
  pointer-events: none;
  z-index: 0;
}

#comparison {
  background: #EEF2F7 !important;
  position: relative !important;
  overflow: hidden !important;
}
#comparison::before {
  content: '';
  position: absolute;
  bottom: -20%; left: -15%;
  width: 600px; height: 600px;
  background: radial-gradient(ellipse, rgba(30,58,95,0.05) 0%, transparent 65%);
  pointer-events: none;
}

/* ── Process 時間軸樣式 ── */
.process-step {
  position: relative !important;
  overflow: hidden !important;
}
.process-step::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 3px; height: 0;
  background: linear-gradient(to bottom, var(--d-gold, #C8A96E), transparent);
  transition: height .8s cubic-bezier(.22,1,.36,1);
}
.process-step.visible::before { height: 100%; }

/* ── Line CTA 視覺升級 ── */
#line-cta {
  background: linear-gradient(135deg, #1E3A5F 0%, #2A5080 50%, #1A2F4F 100%) !important;
  position: relative !important;
  overflow: hidden !important;
}
#line-cta::before {
  content: '';
  position: absolute;
  top: -50%; right: -10%;
  width: 500px; height: 500px;
  background: radial-gradient(circle, rgba(193,154,78,0.12) 0%, transparent 60%);
  pointer-events: none;
}
.lcta-title { color: #fff !important; font-size: 1.6rem !important; font-weight: 700 !important; }
.lcta-perk { color: rgba(255,255,255,0.8) !important; }
.lcta-check { background: var(--d-gold, #C8A96E) !important; color: #fff !important; }
.lcta-note { color: rgba(255,255,255,0.5) !important; }
.line-btn {
  background: #fff !important;
  color: #1E3A5F !important;
  font-weight: 700 !important;
}
.line-btn:hover {
  background: var(--d-gold, #C8A96E) !important;
  color: #fff !important;
  transform: translateY(-2px) !important;
}

/* ── Footer 頂部漸層 ── */
footer::before {
  content: '';
  display: block;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--d-gold, #C8A96E), transparent);
  opacity: .4;
}

/* ── 比較區 feature icon ── */
.feature-icon {
  width: 26px !important; height: 26px !important;
  font-weight: 700 !important;
  flex-shrink: 0;
}

/* ── 按鈕全站優化 ── */
.btn {
  position: relative !important;
  overflow: hidden !important;
}
.btn::before {
  content: '';
  position: absolute;
  top: 50%; left: 50%;
  width: 0; height: 0;
  background: rgba(255,255,255,0.15);
  border-radius: 50%;
  transform: translate(-50%,-50%);
  transition: width .5s, height .5s, opacity .5s;
  opacity: 0;
  pointer-events: none;
}
.btn:active::before {
  width: 300px; height: 300px;
  opacity: 0;
  transition: 0s;
}

/* ── Project tag ── */
.pj-tag {
  background: rgba(10,18,30,0.65) !important;
  color: #fff !important;
  border: 1px solid rgba(255,255,255,0.15) !important;
  backdrop-filter: blur(8px) !important;
  border-radius: 6px !important;
  font-size: .65rem !important;
  letter-spacing: .14em !important;
  font-weight: 600 !important;
}
.pj-tag.hot, .pj-tag.new {
  background: rgba(193,154,78,0.85) !important;
  color: #fff !important;
  border-color: rgba(193,154,78,0.5) !important;
}

/* ── 平滑滾動 & 精緻細節 ── */
html { scroll-behavior: smooth !important; }

/* 精選建案 note */
.pj-note {
  color: var(--d-ink-3, #7A96B0) !important;
  font-size: .8rem !important;
  letter-spacing: .06em !important;
}

/* section-head */
.pj-head, .section-head {
  margin-bottom: 2.8rem !important;
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + UPGRADE_CSS + '\n' + html[style_end:]
print("2. Upgrade CSS:", "OK")

# ── 3. 加入 reveal 類別到主要區塊 ────────────────────────────────────────────
# section-head 類別加 reveal
html = html.replace(
    '<div class="pj-head">',
    '<div class="pj-head reveal">',
    1
)
# bro-cell 加 reveal
html = html.replace('<div class="bro-cell">', '<div class="bro-cell reveal">', 1)
html = html.replace(
    '<div class="bro-cell">\n        <span class="bro-no">二</span>',
    '<div class="bro-cell reveal reveal-delay-1">\n        <span class="bro-no">二</span>',
    1
)
html = html.replace(
    '<div class="bro-cell">\n        <span class="bro-no">三</span>',
    '<div class="bro-cell reveal reveal-delay-2">\n        <span class="bro-no">三</span>',
    1
)
html = html.replace(
    '<div class="bro-cell">\n        <span class="bro-no">四</span>',
    '<div class="bro-cell reveal reveal-delay-3">\n        <span class="bro-no">四</span>',
    1
)
print("3. Reveal classes:", "OK")

# ── 4. JS 增強 ────────────────────────────────────────────────────────────────
ENHANCE_JS = """
<script>
// ── 滾動觸發動畫 ────────────────────────────────────────────────────
(function(){
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  // 讓 fade-up 和 reveal 都走新系統
  document.querySelectorAll('.fade-up, .reveal, .process-step').forEach(el => io.observe(el));
})();

// ── 建案卡片 3D 傾斜 ─────────────────────────────────────────────────
document.querySelectorAll('.pj-tile').forEach(card => {
  card.addEventListener('mousemove', function(e) {
    const rect = this.getBoundingClientRect();
    const cx = rect.left + rect.width  / 2;
    const cy = rect.top  + rect.height / 2;
    const dx = (e.clientX - cx) / (rect.width  / 2);
    const dy = (e.clientY - cy) / (rect.height / 2);
    this.style.transform =
      'perspective(900px) rotateY(' + (dx * 7) + 'deg) rotateX(' + (-dy * 5) + 'deg) translateY(-6px) scale(1.01)';
    this.style.boxShadow = '0 20px 60px rgba(15,25,35,0.18), ' +
      (dx * 10) + 'px ' + (dy * 10) + 'px 30px rgba(15,25,35,0.08)';
    this.style.zIndex = '5';
  });
  card.addEventListener('mouseleave', function() {
    this.style.transform = '';
    this.style.boxShadow = '';
    this.style.zIndex   = '';
  });
  card.addEventListener('mouseenter', function() {
    this.style.transition = 'transform .1s, box-shadow .1s';
  });
});

// ── Hero 圖片視差 ─────────────────────────────────────────────────────
(function(){
  const slides = document.querySelectorAll('.hero-slide .hero-bg');
  window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    if (scrolled > window.innerHeight) return;
    slides.forEach(img => {
      img.style.transform = 'translateY(' + (scrolled * 0.28) + 'px)';
    });
  }, { passive: true });
})();

// ── Navbar 顏色平滑過渡 ───────────────────────────────────────────────
(function(){
  const nav = document.getElementById('navbar');
  if (!nav) return;
  window.addEventListener('scroll', function() {
    if (window.scrollY > 60) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  }, { passive: true });
})();

// ── 按鈕 ripple 水波效果 ─────────────────────────────────────────────
document.querySelectorAll('.btn').forEach(btn => {
  btn.addEventListener('click', function(e) {
    const rect = this.getBoundingClientRect();
    const ripple = document.createElement('span');
    ripple.style.cssText =
      'position:absolute;border-radius:50%;background:rgba(255,255,255,0.25);' +
      'pointer-events:none;transform:scale(0);animation:rippleAnim .55s linear;' +
      'width:120px;height:120px;' +
      'left:' + (e.clientX - rect.left - 60) + 'px;' +
      'top:'  + (e.clientY - rect.top  - 60) + 'px;';
    this.appendChild(ripple);
    setTimeout(() => ripple.remove(), 560);
  });
});

// ── 跑馬燈滑鼠暫停 ──────────────────────────────────────────────────
(function(){
  const track = document.querySelector('.mq-track');
  if (!track) return;
  track.parentElement.addEventListener('mouseenter', () => track.style.animationPlayState = 'paused');
  track.parentElement.addEventListener('mouseleave', () => track.style.animationPlayState = '');
})();
</script>

<style>
@keyframes rippleAnim {
  to { transform: scale(4); opacity: 0; }
}
/* fade-up 改成走 reveal 系統 */
.fade-up {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity .7s cubic-bezier(.22,1,.36,1), transform .7s cubic-bezier(.22,1,.36,1);
}
.fade-up.visible { opacity: 1; transform: translateY(0); }
.fade-up-delay-1.visible { transition-delay: .14s; }
.fade-up-delay-2.visible { transition-delay: .26s; }
</style>
"""

html = html.replace('</body>', ENHANCE_JS + '\n</body>', 1)
print("4. JS enhancements:", "OK")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("fix15 done.")
