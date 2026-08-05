# -*- coding: utf-8 -*-
"""
Connect customer booking form → broker dashboard.

Changes:
1. bkSubmit() saves to localStorage['clientBookings']
2. New sidebar item "客戶預約帶看" with badge
3. New panel bop-client-bookings with full list + status management
4. Overview stat "帶看預約" shows combined count
5. Badge auto-updates on every dashboard open
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. UPDATE bkSubmit() to SAVE booking to localStorage ─────────────────────
OLD_BK_SUBMIT = """  // Generate reference number
  const ref = 'BK-' + String(Date.now()).slice(-6);
  document.getElementById('bkRef').textContent = '預約編號：' + ref;
  // Show success
  document.getElementById('bkFormWrap').style.display = 'none';
  document.getElementById('bkSuccess').classList.add('show');"""

NEW_BK_SUBMIT = """  // Generate reference number
  const ref = 'BK-' + String(Date.now()).slice(-6);
  document.getElementById('bkRef').textContent = '預約編號：' + ref;

  // === SAVE to localStorage so broker dashboard can see it ===
  const booking = {
    ref,
    name,
    phone,
    email: document.getElementById('bkEmail').value.trim(),
    project,
    date,
    time: time.value,
    note: document.getElementById('bkNote').value.trim(),
    ts: Date.now(),
    status: 'pending',   // pending | confirmed | cancelled
    read: false
  };
  try {
    const existing = JSON.parse(localStorage.getItem('clientBookings') || '[]');
    existing.unshift(booking);
    localStorage.setItem('clientBookings', JSON.stringify(existing));
  } catch(e) {}

  // Show success
  document.getElementById('bkFormWrap').style.display = 'none';
  document.getElementById('bkSuccess').classList.add('show');"""

html = html.replace(OLD_BK_SUBMIT, NEW_BK_SUBMIT)
print("1. bkSubmit save:", "OK" if OLD_BK_SUBMIT not in html else "MISS")

# ── 2. ADD sidebar nav item "客戶預約帶看" ─────────────────────────────────────
OLD_SIDEBAR_BOOKING = """          <button class="bo-ni" onclick="boSwitch(this,'booking')"><span class="ico">◻</span>帶看登記系統</button>
          <button class="bo-ni" onclick="boSwitch(this,'conflict')"><span class="ico">◎</span>撞客查詢</button>"""

NEW_SIDEBAR_BOOKING = """          <button class="bo-ni" onclick="boSwitch(this,'booking')"><span class="ico">◻</span>帶看登記系統</button>
          <button class="bo-ni" onclick="boSwitch(this,'client-bookings')" id="niClientBk"><span class="ico">🔔</span>客戶預約帶看<span class="bo-nbadge" id="clientBkBadge" style="display:none">0</span></button>
          <button class="bo-ni" onclick="boSwitch(this,'conflict')"><span class="ico">◎</span>撞客查詢</button>"""

html = html.replace(OLD_SIDEBAR_BOOKING, NEW_SIDEBAR_BOOKING)
print("2. Sidebar item:", "OK" if OLD_SIDEBAR_BOOKING not in html else "MISS")

# ── 3. ADD panel HTML right after the BOOKING panel (before <!-- CONFLICT -->) ─
OLD_CONFLICT_COMMENT = """          <!-- CONFLICT -->
          <div class="bo-panel" id="bop-conflict">"""

NEW_CONFLICT_COMMENT = """          <!-- CLIENT BOOKINGS -->
          <div class="bo-panel" id="bop-client-bookings">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.2rem;flex-wrap:wrap;gap:.8rem">
              <div>
                <div style="font-family:'Noto Serif TC',serif;font-size:1rem;font-weight:700;color:#1B3228">客戶預約帶看</div>
                <div style="font-size:.76rem;color:#aaa;margin-top:.2rem">來自網站「預約賞屋」表單的客戶預約記錄</div>
              </div>
              <div style="display:flex;gap:.6rem;align-items:center">
                <select id="cbFilter" onchange="renderClientBookings()" style="font-size:.78rem;border:1.5px solid #e0dbd2;border-radius:8px;padding:.35rem .7rem;color:#444;outline:none">
                  <option value="">全部狀態</option>
                  <option value="pending">待確認</option>
                  <option value="confirmed">已確認</option>
                  <option value="cancelled">已取消</option>
                </select>
                <button class="bb bb-outline bb-sm" onclick="clearAllClientBookings()" style="font-size:.73rem;color:#c06060;border-color:#e0b0b0">清除全部</button>
              </div>
            </div>
            <div id="cbList"></div>
          </div>

          <!-- CONFLICT -->
          <div class="bo-panel" id="bop-conflict">"""

html = html.replace(OLD_CONFLICT_COMMENT, NEW_CONFLICT_COMMENT)
print("3. Panel HTML:", "OK" if OLD_CONFLICT_COMMENT not in html else "MISS")

# ── 4. ADD CSS for the new panel ──────────────────────────────────────────────
CLIENT_BOOKING_CSS = """
/* ── CLIENT BOOKING PANEL ─────────────────────────────── */
.cb-card {
  background: #fff;
  border: 1.5px solid #eceae6;
  border-radius: 14px;
  padding: 1.1rem 1.3rem;
  margin-bottom: .85rem;
  display: grid;
  grid-template-columns: 1fr auto;
  gap: .6rem 1rem;
  transition: border-color .2s, box-shadow .2s;
  position: relative;
}
.cb-card:hover { border-color: rgba(168,136,58,0.35); box-shadow: 0 4px 16px rgba(44,74,62,.07); }
.cb-card.unread::before {
  content: '';
  position: absolute;
  left: -1.5px; top: -1.5px; bottom: -1.5px;
  width: 4px;
  background: var(--gold);
  border-radius: 14px 0 0 14px;
}
.cb-card-main { display: flex; flex-direction: column; gap: .28rem; }
.cb-ref { font-size: .68rem; color: #bbb; letter-spacing: .1em; }
.cb-name { font-weight: 700; color: #1B3228; font-size: .95rem; }
.cb-meta { font-size: .78rem; color: #666; display: flex; flex-wrap: wrap; gap: .3rem 1rem; }
.cb-meta span { display: flex; align-items: center; gap: .25rem; }
.cb-project { font-size: .78rem; color: #3d7056; font-weight: 600; margin-top: .1rem; }
.cb-note { font-size: .76rem; color: #888; font-style: italic; margin-top: .15rem; }
.cb-actions { display: flex; flex-direction: column; gap: .4rem; align-items: flex-end; justify-content: flex-start; padding-top: .1rem; }
.cb-status {
  display: inline-block;
  padding: .22rem .7rem;
  border-radius: 20px;
  font-size: .7rem;
  font-weight: 600;
  letter-spacing: .05em;
  white-space: nowrap;
}
.cb-status.pending  { background: rgba(200,169,110,.15); color: #a8883a; }
.cb-status.confirmed { background: rgba(44,74,62,.12);  color: #2c4a3e; }
.cb-status.cancelled { background: rgba(180,60,60,.10);  color: #b03c3c; }
.cb-action-btns { display: flex; gap: .35rem; flex-wrap: wrap; justify-content: flex-end; }
.cb-btn {
  border: 1.5px solid #e0dbd2;
  background: none;
  border-radius: 8px;
  padding: .25rem .65rem;
  font-size: .72rem;
  cursor: pointer;
  font-family: inherit;
  transition: all .2s;
  color: #555;
}
.cb-btn:hover { background: #f5f3ef; }
.cb-btn.confirm { border-color: #3d7056; color: #3d7056; }
.cb-btn.confirm:hover { background: rgba(61,112,86,.08); }
.cb-btn.cancel { border-color: #c06060; color: #b03c3c; }
.cb-btn.cancel:hover { background: rgba(180,60,60,.07); }
.cb-empty {
  text-align: center;
  padding: 3.5rem 1rem;
  color: #bbb;
}
.cb-empty .cb-empty-icon { font-size: 2.5rem; margin-bottom: .8rem; opacity: .5; }
.cb-empty p { font-size: .82rem; }
"""

# Insert CSS before </style>
style_end = html.rfind('</style>')
html = html[:style_end] + CLIENT_BOOKING_CSS + '\n' + html[style_end:]
print("4. CSS:", "OK")

# ── 5. ADD JS functions ────────────────────────────────────────────────────────
CLIENT_BOOKING_JS = """
/* ===== CLIENT BOOKINGS PANEL ===== */

function getClientBookings() {
  try { return JSON.parse(localStorage.getItem('clientBookings') || '[]'); } catch(e) { return []; }
}
function saveClientBookings(arr) {
  localStorage.setItem('clientBookings', JSON.stringify(arr));
}

function updateClientBkBadge() {
  const bookings = getClientBookings();
  const unread = bookings.filter(b => b.read === false).length;
  const badge = document.getElementById('clientBkBadge');
  if (!badge) return;
  if (unread > 0) {
    badge.textContent = unread;
    badge.style.display = '';
  } else {
    badge.style.display = 'none';
  }
}

function renderClientBookings() {
  const filter = document.getElementById('cbFilter') ? document.getElementById('cbFilter').value : '';
  let bookings = getClientBookings();
  if (filter) bookings = bookings.filter(b => b.status === filter);

  const container = document.getElementById('cbList');
  if (!container) return;

  if (bookings.length === 0) {
    container.innerHTML = `<div class="cb-empty">
      <div class="cb-empty-icon">📋</div>
      <p>${filter ? '該狀態下沒有預約記錄' : '目前還沒有客戶預約，<br/>客戶透過網站填寫預約賞屋後會即時出現在這裡'}</p>
    </div>`;
    return;
  }

  container.innerHTML = bookings.map((b, idx) => {
    const date = b.date ? b.date.replace(/-/g, '/') : '—';
    const tsStr = b.ts ? new Date(b.ts).toLocaleString('zh-TW', {month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit'}) : '';
    const statusLabel = {pending:'待確認', confirmed:'已確認', cancelled:'已取消'}[b.status] || b.status;
    const actionBtns = b.status === 'pending'
      ? `<button class="cb-btn confirm" onclick="cbUpdateStatus(${idx},'confirmed')">✓ 確認</button>
         <button class="cb-btn cancel"  onclick="cbUpdateStatus(${idx},'cancelled')">✕ 取消</button>`
      : `<button class="cb-btn" onclick="cbUpdateStatus(${idx},'pending')">↩ 重設</button>`;

    return `<div class="cb-card ${b.read===false?'unread':''}">
      <div class="cb-card-main">
        <div class="cb-ref">${b.ref || ''} · ${tsStr}</div>
        <div class="cb-name">${b.name}</div>
        <div class="cb-meta">
          <span>📞 ${b.phone}</span>
          ${b.email ? `<span>✉ ${b.email}</span>` : ''}
          <span>📅 ${date}</span>
          <span>🕐 ${b.time || '—'}</span>
        </div>
        <div class="cb-project">◫ ${b.project || '—'}</div>
        ${b.note ? `<div class="cb-note">備註：${b.note}</div>` : ''}
      </div>
      <div class="cb-actions">
        <span class="cb-status ${b.status}">${statusLabel}</span>
        <div class="cb-action-btns">${actionBtns}</div>
      </div>
    </div>`;
  }).join('');
}

function cbUpdateStatus(idx, status) {
  const all = getClientBookings();
  const filter = document.getElementById('cbFilter') ? document.getElementById('cbFilter').value : '';
  // If filtered, need to find the real index
  let target;
  if (filter) {
    const filtered = all.map((b,i)=>({b,i})).filter(({b})=>b.status===filter);
    if (filtered[idx]) { target = filtered[idx].i; }
  } else {
    target = idx;
  }
  if (target === undefined || !all[target]) return;
  all[target].status = status;
  all[target].read = true;
  saveClientBookings(all);
  renderClientBookings();
  updateClientBkBadge();
  // Update overview badge
  updateOvBookings();
}

function clearAllClientBookings() {
  if (!confirm('確定要清除所有客戶預約記錄？')) return;
  localStorage.removeItem('clientBookings');
  renderClientBookings();
  updateClientBkBadge();
  updateOvBookings();
}

function updateOvBookings() {
  const el = document.getElementById('ovBookings');
  if (!el) return;
  const clientBks = getClientBookings().filter(b => b.status !== 'cancelled').length;
  el.textContent = clientBks || '—';
}

// Mark all as read when entering the panel
const _origBoSwitch = typeof boSwitch === 'function' ? boSwitch : null;
"""

# Insert the JS before the closing </script> before </body>
script_end = html.rfind('</script>', 0, html.rfind('</body>'))
html = html[:script_end] + '\n' + CLIENT_BOOKING_JS + '\n' + html[script_end:]
print("5. JS:", "OK")

# ── 6. HOOK boSwitch to trigger renderClientBookings + mark read ──────────────
# Find the boSwitch function and add the hook
OLD_BOSWITCH_HOOK = """function boSwitch(btn,id){"""

NEW_BOSWITCH_HOOK = """function boSwitch(btn,id){
  if(id==='client-bookings'){
    // Mark all as read
    try{
      const bks=JSON.parse(localStorage.getItem('clientBookings')||'[]');
      bks.forEach(b=>b.read=true);
      localStorage.setItem('clientBookings',JSON.stringify(bks));
    }catch(e){}
    setTimeout(renderClientBookings, 0);
    setTimeout(updateClientBkBadge, 50);
  }"""

html = html.replace(OLD_BOSWITCH_HOOK, NEW_BOSWITCH_HOOK, 1)
print("6. boSwitch hook:", "OK" if OLD_BOSWITCH_HOOK not in html else "MISS")

# ── 7. HOOK dashboard open to auto-update badge and stats ─────────────────────
OLD_OPEN_BROKER = """function openBrokerOverlay(){document.getElementById('brokerOverlay').classList.add('open');document.body.style.overflow='hidden';}"""

NEW_OPEN_BROKER = """function openBrokerOverlay(){
  document.getElementById('brokerOverlay').classList.add('open');
  document.body.style.overflow='hidden';
  setTimeout(updateClientBkBadge, 100);
  setTimeout(updateOvBookings, 120);
}"""

html = html.replace(OLD_OPEN_BROKER, NEW_OPEN_BROKER, 1)
print("7. openBrokerOverlay hook:", "OK" if OLD_OPEN_BROKER not in html else "MISS")

# ── Save ──────────────────────────────────────────────────────────────────────
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Client bookings panel connected to broker dashboard.")
