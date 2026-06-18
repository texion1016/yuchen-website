# -*- coding: utf-8 -*-
import re

content = open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8').read()
lines = content.split('\n')

before = '\n'.join(lines[:1900])
after  = '\n'.join(lines[2775:])

new_broker = r'''
<!-- ══════════════════════════════════════════════
     仲介專區 OVERLAY - REDESIGNED
══════════════════════════════════════════════ -->
<style>
/* === BASE === */
#brokerOverlay{position:fixed;inset:0;z-index:2000;display:none;background:#EEECE8;}
#brokerOverlay.open{display:flex;flex-direction:column;animation:boIn .3s ease;}
@keyframes boIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}

/* LOGIN */
#boLogin{flex:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,#0A130E 0%,#1B3228 60%,#0A130E 100%);padding:2rem;position:relative;}
.bo-login-box{background:#fff;width:100%;max-width:400px;padding:2.8rem 2.5rem;border-top:3px solid #A8883A;}
.bo-login-brand{font-family:'Noto Serif TC',serif;font-size:1.3rem;font-weight:700;color:#1B3228;letter-spacing:.06em;text-align:center;margin-bottom:.2rem}
.bo-login-sub{font-size:.7rem;color:#aaa;text-align:center;letter-spacing:.15em;text-transform:uppercase;margin-bottom:2rem}
.bo-login-err{display:none;padding:.5rem .9rem;background:#FEF2F2;border-left:3px solid #DC2626;font-size:.78rem;color:#DC2626;margin-bottom:1rem}
.bo-fg{display:flex;flex-direction:column;gap:.3rem;margin-bottom:.9rem}
.bo-fg label{font-size:.7rem;font-weight:700;color:#666;letter-spacing:.08em;text-transform:uppercase}
.bo-fg input{padding:.65rem .9rem;border:1px solid #D8D4CC;font-size:.88rem;color:#111;outline:none;transition:.2s;font-family:'Noto Sans TC',sans-serif}
.bo-fg input:focus{border-color:#1B3228;box-shadow:0 0 0 3px rgba(27,50,40,.08)}
.bo-login-btn{width:100%;padding:.82rem;background:#1B3228;color:#fff;border:none;font-size:.9rem;font-weight:600;letter-spacing:.1em;cursor:pointer;transition:.2s;margin-top:.4rem}
.bo-login-btn:hover{background:#2C5245}
.bo-demo{margin-top:1.4rem;padding:.9rem;background:#F5F3EF;border-left:3px solid #A8883A;font-size:.76rem;color:#666;line-height:1.8}
.bo-demo strong{color:#1B3228}
.bo-back{position:absolute;top:1.4rem;left:1.8rem;display:flex;align-items:center;gap:.4rem;color:rgba(255,255,255,.45);font-size:.78rem;cursor:pointer;border:none;background:none;letter-spacing:.04em;transition:.2s}
.bo-back:hover{color:#fff}

/* DASHBOARD */
#boDash{display:none;flex:1;min-height:0;}
.bo-wrap{display:flex;width:100%;height:100%;overflow:hidden;}

/* SIDEBAR */
.bo-sb{width:220px;flex-shrink:0;background:#0A130E;display:flex;flex-direction:column;overflow-y:auto;}
.bo-sb-top{padding:1.2rem 1rem;border-bottom:1px solid rgba(255,255,255,.06)}
.bo-sb-brand{font-family:'Noto Serif TC',serif;font-size:.98rem;font-weight:700;color:#fff;letter-spacing:.05em;margin-bottom:.15rem}
.bo-sb-label{font-size:.6rem;color:rgba(255,255,255,.28);letter-spacing:.14em;text-transform:uppercase}
.bo-sb-user{padding:.85rem 1rem;border-bottom:1px solid rgba(255,255,255,.06);display:flex;align-items:center;gap:.6rem}
.bo-sb-av{width:32px;height:32px;background:#A8883A;display:flex;align-items:center;justify-content:center;font-size:.78rem;font-weight:700;color:#fff;flex-shrink:0}
.bo-sb-name{font-size:.78rem;color:#fff;font-weight:500}
.bo-sb-role{font-size:.63rem;color:rgba(255,255,255,.36);margin-top:.1rem}
.bo-sb-nav{flex:1;padding:.5rem 0}
.bo-sb-sec{font-size:.58rem;letter-spacing:.18em;color:rgba(255,255,255,.22);padding:.7rem 1rem .2rem;text-transform:uppercase}
.bo-ni{display:flex;align-items:center;gap:.6rem;padding:.6rem 1rem;font-size:.79rem;color:rgba(255,255,255,.52);cursor:pointer;transition:.2s;position:relative;border:none;background:none;width:100%;text-align:left}
.bo-ni:hover{background:rgba(255,255,255,.05);color:rgba(255,255,255,.85)}
.bo-ni.active{background:rgba(168,136,58,.13);color:#A8883A}
.bo-ni.active::before{content:'';position:absolute;left:0;top:15%;bottom:15%;width:2px;background:#A8883A}
.bo-ni .ico{font-size:.85rem;width:16px;text-align:center;opacity:.7}
.bo-nbadge{margin-left:auto;background:#DC2626;color:#fff;font-size:.58rem;padding:.08rem .4rem;min-width:18px;text-align:center}
.bo-sb-foot{padding:.9rem 1rem;border-top:1px solid rgba(255,255,255,.06)}
.bo-logout-btn{display:flex;align-items:center;gap:.5rem;font-size:.75rem;color:rgba(255,255,255,.32);cursor:pointer;border:none;background:none;transition:.2s;letter-spacing:.04em}
.bo-logout-btn:hover{color:#fff}

/* MAIN */
.bo-main{flex:1;display:flex;flex-direction:column;min-width:0;background:#EEECE8;}
.bo-topbar{background:#fff;border-bottom:1px solid #DDD9D3;padding:.85rem 2rem;display:flex;align-items:center;justify-content:space-between;flex-shrink:0;}
.bo-tb-title{font-family:'Noto Serif TC',serif;font-size:.98rem;font-weight:700;color:#1B3228;letter-spacing:.04em}
.bo-tb-right{display:flex;align-items:center;gap:.8rem}
.bo-date{font-size:.72rem;color:#aaa;letter-spacing:.03em}
.bo-close{padding:.42rem 1.1rem;background:transparent;border:1px solid #C5BFB5;color:#666;font-size:.75rem;font-weight:600;letter-spacing:.06em;cursor:pointer;transition:.2s}
.bo-close:hover{background:#1B3228;color:#fff;border-color:#1B3228}
.bo-content{flex:1;overflow-y:auto;padding:1.8rem 2rem;}

/* PANELS */
.bo-panel{display:none;width:100%}
.bo-panel.active{display:block}

/* CARD */
.boc{background:#fff;border:1px solid #DDD9D3;padding:1.6rem;margin-bottom:1.2rem;}
.boc-title{font-family:'Noto Serif TC',serif;font-size:.95rem;font-weight:700;color:#1B3228;letter-spacing:.03em;margin-bottom:1.2rem}

/* STAT GRID */
.bo-stat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:#DDD9D3;margin-bottom:1.4rem;}
.bo-stat{background:#fff;padding:1.4rem 1.8rem;}
.bo-stat-num{font-family:'Noto Serif TC',serif;font-size:2.2rem;font-weight:700;color:#1B3228;line-height:1}
.bo-stat-lbl{font-size:.67rem;color:#aaa;letter-spacing:.1em;text-transform:uppercase;margin-top:.35rem}

/* TABLE */
.bo-table-wrap{overflow-x:auto;border:1px solid #DDD9D3;}
table.bt2{width:100%;border-collapse:collapse;font-size:.82rem;}
table.bt2 thead tr{background:#1B3228;}
table.bt2 thead th{padding:.75rem 1rem;text-align:left;font-size:.66rem;font-weight:700;color:rgba(255,255,255,.75);letter-spacing:.12em;text-transform:uppercase;white-space:nowrap}
table.bt2 tbody tr{border-bottom:1px solid #ECEAE6;transition:.15s}
table.bt2 tbody tr:last-child{border:none}
table.bt2 tbody tr:hover{background:#F7F5F1}
table.bt2 tbody td{padding:.72rem 1rem;color:#555;white-space:nowrap}
.td-name{font-weight:600;color:#1A1A1A}

/* TAGS */
.bt{display:inline-block;padding:.16rem .52rem;font-size:.67rem;font-weight:700;letter-spacing:.04em}
.bt-g{background:#ECFDF5;color:#065F46;border:1px solid #A7F3D0}
.bt-o{background:#FFFBEB;color:#92400E;border:1px solid #FDE68A}
.bt-r{background:#FEF2F2;color:#991B1B;border:1px solid #FECACA}
.bt-b{background:#EFF6FF;color:#1E40AF;border:1px solid #BFDBFE}

/* BUTTONS */
.bb{display:inline-flex;align-items:center;gap:.35rem;padding:.46rem 1.1rem;font-size:.77rem;font-weight:700;letter-spacing:.04em;cursor:pointer;border:1px solid transparent;transition:.2s;white-space:nowrap;background:none}
.bb-primary{background:#1B3228;color:#fff;border-color:#1B3228}
.bb-primary:hover{background:#2C5245;border-color:#2C5245}
.bb-outline{color:#1B3228;border-color:#C5BFB5}
.bb-outline:hover{background:#1B3228;color:#fff;border-color:#1B3228}
.bb-gold{background:#A8883A;color:#fff;border-color:#A8883A}
.bb-gold:hover{background:#8A6E28;border-color:#8A6E28}
.bb-danger{background:#DC2626;color:#fff;border-color:#DC2626}
.bb-danger:hover{background:#B91C1C}
.bb-sm{padding:.3rem .78rem;font-size:.71rem}

/* FILTER BAR */
.bo-fbar{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap;margin-bottom:1.2rem}
.bo-fbar input,.bo-fbar select{padding:.44rem .8rem;border:1px solid #D3CFC9;font-size:.79rem;color:#333;outline:none;transition:.2s;background:#fff;font-family:'Noto Sans TC',sans-serif}
.bo-fbar input:focus,.bo-fbar select:focus{border-color:#1B3228}
.bo-fbar input{min-width:220px}

/* PROJECT TABS */
.bo-proj-tabs{display:flex;gap:0;border-bottom:1px solid #DDD9D3;margin-bottom:1.4rem}
.bo-ptab{padding:.55rem 1.2rem;font-size:.77rem;font-weight:500;cursor:pointer;color:#999;border-bottom:2px solid transparent;transition:.2s;white-space:nowrap;letter-spacing:.02em;background:none;border-top:none;border-left:none;border-right:none}
.bo-ptab:hover{color:#1B3228}
.bo-ptab.active{color:#1B3228;border-bottom-color:#A8883A;font-weight:700}

/* FORM */
.bo-fgrid2{display:grid;grid-template-columns:1fr 1fr;gap:0 1.2rem}
.bo-fgrid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0 1rem}
.bo-fg2{display:flex;flex-direction:column;gap:.3rem;margin-bottom:.9rem}
.bo-fg2 label{font-size:.67rem;font-weight:700;color:#777;letter-spacing:.08em;text-transform:uppercase}
.bo-fg2 input,.bo-fg2 select,.bo-fg2 textarea{padding:.6rem .85rem;border:1px solid #D3CFC9;font-size:.84rem;color:#111;outline:none;transition:.2s;background:#fff;font-family:'Noto Sans TC',sans-serif}
.bo-fg2 input:focus,.bo-fg2 select:focus,.bo-fg2 textarea:focus{border-color:#1B3228}

/* MODAL */
.bo-modal-bg{display:none;position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:3000;align-items:center;justify-content:center;padding:2rem}
.bo-modal-bg.open{display:flex}
.bo-modal{background:#fff;width:100%;max-width:640px;max-height:90vh;overflow-y:auto;border-top:3px solid #A8883A;}
.bo-modal-hdr{padding:1.2rem 1.5rem;border-bottom:1px solid #DDD9D3;display:flex;align-items:center;justify-content:space-between}
.bo-modal-title{font-family:'Noto Serif TC',serif;font-size:.98rem;font-weight:700;color:#1B3228}
.bo-modal-close{background:none;border:none;font-size:1.2rem;cursor:pointer;color:#aaa;padding:.2rem .4rem;line-height:1}
.bo-modal-close:hover{color:#1B3228}
.bo-modal-body{padding:1.5rem}
.bo-modal-foot{padding:1rem 1.5rem;border-top:1px solid #DDD9D3;display:flex;gap:.7rem;justify-content:flex-end}

/* BOOKING */
.bo-book-grid{display:grid;grid-template-columns:420px 1fr;gap:1.5rem;align-items:start}
.bo-mini-cal{background:#F5F3EF;border:1px solid #DDD9D3;padding:1rem;margin-bottom:1.2rem}
.bo-cal-hdr{display:flex;justify-content:space-between;align-items:center;margin-bottom:.8rem}
.bo-cal-hdr span{font-size:.84rem;font-weight:700;color:#1B3228;letter-spacing:.03em}
.bo-cal-nav{background:none;border:1px solid #D3CFC9;cursor:pointer;color:#555;font-size:.9rem;padding:.2rem .5rem;transition:.2s}
.bo-cal-nav:hover{background:#1B3228;color:#fff;border-color:#1B3228}
.bo-cal-grid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;text-align:center}
.bo-cal-dl{font-size:.63rem;color:#bbb;padding:.2rem 0;letter-spacing:.04em}
.bo-cal-d{font-size:.73rem;padding:.3rem .1rem;cursor:pointer;color:#666;transition:.15s}
.bo-cal-d:hover{background:#1B3228;color:#fff}
.bo-cal-d.today{background:#A8883A;color:#fff;font-weight:700}
.bo-cal-d.has-b::after{content:'';display:block;width:4px;height:4px;border-radius:50%;background:#DC2626;margin:.1rem auto 0}
.bo-cal-d.empty{pointer-events:none;opacity:0}
.bo-brec{display:flex;gap:.8rem;padding:.8rem 0;border-bottom:1px solid #ECEAE6}
.bo-brec:last-child{border:none}
.bo-brec-date{flex-shrink:0;width:40px;text-align:center;background:#F5F3EF;border-left:2px solid #A8883A;padding:.3rem .2rem}
.bo-brec-d{font-size:1rem;font-weight:700;color:#1B3228;line-height:1}
.bo-brec-m{font-size:.6rem;color:#aaa}
.bo-brec-info{flex:1}
.bo-brec-proj{font-size:.83rem;font-weight:700;color:#1A1A1A}
.bo-brec-meta{font-size:.72rem;color:#999;line-height:1.65;margin-top:.15rem}

/* CONFLICT */
.bo-cf-result{padding:1.4rem;border:1px solid #DDD9D3;display:none;margin-top:1.2rem}
.bo-cf-result.safe{border-color:#059669;background:#F0FDF4}
.bo-cf-result.danger{border-color:#DC2626;background:#FEF2F2}

/* MATERIALS */
.bo-mat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(155px,1fr));gap:.9rem}
.bo-mat-item{background:#fff;border:1px solid #DDD9D3;cursor:pointer;transition:.2s}
.bo-mat-item:hover{border-color:#1B3228;transform:translateY(-2px);}
.bo-mat-thumb{height:88px;display:flex;align-items:center;justify-content:center;font-size:1.8rem;background:#F5F3EF;border-bottom:1px solid #DDD9D3;color:#555}
.bo-mat-info{padding:.7rem .85rem}
.bo-mat-name{font-size:.76rem;font-weight:600;color:#1A1A1A;margin-bottom:.2rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bo-mat-size{font-size:.67rem;color:#bbb;margin-bottom:.45rem}
.bo-mat-dl{font-size:.7rem;color:#A8883A;font-weight:700;letter-spacing:.04em}

/* NEWS */
.bo-news-item{background:#fff;border:1px solid #DDD9D3;padding:1.1rem 1.5rem;margin-bottom:.8rem;display:flex;gap:1.1rem;cursor:pointer;transition:.2s}
.bo-news-item:hover{border-left-color:#A8883A;border-left-width:3px}
.bo-news-date{flex-shrink:0;width:44px;text-align:center;border-right:1px solid #ECEAE6;padding-right:1rem}
.bnd-d{font-size:1.1rem;font-weight:700;color:#1B3228;line-height:1}
.bnd-m{font-size:.62rem;color:#bbb}
.bo-news-body{flex:1}
.bo-news-title{font-size:.86rem;font-weight:700;color:#1A1A1A;margin-bottom:.3rem}
.bo-news-exc{font-size:.77rem;color:#888;line-height:1.65}
.bo-news-tags{display:flex;gap:.35rem;margin-top:.45rem;flex-wrap:wrap}

/* COMMISSION */
.bo-comm-banner{background:#1B3228;padding:1.4rem 2rem;display:flex;align-items:center;justify-content:space-between;margin-bottom:1.4rem;color:#fff;border-left:4px solid #A8883A;flex-wrap:wrap;gap:1rem}

/* CONTACT */
.bo-ct-grid{display:grid;grid-template-columns:1fr 1.5fr;gap:1.5rem}
.bo-ct-person{display:flex;align-items:center;gap:.9rem;padding-bottom:.9rem;margin-bottom:.9rem;border-bottom:1px solid #ECEAE6}
.bo-ct-av{width:46px;height:46px;background:#1B3228;display:flex;align-items:center;justify-content:center;font-size:1rem;color:#fff;flex-shrink:0}
.bo-ct-name{font-weight:700;font-size:.88rem;color:#1A1A1A}
.bo-ct-role{font-size:.71rem;color:#aaa;margin-top:.15rem}
.bo-ct-item{display:flex;align-items:flex-start;gap:.7rem;margin-bottom:.85rem;font-size:.81rem;color:#444}
.bo-ct-ico{width:28px;height:28px;background:#F5F3EF;border:1px solid #DDD9D3;display:flex;align-items:center;justify-content:center;font-size:.8rem;flex-shrink:0}

/* TOAST */
.bo-toast{position:fixed;bottom:2rem;right:2rem;z-index:4000;background:#1B3228;color:#fff;padding:.75rem 1.4rem;font-size:.82rem;letter-spacing:.03em;box-shadow:0 6px 20px rgba(0,0,0,.2);display:none;align-items:center;gap:.5rem;border-left:3px solid #A8883A}

@media(max-width:900px){
  .bo-stat-grid{grid-template-columns:repeat(2,1fr)}
  .bo-book-grid,.bo-ct-grid{grid-template-columns:1fr}
}
@media(max-width:640px){
  .bo-sb{display:none}
  .bo-fgrid2,.bo-fgrid3{grid-template-columns:1fr}
}
</style>

<div class="bo-toast" id="boToast">✓ <span id="boToastMsg"></span></div>

<!-- Add/Edit Unit Modal -->
<div class="bo-modal-bg" id="boUnitModal">
  <div class="bo-modal">
    <div class="bo-modal-hdr">
      <div class="bo-modal-title" id="boModalTitle">新增可售戶</div>
      <button class="bo-modal-close" onclick="closeUnitModal()">✕</button>
    </div>
    <div class="bo-modal-body">
      <input type="hidden" id="boEditIdx" value="-1"/>
      <div class="bo-fg2"><label>建案名稱 *</label>
        <select id="mProj">
          <option value="">-- 請選擇 --</option>
          <option>譽誠沐光苑</option><option>譽誠和風居</option>
          <option>譽誠晴山苑</option><option>譽誠星曜</option><option>譽誠綠意村</option>
        </select>
      </div>
      <div class="bo-fgrid2">
        <div class="bo-fg2"><label>樓層 *</label><input type="text" id="mFloor" placeholder="例：8F"/></div>
        <div class="bo-fg2"><label>戶別 *</label><input type="text" id="mUnit" placeholder="例：A棟-01"/></div>
      </div>
      <div class="bo-fgrid2">
        <div class="bo-fg2"><label>房型 *</label>
          <select id="mType">
            <option>2房2廳</option><option>2房2廳1衛</option>
            <option>3房2廳</option><option>3房2廳1衛</option><option>3房2廳2衛</option>
            <option>4房3廳</option><option>4房3廳2衛</option>
          </select>
        </div>
        <div class="bo-fg2"><label>坪數</label><input type="text" id="mSize" placeholder="例：28.5"/></div>
      </div>
      <div class="bo-fgrid2">
        <div class="bo-fg2"><label>售價 *</label><input type="text" id="mPrice" placeholder="例：988萬"/></div>
        <div class="bo-fg2"><label>車位</label>
          <select id="mParking"><option>無</option><option>1車位</option><option>2車位</option></select>
        </div>
      </div>
      <div class="bo-fgrid2">
        <div class="bo-fg2"><label>管理費/月</label><input type="text" id="mMgmt" placeholder="例：2,800/月"/></div>
        <div class="bo-fg2"><label>狀態</label>
          <select id="mStatus"><option>可售</option><option>保留中</option><option>已成交</option></select>
        </div>
      </div>
    </div>
    <div class="bo-modal-foot">
      <button class="bb bb-outline" onclick="closeUnitModal()">取消</button>
      <button class="bb bb-primary" onclick="saveUnit()">確認儲存</button>
    </div>
  </div>
</div>

<!-- BROKER OVERLAY -->
<div id="brokerOverlay">

  <div id="boLogin">
    <button class="bo-back" onclick="closeBrokerOverlay()">← 返回首頁</button>
    <div class="bo-login-box">
      <div class="bo-login-brand">譽誠廣告</div>
      <div class="bo-login-sub">仲介合作夥伴專區</div>
      <div class="bo-login-err" id="boLoginErr">帳號或密碼錯誤</div>
      <form onsubmit="boDoLogin(event)">
        <div class="bo-fg"><label>帳號</label><input type="text" id="boUser" placeholder="Email"/></div>
        <div class="bo-fg"><label>密碼</label><input type="password" id="boPass" placeholder="Password"/></div>
        <button type="submit" class="bo-login-btn">登 入</button>
      </form>
      <div class="bo-demo">
        測試帳號：<strong>broker@yucheng.com</strong><br/>
        密碼：<strong>yucheng2025</strong>
      </div>
    </div>
  </div>

  <div id="boDash">
    <div class="bo-wrap">
      <aside class="bo-sb">
        <div class="bo-sb-top">
          <div class="bo-sb-brand">譽誠廣告</div>
          <div class="bo-sb-label">仲介合作專區</div>
        </div>
        <div class="bo-sb-user">
          <div class="bo-sb-av">王</div>
          <div><div class="bo-sb-name">王大明 仲介</div><div class="bo-sb-role">合作仲介夥伴</div></div>
        </div>
        <nav class="bo-sb-nav">
          <div class="bo-sb-sec">主要功能</div>
          <button class="bo-ni active" onclick="boSwitch(this,'overview')"><span class="ico">▤</span>總覽儀表板</button>
          <button class="bo-ni" onclick="boSwitch(this,'units')"><span class="ico">⊞</span>即時可售戶<span class="bo-nbadge" id="unitsBadge">—</span></button>
          <button class="bo-ni" onclick="boSwitch(this,'projects')"><span class="ico">◫</span>建案詳細資料</button>
          <div class="bo-sb-sec">帶看服務</div>
          <button class="bo-ni" onclick="boSwitch(this,'booking')"><span class="ico">◻</span>帶看登記系統</button>
          <button class="bo-ni" onclick="boSwitch(this,'conflict')"><span class="ico">◎</span>撞客查詢</button>
          <div class="bo-sb-sec">資源中心</div>
          <button class="bo-ni" onclick="boSwitch(this,'materials')"><span class="ico">▦</span>素材下載區</button>
          <button class="bo-ni" onclick="boSwitch(this,'commission')"><span class="ico">◈</span>傭金公告</button>
          <div class="bo-sb-sec">資訊</div>
          <button class="bo-ni" onclick="boSwitch(this,'news')"><span class="ico">◉</span>最新消息<span class="bo-nbadge">3</span></button>
          <button class="bo-ni" onclick="boSwitch(this,'contact')"><span class="ico">◌</span>聯絡窗口</button>
        </nav>
        <div class="bo-sb-foot">
          <button class="bo-logout-btn" onclick="boDoLogout()">→ 登出</button>
        </div>
      </aside>

      <div class="bo-main">
        <div class="bo-topbar">
          <div class="bo-tb-title" id="boTopTitle">總覽儀表板</div>
          <div class="bo-tb-right">
            <div class="bo-date" id="boDate"></div>
            <button class="bo-close" onclick="closeBrokerOverlay()">← 返回首頁</button>
          </div>
        </div>
        <div class="bo-content">

          <!-- OVERVIEW -->
          <div class="bo-panel active" id="bop-overview">
            <div class="bo-stat-grid">
              <div class="bo-stat"><div class="bo-stat-num" id="ovUnits">—</div><div class="bo-stat-lbl">即時可售戶</div></div>
              <div class="bo-stat"><div class="bo-stat-num" id="ovBookings">—</div><div class="bo-stat-lbl">帶看預約</div></div>
              <div class="bo-stat"><div class="bo-stat-num">8</div><div class="bo-stat-lbl">本月已成交</div></div>
              <div class="bo-stat"><div class="bo-stat-num">3</div><div class="bo-stat-lbl">未讀消息</div></div>
            </div>
            <div class="boc">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
                <div class="boc-title" style="margin:0">最近帶看記錄</div>
                <button class="bb bb-outline bb-sm" onclick="boSwitch(document.querySelector('.bo-ni[onclick*=booking]'),'booking')">查看全部</button>
              </div>
              <div class="bo-table-wrap"><table class="bt2"><thead><tr><th>日期</th><th>時間</th><th>建案</th><th>客戶</th><th>狀態</th></tr></thead><tbody id="boRecentBk"></tbody></table></div>
            </div>
            <div class="boc">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem">
                <div class="boc-title" style="margin:0">熱門可售戶</div>
                <button class="bb bb-outline bb-sm" onclick="boSwitch(document.querySelector('.bo-ni[onclick*=units]'),'units')">查看全部</button>
              </div>
              <div class="bo-table-wrap">
                <table class="bt2"><thead><tr><th>建案</th><th>樓層/戶別</th><th>房型</th><th>坪數</th><th>售價</th><th>狀態</th><th>操作</th></tr></thead>
                <tbody id="boHotUnits"></tbody></table>
              </div>
            </div>
          </div>

          <!-- UNITS -->
          <div class="bo-panel" id="bop-units">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1rem">
              <div style="font-family:'Noto Serif TC',serif;font-size:.98rem;font-weight:700;color:#1B3228">可售戶管理</div>
              <button class="bb bb-primary" onclick="openAddUnit()">＋ 新增可售戶</button>
            </div>
            <div class="bo-proj-tabs" id="boProjTabs2"></div>
            <div class="bo-fbar">
              <input type="text" placeholder="搜尋戶別、房型..." id="boUSearch" oninput="boFilterUnits()"/>
              <select id="boUStat" onchange="boFilterUnits()">
                <option value="">全部狀態</option><option>可售</option><option>保留中</option><option>已成交</option>
              </select>
            </div>
            <div class="bo-table-wrap">
              <table class="bt2">
                <thead><tr><th>建案</th><th>樓層</th><th>戶別</th><th>房型</th><th>坪數</th><th>售價</th><th>車位</th><th>管理費</th><th>狀態</th><th>操作</th></tr></thead>
                <tbody id="boUnitsTbody"></tbody>
              </table>
            </div>
          </div>

          <!-- PROJECTS -->
          <div class="bo-panel" id="bop-projects">
            <div class="bo-proj-tabs" id="boProjTabsMain"></div>
            <div id="boProjDetail"></div>
          </div>

          <!-- BOOKING -->
          <div class="bo-panel" id="bop-booking">
            <div class="bo-book-grid">
              <div class="boc">
                <div class="boc-title">新增帶看登記</div>
                <div id="boBookForm">
                  <div class="bo-fg2"><label>選擇建案 *</label>
                    <select id="boBkProj" onchange="boBkUnits()">
                      <option value="">-- 請選擇 --</option>
                      <option>譽誠沐光苑</option><option>譽誠和風居</option>
                      <option>譽誠晴山苑</option><option>譽誠星曜</option><option>譽誠綠意村</option>
                    </select>
                  </div>
                  <div class="bo-fg2"><label>選擇戶別 *</label><select id="boBkUnit"><option>-- 請先選擇建案 --</option></select></div>
                  <div class="bo-fgrid2">
                    <div class="bo-fg2"><label>帶看日期 *</label><input type="date" id="boBkDate"/></div>
                    <div class="bo-fg2"><label>帶看時間 *</label>
                      <select id="boBkTime">
                        <option>09:00</option><option>09:30</option><option>10:00</option><option>10:30</option>
                        <option>11:00</option><option>11:30</option><option>13:30</option><option>14:00</option>
                        <option>14:30</option><option>15:00</option><option>15:30</option><option>16:00</option>
                      </select>
                    </div>
                  </div>
                  <div style="height:1px;background:#ECEAE6;margin:.8rem 0"></div>
                  <div class="bo-fgrid2">
                    <div class="bo-fg2"><label>客戶姓名 *</label><input type="text" id="boBkName" placeholder="陳小姐"/></div>
                    <div class="bo-fg2"><label>客戶電話 *</label><input type="tel" id="boBkPhone" placeholder="09XX-XXX-XXX"/></div>
                  </div>
                  <div class="bo-fg2"><label>備註</label><textarea id="boBkNote" rows="3" placeholder="偏好樓層、停車需求..."></textarea></div>
                  <button class="bb bb-primary" style="width:100%;justify-content:center;padding:.72rem;font-size:.84rem" onclick="boSubmitBooking()">確認提交帶看登記</button>
                </div>
                <div id="boBookOk" style="display:none;text-align:center;padding:2.5rem 1rem">
                  <div style="font-size:1.8rem;margin-bottom:.8rem;color:#A8883A">✓</div>
                  <div style="font-family:'Noto Serif TC',serif;font-size:.98rem;color:#1B3228;font-weight:700;margin-bottom:.4rem">登記成功</div>
                  <div style="font-size:.79rem;color:#aaa" id="boBookOkMsg"></div>
                  <button class="bb bb-outline" style="margin-top:1.2rem" onclick="boResetBook()">繼續登記</button>
                </div>
              </div>
              <div class="boc">
                <div class="boc-title">帶看行程表</div>
                <div class="bo-mini-cal" id="boCal"></div>
                <div id="boBookRecs"></div>
              </div>
            </div>
          </div>

          <!-- CONFLICT -->
          <div class="bo-panel" id="bop-conflict">
            <div style="display:grid;grid-template-columns:380px 1fr;gap:1.5rem;align-items:start">
              <div class="boc">
                <div class="boc-title">撞客查詢</div>
                <p style="font-size:.81rem;color:#888;line-height:1.75;margin-bottom:1.2rem">輸入客戶電話確認是否已被其他仲介登記，客戶保護期 60 天。</p>
                <div class="bo-fg2"><label>選擇建案 *</label>
                  <select id="boCfProj"><option value="">-- 請選擇 --</option>
                    <option>譽誠沐光苑</option><option>譽誠和風居</option>
                    <option>譽誠晴山苑</option><option>譽誠星曜</option><option>譽誠綠意村</option>
                  </select>
                </div>
                <div class="bo-fg2"><label>客戶電話 *</label><input type="tel" id="boCfPhone" placeholder="09XX-XXX-XXX"/></div>
                <div class="bo-fg2"><label>客戶姓名（選填）</label><input type="text" id="boCfName"/></div>
                <button class="bb bb-primary" style="width:100%;justify-content:center;padding:.7rem" onclick="boCheckConflict()">立即查詢</button>
                <div id="boCfResult" class="bo-cf-result"></div>
              </div>
              <div class="boc">
                <div class="boc-title">保護規則說明</div>
                <div style="border-left:3px solid #A8883A;padding:.6rem 1rem;background:#F9F7F3;margin-bottom:1.2rem">
                  <div style="font-size:.8rem;font-weight:700;color:#1B3228;margin-bottom:.4rem">客戶歸屬原則</div>
                  <p style="font-size:.77rem;color:#666;line-height:1.85">同一客戶同一建案，以第一次帶看登記之仲介為主。超過 60 天保護期後視為公開客戶。</p>
                </div>
                <ul style="font-size:.79rem;color:#555;line-height:2.3;padding-left:.8rem">
                  <li>• 登記時請確實填寫客戶電話</li>
                  <li>• 系統以電話號碼作為主要比對依據</li>
                  <li>• 帶看當天須於系統確認出席狀態</li>
                  <li>• 糾紛請洽仲介合作窗口（陳志豪副理）</li>
                </ul>
              </div>
            </div>
          </div>

          <!-- MATERIALS -->
          <div class="bo-panel" id="bop-materials">
            <div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1.4rem" id="boMatTabs">
              <button class="bb bb-primary bb-sm" onclick="boFilterMat('all',this)">全部</button>
              <button class="bb bb-outline bb-sm" onclick="boFilterMat('photo',this)">照片</button>
              <button class="bb bb-outline bb-sm" onclick="boFilterMat('video',this)">短影音</button>
              <button class="bb bb-outline bb-sm" onclick="boFilterMat('copy',this)">文案</button>
              <button class="bb bb-outline bb-sm" onclick="boFilterMat('dm',this)">DM</button>
              <button class="bb bb-outline bb-sm" onclick="boFilterMat('logo',this)">LOGO</button>
            </div>
            <div class="bo-mat-grid" id="boMatGrid"></div>
          </div>

          <!-- COMMISSION -->
          <div class="bo-panel" id="bop-commission">
            <div class="bo-comm-banner">
              <div>
                <div style="font-family:'Noto Serif TC',serif;font-size:.98rem;font-weight:700;margin-bottom:.2rem">2025 年 Q2 傭金方案</div>
                <div style="font-size:.76rem;color:rgba(255,255,255,.55)">有效期間：2025/04/01 — 2025/06/30</div>
              </div>
              <span style="font-size:.7rem;background:rgba(168,136,58,.25);color:#E8C87A;padding:.3rem .9rem;border:1px solid rgba(168,136,58,.4)">現行方案</span>
            </div>
            <div class="boc" style="margin-bottom:1.2rem">
              <div class="boc-title">各建案傭金比例</div>
              <div class="bo-table-wrap"><table class="bt2">
                <thead><tr><th>建案名稱</th><th>基本傭金</th><th>快速成交獎勵</th><th>條件</th></tr></thead>
                <tbody>
                  <tr><td class="td-name">譽誠沐光苑</td><td style="color:#A8883A;font-weight:700">2.0%</td><td style="color:#A8883A;font-weight:700">+0.5%</td><td>30天內成交</td></tr>
                  <tr><td class="td-name">譽誠和風居</td><td style="color:#A8883A;font-weight:700">2.0%</td><td style="color:#A8883A;font-weight:700">+0.3%</td><td>指定樓層加碼</td></tr>
                  <tr><td class="td-name">譽誠晴山苑</td><td style="color:#A8883A;font-weight:700">1.8%</td><td style="color:#A8883A;font-weight:700">+0.5%</td><td>首購族優惠</td></tr>
                  <tr><td class="td-name">譽誠星曜</td><td style="color:#A8883A;font-weight:700">2.2%</td><td style="color:#A8883A;font-weight:700">+0.5%</td><td>高總價方案</td></tr>
                  <tr><td class="td-name">譽誠綠意村</td><td style="color:#A8883A;font-weight:700">2.0%</td><td style="color:#A8883A;font-weight:700">+0.8%</td><td>新案開賣獎勵</td></tr>
                </tbody>
              </table></div>
            </div>
            <div class="boc">
              <div class="boc-title">季度業績獎勵</div>
              <div class="bo-table-wrap"><table class="bt2">
                <thead><tr><th>季度成交戶數</th><th>額外獎勵</th><th>適用範圍</th></tr></thead>
                <tbody>
                  <tr><td>3 戶以上</td><td style="color:#A8883A;font-weight:700">+0.3%</td><td>當季全部成交案</td></tr>
                  <tr><td>5 戶以上</td><td style="color:#A8883A;font-weight:700">+0.5%</td><td>當季全部成交案</td></tr>
                  <tr><td>8 戶以上</td><td style="color:#A8883A;font-weight:700">+1.0% + 禮品</td><td>當季全部成交案</td></tr>
                </tbody>
              </table></div>
            </div>
          </div>

          <!-- NEWS -->
          <div class="bo-panel" id="bop-news"><div id="boNewsList"></div></div>

          <!-- CONTACT -->
          <div class="bo-panel" id="bop-contact">
            <div class="bo-ct-grid">
              <div class="boc">
                <div class="boc-title">聯絡窗口</div>
                <div class="bo-ct-person">
                  <div class="bo-ct-av">李</div>
                  <div><div class="bo-ct-name">李美玲 專員</div><div class="bo-ct-role">仲介合作窗口｜業務部</div></div>
                </div>
                <div class="bo-ct-item"><div class="bo-ct-ico">☎</div><div><strong>02-2792-XXXX</strong><br/><small style="color:#bbb">週一至週五 09:00–18:00</small></div></div>
                <div class="bo-ct-item"><div class="bo-ct-ico">@</div><div>broker@yucheng.com.tw</div></div>
                <div class="bo-ct-item"><div class="bo-ct-ico">L</div><div>LINE ID：yucheng_broker</div></div>
                <div style="height:1px;background:#ECEAE6;margin:1rem 0"></div>
                <div class="bo-ct-person" style="border:none;margin:0;padding:0">
                  <div class="bo-ct-av" style="background:#A8883A">陳</div>
                  <div><div class="bo-ct-name">陳志豪 副理</div><div class="bo-ct-role">糾紛處理｜高階諮詢</div></div>
                </div>
                <div class="bo-ct-item" style="margin-top:.8rem"><div class="bo-ct-ico">☎</div><div><strong>0912-XXX-XXX</strong></div></div>
              </div>
              <div class="boc">
                <div class="boc-title">線上留言</div>
                <div id="boCtForm">
                  <div class="bo-fgrid2">
                    <div class="bo-fg2"><label>姓名 *</label><input type="text" id="boCtName"/></div>
                    <div class="bo-fg2"><label>電話 *</label><input type="tel" id="boCtPhone"/></div>
                  </div>
                  <div class="bo-fg2"><label>主旨</label>
                    <select id="boCtSubj">
                      <option>帶看相關問題</option><option>撞客糾紛處理</option>
                      <option>傭金計算問題</option><option>素材需求申請</option><option>其他問題</option>
                    </select>
                  </div>
                  <div class="bo-fg2"><label>訊息 *</label><textarea id="boCtMsg" rows="5"></textarea></div>
                  <button class="bb bb-primary" style="width:100%;justify-content:center;padding:.7rem" onclick="boSubmitContact()">送出留言</button>
                </div>
                <div id="boCtOk" style="display:none;text-align:center;padding:3rem 1rem">
                  <div style="font-size:1.8rem;color:#A8883A;margin-bottom:.8rem">✓</div>
                  <div style="font-family:'Noto Serif TC',serif;font-size:.98rem;color:#1B3228;font-weight:700">訊息已送出</div>
                  <p style="font-size:.79rem;color:#aaa;margin-top:.4rem">1 個工作天內回覆</p>
                  <button class="bb bb-outline" style="margin-top:1.2rem" onclick="boResetContact()">再次留言</button>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</div>

<script>
/* ===== DATA ===== */
let BO_UNITS = [
  {project:'譽誠沐光苑',floor:'3F',unit:'A棟-01',type:'2房2廳',size:'26.5',price:'958萬',parking:'無',mgmt:'2,800/月',status:'可售'},
  {project:'譽誠沐光苑',floor:'5F',unit:'A棟-02',type:'2房2廳',size:'28.5',price:'988萬',parking:'1車位',mgmt:'2,800/月',status:'可售'},
  {project:'譽誠沐光苑',floor:'8F',unit:'B棟-01',type:'3房2廳',size:'34',price:'1,180萬',parking:'1車位',mgmt:'3,200/月',status:'可售'},
  {project:'譽誠沐光苑',floor:'10F',unit:'B棟-02',type:'3房2廳',size:'35.5',price:'1,220萬',parking:'2車位',mgmt:'3,200/月',status:'保留中'},
  {project:'譽誠和風居',floor:'6F',unit:'A棟-01',type:'2房2廳',size:'30',price:'1,250萬',parking:'1車位',mgmt:'3,500/月',status:'可售'},
  {project:'譽誠和風居',floor:'9F',unit:'A棟-03',type:'3房2廳',size:'36',price:'1,280萬',parking:'1車位',mgmt:'3,500/月',status:'可售'},
  {project:'譽誠和風居',floor:'12F',unit:'B棟-01',type:'3房2廳',size:'38',price:'1,380萬',parking:'2車位',mgmt:'3,800/月',status:'可售'},
  {project:'譽誠晴山苑',floor:'2F',unit:'C棟-01',type:'3房2廳1衛',size:'40',price:'1,480萬',parking:'1車位',mgmt:'4,000/月',status:'可售'},
  {project:'譽誠晴山苑',floor:'5F',unit:'C棟-03',type:'3房2廳2衛',size:'42',price:'1,580萬',parking:'2車位',mgmt:'4,200/月',status:'保留中'},
  {project:'譽誠晴山苑',floor:'8F',unit:'D棟-02',type:'4房3廳2衛',size:'52',price:'2,100萬',parking:'2車位',mgmt:'5,000/月',status:'可售'},
  {project:'譽誠星曜',floor:'18F',unit:'A棟-01',type:'3房2廳',size:'45',price:'3,200萬',parking:'2車位',mgmt:'6,500/月',status:'可售'},
  {project:'譽誠星曜',floor:'22F',unit:'A棟-02',type:'4房3廳',size:'58',price:'4,200萬',parking:'2車位',mgmt:'8,000/月',status:'可售'},
  {project:'譽誠綠意村',floor:'3F',unit:'B棟-01',type:'2房2廳',size:'25',price:'850萬',parking:'無',mgmt:'2,200/月',status:'可售'},
  {project:'譽誠綠意村',floor:'6F',unit:'B棟-02',type:'3房2廳',size:'32',price:'980萬',parking:'1車位',mgmt:'2,500/月',status:'已成交'},
];
const BO_PROJ_INFO = {
  '譽誠沐光苑':{loc:'桃園市中壢區環中東路二段100號',floors:'地上12層',date:'2025年8月',desc:'鄰近捷運A21站步行5分鐘，附基本輕裝修方案，2-3房格局。'},
  '譽誠和風居':{loc:'新北市新莊區中正路500號',floors:'地上15層',date:'2025年10月',desc:'日系設計風格，頂樓觀景平台，捷運輔大站步行8分鐘。'},
  '譽誠晴山苑':{loc:'台中市西屯區台灣大道四段1000號',floors:'地上10層',date:'2025年12月',desc:'面對大肚山第一排，3-4房大坪數，社區游泳池。'},
  '譽誠星曜':{loc:'台北市內湖區民權東路六段180號',floors:'地上24層',date:'2026年Q1',desc:'台北精品豪宅，基隆河景，私人電梯大廳。'},
  '譽誠綠意村':{loc:'新竹縣竹北市文興路一段200號',floors:'地上8層',date:'2025年6月',desc:'竹科生活圈，綠建築認證，首購首選。'},
};
const BO_MAT = [
  {name:'沐光苑外觀全景',size:'8.2 MB',icon:'▣',cat:'photo'},{name:'客廳實景照',size:'5.4 MB',icon:'▣',cat:'photo'},
  {name:'和風居樣品屋',size:'12.1 MB',icon:'▣',cat:'photo'},{name:'晴山苑山景空拍',size:'9.8 MB',icon:'▣',cat:'photo'},
  {name:'沐光苑生活影片',size:'120 MB',icon:'▶',cat:'video'},{name:'和風居宣傳片',size:'85 MB',icon:'▶',cat:'video'},
  {name:'晴山苑Reel',size:'42 MB',icon:'▶',cat:'video'},
  {name:'FB廣告文案包',size:'12 KB',icon:'▤',cat:'copy'},{name:'LINE貼文文案',size:'8 KB',icon:'▤',cat:'copy'},{name:'仲介話術SOP',size:'24 KB',icon:'▤',cat:'copy'},
  {name:'沐光苑DM A4',size:'3.2 MB',icon:'◫',cat:'dm'},{name:'和風居折頁',size:'4.5 MB',icon:'◫',cat:'dm'},{name:'全案DM合輯',size:'18 MB',icon:'◫',cat:'dm'},
  {name:'LOGO PNG',size:'2.1 MB',icon:'◈',cat:'logo'},{name:'LOGO SVG',size:'0.3 MB',icon:'◈',cat:'logo'},{name:'品牌色票規範',size:'0.8 MB',icon:'◈',cat:'logo'},
];
const BO_NEWS = [
  {day:'12',mon:'05月',title:'【重要】沐光苑5月衝刺加碼活動',exc:'本月成交任一戶型，額外+0.5%傭金，限至5月31日。',tags:['活動','加碼'],isNew:true},
  {day:'08',mon:'05月',title:'和風居12F景觀戶正式釋出',exc:'12F-B棟解除保留，38坪雙車位，售1,380萬。',tags:['新釋出'],isNew:true},
  {day:'02',mon:'05月',title:'仲介平台系統更新說明',exc:'帶看登記新增備註欄位，撞客查詢速度優化。',tags:['系統'],isNew:true},
  {day:'28',mon:'04月',title:'譽誠綠意村取得使用執照',exc:'預計6月底交屋，感謝各位仲介夥伴支持。',tags:['公告'],isNew:false},
  {day:'15',mon:'04月',title:'Q2傭金方案公告',exc:'請至傭金公告區查看最新方案。',tags:['傭金'],isNew:false},
];
let boBookings = [
  {date:'2025-05-16',time:'10:00',project:'譽誠沐光苑',unit:'5F-A棟-02',client:'陳小姐',phone:'0912-345-678',note:'',status:'確認中'},
  {date:'2025-05-18',time:'14:00',project:'譽誠和風居',unit:'9F-A棟-03',client:'林先生',phone:'0923-456-789',note:'需車位',status:'確認中'},
];
let boCurrentProj='全部',boCY,boCM;
const boPanelNames={overview:'總覽儀表板',units:'即時可售戶',projects:'建案詳細資料',booking:'帶看登記系統',conflict:'撞客查詢',materials:'素材下載區',commission:'傭金公告',news:'最新消息',contact:'聯絡窗口'};
const stag=s=>({可售:'bt-g',保留中:'bt-o',已成交:'bt-r'}[s]||'');

/* ===== OPEN / CLOSE ===== */
function openBrokerOverlay(){document.getElementById('brokerOverlay').classList.add('open');document.body.style.overflow='hidden';}
function closeBrokerOverlay(){document.getElementById('brokerOverlay').classList.remove('open');document.body.style.overflow='';}

/* ===== AUTH ===== */
function boDoLogin(e){
  e.preventDefault();
  if(document.getElementById('boUser').value.trim()==='broker@yucheng.com'&&document.getElementById('boPass').value==='yucheng2025'){
    document.getElementById('boLoginErr').style.display='none';
    document.getElementById('boLogin').style.display='none';
    const d=document.getElementById('boDash');d.style.display='flex';d.style.flex='1';
    boInitDash();
  } else { document.getElementById('boLoginErr').style.display='block'; }
}
function boDoLogout(){
  document.getElementById('boDash').style.display='none';
  document.getElementById('boLogin').style.display='flex';
  document.getElementById('boUser').value='';document.getElementById('boPass').value='';
}

/* ===== INIT ===== */
function boInitDash(){
  document.getElementById('boDate').textContent=new Date().toLocaleDateString('zh-TW',{year:'numeric',month:'long',day:'numeric',weekday:'short'});
  const t=new Date().toISOString().split('T')[0];
  document.getElementById('boBkDate').min=t;document.getElementById('boBkDate').value=t;
  boRefreshAll();
}
function boRefreshAll(){
  const avail=BO_UNITS.filter(u=>u.status==='可售').length;
  document.getElementById('unitsBadge').textContent=avail;
  document.getElementById('ovUnits').textContent=avail;
  document.getElementById('ovBookings').textContent=boBookings.length;
  boRenderProjTabs2();boRenderUnits();boRenderRecentBk();boRenderHotUnits();
  boRenderProjTabsMain();boRenderBookRecs();boRenderCal();boRenderMat('all');boRenderNews();
}

/* ===== NAV ===== */
function boSwitch(el,id){
  document.querySelectorAll('.bo-panel').forEach(p=>p.classList.remove('active'));
  document.getElementById('bop-'+id).classList.add('active');
  document.querySelectorAll('.bo-ni').forEach(n=>n.classList.remove('active'));
  if(el) el.classList.add('active');
  document.getElementById('boTopTitle').textContent=boPanelNames[id]||id;
  document.querySelector('.bo-content').scrollTop=0;
}

/* ===== UNITS CRUD ===== */
function boRenderProjTabs2(){
  const projs=['全部',...Object.keys(BO_PROJ_INFO)];
  document.getElementById('boProjTabs2').innerHTML=projs.map(p=>`
    <button class="bo-ptab${p===boCurrentProj?' active':''}" onclick="setProjTab('${p}')">
      ${p}${p!=='全部'?' ('+BO_UNITS.filter(u=>u.project===p).length+')':''}
    </button>`).join('');
}
function setProjTab(p){boCurrentProj=p;boRenderProjTabs2();boFilterUnits();}
function boRenderUnits(data){
  if(!data) data=boCurrentProj==='全部'?BO_UNITS:BO_UNITS.filter(u=>u.project===boCurrentProj);
  document.getElementById('boUnitsTbody').innerHTML=!data.length
    ?'<tr><td colspan="10" style="text-align:center;color:#bbb;padding:2.5rem">此分類目前無可售戶</td></tr>'
    :data.map(u=>{
      const i=BO_UNITS.indexOf(u);
      return `<tr><td class="td-name">${u.project}</td><td>${u.floor}</td><td>${u.unit}</td><td>${u.type}</td>
        <td>${u.size}坪</td><td style="color:#A8883A;font-weight:700">${u.price}</td>
        <td>${u.parking}</td><td>${u.mgmt}</td><td><span class="bt ${stag(u.status)}">${u.status}</span></td>
        <td style="display:flex;gap:.35rem;align-items:center">
          <button class="bb bb-outline bb-sm" onclick="openEditUnit(${i})">編輯</button>
          <button class="bb bb-danger bb-sm" onclick="deleteUnit(${i})">刪除</button>
          ${u.status==='可售'?`<button class="bb bb-primary bb-sm" onclick="boOpenBooking('${u.project}')">帶看</button>`:''}
        </td></tr>`;
    }).join('');
}
function boFilterUnits(){
  const q=document.getElementById('boUSearch').value.toLowerCase();
  const s=document.getElementById('boUStat').value;
  let d=boCurrentProj==='全部'?BO_UNITS:BO_UNITS.filter(u=>u.project===boCurrentProj);
  d=d.filter(u=>(!q||u.unit.toLowerCase().includes(q)||u.type.includes(q))&&(!s||u.status===s));
  boRenderUnits(d);
}
function openAddUnit(){
  document.getElementById('boEditIdx').value='-1';
  document.getElementById('boModalTitle').textContent='新增可售戶';
  ['mFloor','mUnit','mSize','mPrice','mMgmt'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('mProj').value='';
  document.getElementById('mType').value='2房2廳';
  document.getElementById('mParking').value='無';
  document.getElementById('mStatus').value='可售';
  document.getElementById('boUnitModal').classList.add('open');
}
function openEditUnit(i){
  const u=BO_UNITS[i];
  document.getElementById('boEditIdx').value=i;
  document.getElementById('boModalTitle').textContent='編輯可售戶';
  document.getElementById('mProj').value=u.project;document.getElementById('mFloor').value=u.floor;
  document.getElementById('mUnit').value=u.unit;document.getElementById('mType').value=u.type;
  document.getElementById('mSize').value=u.size;document.getElementById('mPrice').value=u.price;
  document.getElementById('mParking').value=u.parking;document.getElementById('mMgmt').value=u.mgmt;
  document.getElementById('mStatus').value=u.status;
  document.getElementById('boUnitModal').classList.add('open');
}
function closeUnitModal(){document.getElementById('boUnitModal').classList.remove('open');}
function saveUnit(){
  const proj=document.getElementById('mProj').value;
  const floor=document.getElementById('mFloor').value.trim();
  const unit=document.getElementById('mUnit').value.trim();
  const price=document.getElementById('mPrice').value.trim();
  if(!proj||!floor||!unit||!price){boToast('請填寫必填欄位');return;}
  const nu={project:proj,floor,unit,type:document.getElementById('mType').value,
    size:document.getElementById('mSize').value.trim(),price,parking:document.getElementById('mParking').value,
    mgmt:document.getElementById('mMgmt').value.trim(),status:document.getElementById('mStatus').value};
  const i=parseInt(document.getElementById('boEditIdx').value);
  if(i>=0) BO_UNITS[i]=nu; else BO_UNITS.push(nu);
  closeUnitModal();boRefreshAll();boToast(i>=0?'已更新可售戶':'已新增可售戶');
}
function deleteUnit(i){if(confirm('確定刪除此可售戶？無法復原。')){BO_UNITS.splice(i,1);boRefreshAll();boToast('已刪除');}}
function boRenderHotUnits(){
  document.getElementById('boHotUnits').innerHTML=BO_UNITS.filter(u=>u.status==='可售').slice(0,5).map(u=>`
    <tr><td class="td-name">${u.project}</td><td>${u.floor}-${u.unit}</td><td>${u.type}</td>
    <td>${u.size}坪</td><td style="color:#A8883A;font-weight:700">${u.price}</td>
    <td><span class="bt ${stag(u.status)}">${u.status}</span></td>
    <td><button class="bb bb-primary bb-sm" onclick="boOpenBooking('${u.project}')">帶看</button></td></tr>`).join('');
}

/* ===== PROJECTS ===== */
function boRenderProjTabsMain(){
  const keys=Object.keys(BO_PROJ_INFO);
  document.getElementById('boProjTabsMain').innerHTML=keys.map((p,i)=>
    `<button class="bo-ptab${i===0?' active':''}" onclick="boShowProj('${p}',this)">${p}</button>`).join('');
  boShowProj(keys[0],null);
}
function boShowProj(name,el){
  if(el) document.querySelectorAll('#boProjTabsMain .bo-ptab').forEach(t=>t.classList.toggle('active',t===el));
  const d=BO_PROJ_INFO[name],units=BO_UNITS.filter(u=>u.project===name);
  const avail=units.filter(u=>u.status==='可售').length;
  document.getElementById('boProjDetail').innerHTML=`
    <div style="background:#1B3228;padding:1.8rem 2rem;margin-bottom:1.4rem;display:flex;justify-content:space-between;align-items:flex-end;flex-wrap:wrap;gap:1rem">
      <div>
        <div style="font-family:'Noto Serif TC',serif;font-size:1.4rem;font-weight:700;color:#fff;letter-spacing:.04em;margin-bottom:.3rem">${name}</div>
        <div style="font-size:.79rem;color:rgba(255,255,255,.5);margin-bottom:.2rem">${d.loc}</div>
        <div style="font-size:.74rem;color:rgba(255,255,255,.35)">${d.floors}　預計 ${d.date} 交屋</div>
      </div>
      <div style="text-align:right">
        <div style="font-size:1.8rem;font-weight:700;color:#A8883A;font-family:'Noto Serif TC',serif">${units[0]?.price||'—'}<span style="font-size:.55em">起</span></div>
        <div style="font-size:.7rem;color:rgba(255,255,255,.35);margin-top:.2rem">${avail} 戶可售</div>
      </div>
    </div>
    <div class="boc" style="margin-bottom:1.2rem">
      <div style="font-size:.68rem;font-weight:700;color:#aaa;letter-spacing:.12em;text-transform:uppercase;border-left:3px solid #A8883A;padding-left:.7rem;margin-bottom:.9rem">建案說明</div>
      <p style="font-size:.84rem;color:#555;line-height:1.9">${d.desc}</p>
    </div>
    <div class="boc">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1.1rem">
        <div style="font-size:.68rem;font-weight:700;color:#aaa;letter-spacing:.12em;text-transform:uppercase;border-left:3px solid #A8883A;padding-left:.7rem">戶別一覽</div>
        <button class="bb bb-primary bb-sm" onclick="openAddUnit()">＋ 新增戶別</button>
      </div>
      <div class="bo-table-wrap"><table class="bt2">
        <thead><tr><th>樓層</th><th>戶別</th><th>房型</th><th>坪數</th><th>售價</th><th>車位</th><th>管理費</th><th>狀態</th><th>操作</th></tr></thead>
        <tbody>${units.map(u=>{const ri=BO_UNITS.indexOf(u);return`
          <tr><td>${u.floor}</td><td>${u.unit}</td><td>${u.type}</td><td>${u.size}坪</td>
          <td style="color:#A8883A;font-weight:700">${u.price}</td><td>${u.parking}</td><td>${u.mgmt}</td>
          <td><span class="bt ${stag(u.status)}">${u.status}</span></td>
          <td style="display:flex;gap:.35rem">
            <button class="bb bb-outline bb-sm" onclick="openEditUnit(${ri})">編輯</button>
            <button class="bb bb-danger bb-sm" onclick="deleteUnit(${ri})">刪除</button>
          </td></tr>`;}).join('')}
        </tbody></table>
      </div>
    </div>`;
}

/* ===== BOOKING ===== */
function boBkUnits(){
  const p=document.getElementById('boBkProj').value;
  const units=BO_UNITS.filter(u=>u.project===p&&u.status==='可售');
  document.getElementById('boBkUnit').innerHTML=units.length
    ?units.map(u=>`<option>${u.floor}-${u.unit}</option>`).join('')
    :'<option>此建案目前無可售戶</option>';
}
function boOpenBooking(proj){
  boSwitch(document.querySelector('.bo-ni[onclick*=booking]'),'booking');
  setTimeout(()=>{document.getElementById('boBkProj').value=proj;boBkUnits();},80);
}
function boSubmitBooking(){
  const proj=document.getElementById('boBkProj').value;
  const unit=document.getElementById('boBkUnit').value;
  const date=document.getElementById('boBkDate').value;
  const time=document.getElementById('boBkTime').value;
  const name=document.getElementById('boBkName').value.trim();
  const phone=document.getElementById('boBkPhone').value.trim();
  if(!proj||!unit||!date||!name||!phone){boToast('請填寫所有必填欄位');return;}
  boBookings.unshift({date,time,project:proj,unit,client:name,phone,note:document.getElementById('boBkNote').value,status:'待確認'});
  boRenderRecentBk();boRenderBookRecs();boRenderCal();boRefreshAll();
  document.getElementById('boBookForm').style.display='none';
  document.getElementById('boBookOkMsg').textContent=`${date} ${time} · ${proj} · ${name}`;
  document.getElementById('boBookOk').style.display='block';
  boToast('帶看登記成功');
}
function boResetBook(){
  document.getElementById('boBookForm').style.display='block';
  document.getElementById('boBookOk').style.display='none';
  ['boBkProj','boBkName','boBkPhone','boBkNote'].forEach(id=>document.getElementById(id).value='');
  document.getElementById('boBkUnit').innerHTML='<option>-- 請先選擇建案 --</option>';
}
function boRenderRecentBk(){
  document.getElementById('boRecentBk').innerHTML=boBookings.slice(0,5).map(b=>
    `<tr><td>${b.date}</td><td>${b.time}</td><td class="td-name">${b.project}</td><td>${b.client}</td>
    <td><span class="bt ${b.status==='確認中'?'bt-g':'bt-o'}">${b.status}</span></td></tr>`).join('');
}
function boRenderBookRecs(){
  const el=document.getElementById('boBookRecs');
  if(!boBookings.length){el.innerHTML='<p style="color:#bbb;text-align:center;padding:1.5rem;font-size:.8rem">尚無帶看記錄</p>';return;}
  el.innerHTML=boBookings.slice(0,6).map((b,i)=>{
    const[,m,d]=b.date.split('-');
    return`<div class="bo-brec">
      <div class="bo-brec-date"><div class="bo-brec-d">${d}</div><div class="bo-brec-m">${m}月</div></div>
      <div class="bo-brec-info"><div class="bo-brec-proj">${b.project}</div>
      <div class="bo-brec-meta">${b.time} · ${b.unit}<br/>${b.client} · ${b.phone}</div></div>
      <button class="bb bb-danger bb-sm" onclick="boCancelBk(${i})">取消</button>
    </div>`;}).join('');
}
function boCancelBk(i){if(confirm('確定取消？')){boBookings.splice(i,1);boRenderBookRecs();boRenderRecentBk();boRenderCal();boRefreshAll();boToast('已取消');}}

function boRenderCal(off=0){
  if(boCY===undefined){const n=new Date();boCY=n.getFullYear();boCM=n.getMonth();}
  boCM+=off;if(boCM>11){boCM=0;boCY++;}if(boCM<0){boCM=11;boCY--;}
  const today=new Date(),fd=new Date(boCY,boCM,1).getDay(),dim=new Date(boCY,boCM+1,0).getDate();
  const bd=boBookings.map(b=>b.date);
  const mons=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'];
  let h=`<div class="bo-cal-hdr"><button class="bo-cal-nav" onclick="boRenderCal(-1)">‹</button>
    <span>${boCY}年 ${mons[boCM]}</span><button class="bo-cal-nav" onclick="boRenderCal(1)">›</button></div>
    <div class="bo-cal-grid">
    <div class="bo-cal-dl">日</div><div class="bo-cal-dl">一</div><div class="bo-cal-dl">二</div>
    <div class="bo-cal-dl">三</div><div class="bo-cal-dl">四</div><div class="bo-cal-dl">五</div><div class="bo-cal-dl">六</div>`;
  for(let i=0;i<fd;i++)h+='<div class="bo-cal-d empty"></div>';
  for(let d=1;d<=dim;d++){
    const ds=`${boCY}-${String(boCM+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
    const iT=today.getFullYear()===boCY&&today.getMonth()===boCM&&today.getDate()===d;
    h+=`<div class="bo-cal-d${iT?' today':''}${bd.includes(ds)?' has-b':''}">${d}</div>`;
  }
  h+='</div>';document.getElementById('boCal').innerHTML=h;
}

/* ===== CONFLICT ===== */
function boCheckConflict(){
  const proj=document.getElementById('boCfProj').value;
  const phone=document.getElementById('boCfPhone').value.trim();
  if(!proj||!phone){boToast('請填寫建案與電話');return;}
  const el=document.getElementById('boCfResult');el.style.display='block';
  const found=boBookings.find(b=>b.project===proj&&b.phone.replace(/-/g,'')===phone.replace(/-/g,''));
  if(found){
    el.className='bo-cf-result danger';
    el.innerHTML=`<div style="font-weight:700;color:#DC2626;margin-bottom:.5rem">⚠ 此客戶已有帶看記錄</div>
      <p style="font-size:.79rem;color:#555">建案：${found.project}<br/>帶看：${found.date} ${found.time}<br/>如有糾紛請洽聯絡窗口</p>`;
  } else {
    el.className='bo-cf-result safe';
    el.innerHTML=`<div style="font-weight:700;color:#059669;margin-bottom:.5rem">✓ 無衝突記錄</div>
      <p style="font-size:.79rem;color:#555">在 <strong>${proj}</strong> 查無此電話帶看記錄，可安心安排帶看。</p>`;
  }
}

/* ===== MATERIALS ===== */
function boRenderMat(cat){
  const d=cat==='all'?BO_MAT:BO_MAT.filter(m=>m.cat===cat);
  document.getElementById('boMatGrid').innerHTML=d.map(m=>`
    <div class="bo-mat-item" onclick="boToast('開始下載：${m.name}')">
      <div class="bo-mat-thumb">${m.icon}</div>
      <div class="bo-mat-info"><div class="bo-mat-name">${m.name}</div>
      <div class="bo-mat-size">${m.size}</div><div class="bo-mat-dl">↓ 下載</div></div>
    </div>`).join('');
}
function boFilterMat(cat,el){
  document.querySelectorAll('#boMatTabs .bb').forEach(b=>{b.className='bb bb-outline bb-sm';});
  el.className='bb bb-primary bb-sm';boRenderMat(cat);
}

/* ===== NEWS ===== */
function boRenderNews(){
  document.getElementById('boNewsList').innerHTML=BO_NEWS.map(n=>`
    <div class="bo-news-item">
      <div class="bo-news-date"><div class="bnd-d">${n.day}</div><div class="bnd-m">${n.mon}</div></div>
      <div class="bo-news-body">
        <div class="bo-news-title">${n.isNew?'<span class="bt bt-r" style="margin-right:.4rem">NEW</span>':''}${n.title}</div>
        <div class="bo-news-exc">${n.exc}</div>
        <div class="bo-news-tags">${n.tags.map(t=>`<span class="bt bt-g">${t}</span>`).join(' ')}</div>
      </div>
    </div>`).join('');
}

/* ===== CONTACT ===== */
function boSubmitContact(){
  if(!document.getElementById('boCtName').value.trim()||!document.getElementById('boCtMsg').value.trim()){boToast('請填寫必填欄位');return;}
  document.getElementById('boCtForm').style.display='none';
  document.getElementById('boCtOk').style.display='block';
  boToast('留言送出成功');
}
function boResetContact(){
  document.getElementById('boCtForm').style.display='block';
  document.getElementById('boCtOk').style.display='none';
  ['boCtName','boCtPhone','boCtMsg'].forEach(id=>document.getElementById(id).value='');
}

/* ===== TOAST ===== */
let boTT;
function boToast(msg){
  const t=document.getElementById('boToast');
  document.getElementById('boToastMsg').textContent=msg;
  t.style.display='flex';clearTimeout(boTT);
  boTT=setTimeout(()=>t.style.display='none',3000);
}
</script>
'''

new_content = before + '\n' + new_broker + '\n' + after
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Done, total chars:', len(new_content))
