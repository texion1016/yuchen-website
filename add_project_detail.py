# -*- coding: utf-8 -*-
"""
Add full project detail overlay to each 查看建案 button.
- Full-screen overlay (z-index 9500)
- Hero image + gallery strip
- 建案內容 spec grid (like reference image)
- 可售格局, 生活機能, 交通
- CTA to booking
"""

with open('C:/Users/ROG/yuchen-website/index.html', encoding='utf-8') as f:
    html = f.read()

# ── 1. PROJECT DATA EMBEDDED IN JS ────────────────────────────────────────────
PROJECT_DATA_JS = """
/* ===== PROJECT DETAIL DATA ===== */
const PROJECT_DATA = {
  '譽誠沐光苑': {
    tag: '新上架', tagClass: 'new',
    location: '桃園市中壢區',
    address: '桃園市中壢區中山路168號',
    price: '988萬起',
    priceNote: '附基本輕裝修，即買即住',
    desc: '譽誠沐光苑坐落於桃園中壢核心生活圈，緊鄰捷運站步行5分鐘，匯集商圈、醫療、學區三大優勢。建案以「光」為設計主軸，大面開窗引入自然採光，打造溫潤舒適的居家氛圍，是首購族與換屋族的理想選擇。',
    img: 'https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=1200&h=700&fit=crop',
    gallery: [
      'https://images.unsplash.com/photo-1560185007-cde436f6a4d0?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=400&h=280&fit=crop',
    ],
    specs: [
      {label:'基地面積', value:'452.60坪'},
      {label:'基地座向', value:'坐北朝南'},
      {label:'坐落區域', value:'桃園市中壢區'},
      {label:'基地位置', value:'中壢區中山段220地號'},
      {label:'使用分區', value:'住宅區'},
      {label:'格局規劃', value:'2房28坪、3房35坪'},
      {label:'建築構造', value:'RC構造'},
      {label:'樓層規劃', value:'地上18層、地下2層'},
      {label:'戶數規劃', value:'住家88戶、店面4戶'},
    ],
    units: [
      {type:'2房2廳1衛', area:'28坪', price:'988萬起', status:'可售'},
      {type:'3房2廳2衛', area:'35坪', price:'1,180萬起', status:'可售'},
      {type:'3房2廳2衛', area:'38坪', price:'1,280萬起', status:'保留中'},
    ],
    transport: ['中壢火車站步行8分鐘','捷運中壢站步行5分鐘','國道一號中壢交流道車程3分鐘'],
    amenities: ['中壢遠東百貨', 'SOGO百貨', '中壢市場', '壢新醫院', '中原大學', '中壢高中'],
  },
  '譽誠和風居': {
    tag: '熱銷中', tagClass: '',
    location: '新北市新莊區',
    address: '新北市新莊區中正路500號',
    price: '1,280萬起',
    priceNote: '精裝交屋，家具可議',
    desc: '譽誠和風居汲取日本匠人美學精髓，以榻榻米、檜木格柵、枯山水元素融入現代建築語彙。頂樓設360度環景空中花園，俯瞰觀音山與淡水河景，靜謐的居住環境讓您遠離塵囂，享受身心的全然療癒。',
    img: 'https://images.unsplash.com/photo-1484154218962-a197022b5858?w=1200&h=700&fit=crop',
    gallery: [
      'https://images.unsplash.com/photo-1505691723518-36a5ac3be353?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1556909172-54557c7e4fb7?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1560185008-b033106af5c3?w=400&h=280&fit=crop',
    ],
    specs: [
      {label:'基地面積', value:'380.20坪'},
      {label:'基地座向', value:'坐東朝西'},
      {label:'坐落區域', value:'新北市新莊區'},
      {label:'基地位置', value:'新莊區和風段56地號'},
      {label:'使用分區', value:'住商混合區'},
      {label:'格局規劃', value:'2房32坪、3房42坪'},
      {label:'建築構造', value:'SRC構造'},
      {label:'樓層規劃', value:'地上22層、地下3層'},
      {label:'戶數規劃', value:'住家96戶、店面6戶'},
    ],
    units: [
      {type:'2房2廳1衛', area:'32坪', price:'1,280萬起', status:'可售'},
      {type:'3房2廳2衛', area:'42坪', price:'1,620萬起', status:'可售'},
      {type:'頂樓複層', area:'65坪', price:'2,480萬起', status:'僅剩2戶'},
    ],
    transport: ['輔大站步行6分鐘','新莊站車程5分鐘','台65快速道路匝道車程2分鐘'],
    amenities: ['新莊廟街商圈', '新莊棒球場', '輔仁大學', '新莊國泰醫院', '宏匯廣場', '家樂福新莊店'],
  },
  '譽誠晴山苑': {
    tag: '即將完工', tagClass: '',
    location: '台中市西屯區',
    address: '台中市西屯區台灣大道四段888號',
    price: '1,580萬起',
    priceNote: '毛胚交屋，輕裝修方案可加購',
    desc: '譽誠晴山苑依山而建，獨佔台中七期重劃區最後一排純山景第一排席位。錯落有致的天際線輪廓，搭配落地玻璃帷幕，讓大坪數住宅得以將合歡山脈盡收眼底，山嵐雲霧隨四季更迭，每一天都是絕美畫作。',
    img: 'https://images.unsplash.com/photo-1512917774080-9991b1c3d4b7?w=1200&h=700&fit=crop',
    gallery: [
      'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1565402170291-8491f1b27463?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1564013799919-ab600027ffc6?w=400&h=280&fit=crop',
    ],
    specs: [
      {label:'基地面積', value:'628.40坪'},
      {label:'基地座向', value:'坐西朝東'},
      {label:'坐落區域', value:'台中市西屯區'},
      {label:'基地位置', value:'西屯區晴山段100地號'},
      {label:'使用分區', value:'住宅區'},
      {label:'格局規劃', value:'3房45坪、4房58坪'},
      {label:'建築構造', value:'SRC構造'},
      {label:'樓層規劃', value:'地上24層、地下4層'},
      {label:'戶數規劃', value:'住家72戶'},
    ],
    units: [
      {type:'3房2廳2衛', area:'45坪', price:'1,580萬起', status:'可售'},
      {type:'4房3廳2衛', area:'58坪', price:'2,080萬起', status:'可售'},
      {type:'景觀大坪數', area:'72坪', price:'2,880萬起', status:'預售中'},
    ],
    transport: ['台灣大道幹線公車直達','中港路快速通道','台中高速公路交流道車程8分鐘'],
    amenities: ['新光三越台中中港店', '大遠百台中店', '台中榮總', '逢甲大學商圈', '秋紅谷公園', '台中市政府'],
  },
  '譽誠星曜': {
    tag: '夜景戶', tagClass: '',
    location: '台北市內湖區',
    address: '台北市內湖區內湖路一段500號',
    price: '3,200萬起',
    priceNote: '全裝修交屋，視野絕佳',
    desc: '譽誠星曜屹立台北內湖科技廊道核心，俯瞰基隆河水岸全景。採用德國進口Low-E玻璃帷幕，晝攬山河壯闊、夜賞萬家燈火。頂墅專屬空中泳池、私人影音室等尊榮配備，為您打造媲美五星酒店的都市頂奢生活。',
    img: 'https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200&h=700&fit=crop',
    gallery: [
      'https://images.unsplash.com/photo-1502005229762-cf1b2da7c5d6?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1493809842364-78817add7ffb?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1416331108676-a22ccb276e35?w=400&h=280&fit=crop',
    ],
    specs: [
      {label:'基地面積', value:'907.40坪'},
      {label:'基地座向', value:'坐南朝北'},
      {label:'坐落區域', value:'台北市內湖區'},
      {label:'基地位置', value:'內湖段星曜段200地號'},
      {label:'使用分區', value:'住商混合區'},
      {label:'格局規劃', value:'2房42坪、3房55坪、4房72坪'},
      {label:'建築構造', value:'SC鋼構'},
      {label:'樓層規劃', value:'地上32層、地下5層'},
      {label:'戶數規劃', value:'住家104戶、頂墅8戶、店面2戶'},
    ],
    units: [
      {type:'2房2廳2衛', area:'42坪', price:'3,200萬起', status:'可售'},
      {type:'3房2廳2衛', area:'55坪', price:'4,100萬起', status:'可售'},
      {type:'4房3廳3衛', area:'72坪', price:'5,800萬起', status:'稀缺戶'},
      {type:'空中頂墅', area:'120坪', price:'洽詢專案', status:'預約看屋'},
    ],
    transport: ['內湖站步行3分鐘','國道一號汐止系統連接','台北市快速道路環狀線'],
    amenities: ['內湖科技園區', '家樂福內湖店', '內湖三軍總醫院', '大湖公園', '碧山巖', '美麗華百樂園'],
  },
  '譽誠綠意村': {
    tag: '新案', tagClass: 'new',
    location: '新竹縣竹北市',
    address: '新竹縣竹北市縣政二路168號',
    price: '850萬起',
    priceNote: '首購優惠方案，歡迎洽詢',
    desc: '譽誠綠意村位處新竹縣竹北生醫科技廊道，毗鄰台積電總部研發聚落，以「綠建築鑽石級認證」打造永續生態社區。大面積社區公園、全棟太陽能板、雨水回收系統，讓您在科技城的快節奏中找回自然純粹的生活步調。',
    img: 'https://images.unsplash.com/photo-1416331108676-a22ccb276e35?w=1200&h=700&fit=crop',
    gallery: [
      'https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?w=400&h=280&fit=crop',
      'https://images.unsplash.com/photo-1523217582562-09d0def993a6?w=400&h=280&fit=crop',
    ],
    specs: [
      {label:'基地面積', value:'1,024.80坪'},
      {label:'基地座向', value:'坐北朝南'},
      {label:'坐落區域', value:'新竹縣竹北市'},
      {label:'基地位置', value:'竹北市綠意段88地號'},
      {label:'使用分區', value:'住宅區'},
      {label:'格局規劃', value:'2房26坪、3房36坪'},
      {label:'建築構造', value:'RC構造'},
      {label:'樓層規劃', value:'地上16層、地下2層'},
      {label:'戶數規劃', value:'住家180戶、商業2戶'},
    ],
    units: [
      {type:'2房2廳1衛', area:'26坪', price:'850萬起', status:'可售'},
      {type:'3房2廳2衛', area:'36坪', price:'1,120萬起', status:'可售'},
      {type:'3房2廳2衛', area:'40坪', price:'1,280萬起', status:'可售'},
    ],
    transport: ['竹北火車站步行10分鐘','台68快速道路東西向','高鐵新竹站車程8分鐘'],
    amenities: ['遠東巨城購物中心', '竹北市立圖書館', '竹北國泰醫院', '新竹科學園區', '縣政文化園區', '新瓦屋客家文化保存區'],
  },
};
"""

# ── 2. PROJECT DETAIL OVERLAY HTML ────────────────────────────────────────────
PROJECT_OVERLAY_HTML = """
<!-- ═══ PROJECT DETAIL OVERLAY ═══ -->
<div id="projDetailOverlay" style="display:none;position:fixed;inset:0;z-index:9500;background:#f5f3ef;overflow-y:auto;">

  <!-- Top bar -->
  <div id="pdTopBar" style="position:sticky;top:0;z-index:10;background:rgba(245,243,239,0.95);backdrop-filter:blur(12px);border-bottom:1px solid #e0dbd2;padding:.85rem 2rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;">
    <div style="display:flex;align-items:center;gap:1rem;">
      <button onclick="closeProjDetail()" style="width:36px;height:36px;border-radius:50%;border:1.5px solid #d4cfc8;background:none;cursor:pointer;font-size:1.1rem;color:#555;display:flex;align-items:center;justify-content:center;transition:all .2s;" onmouseover="this.style.background='#1B3228';this.style.color='#fff';this.style.borderColor='#1B3228'" onmouseout="this.style.background='none';this.style.color='#555';this.style.borderColor='#d4cfc8'">←</button>
      <div>
        <div style="font-family:'Noto Serif TC',serif;font-size:.95rem;font-weight:700;color:#1B3228" id="pdBarName">建案名稱</div>
        <div style="font-size:.72rem;color:#aaa" id="pdBarLoc">地點</div>
      </div>
    </div>
    <div style="display:flex;gap:.7rem;align-items:center;">
      <button onclick="openBookingOverlay()" style="background:var(--gold);color:#fff;border:none;border-radius:10px;padding:.5rem 1.2rem;font-size:.8rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;transition:opacity .2s;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏠 預約賞屋</button>
    </div>
  </div>

  <!-- Hero image -->
  <div id="pdHero" style="width:100%;height:420px;background:url('') center/cover no-repeat;position:relative;">
    <div style="position:absolute;inset:0;background:linear-gradient(to bottom, transparent 50%, rgba(27,50,40,0.55) 100%)"></div>
    <div style="position:absolute;bottom:2rem;left:2.5rem;right:2.5rem;display:flex;align-items:flex-end;justify-content:space-between;flex-wrap:wrap;gap:1rem;">
      <div>
        <span id="pdHeroTag" class="project-tag" style="position:relative;margin-bottom:.6rem;display:inline-block;">新上架</span>
        <div style="font-family:'Noto Serif TC',serif;font-size:2rem;font-weight:700;color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.4)" id="pdHeroName">建案名稱</div>
        <div style="font-size:.85rem;color:rgba(255,255,255,.8);margin-top:.3rem" id="pdHeroAddr">📍 地址</div>
      </div>
      <div style="text-align:right;">
        <div style="font-size:2rem;font-weight:700;color:#fff;font-family:'Noto Serif TC',serif;text-shadow:0 2px 8px rgba(0,0,0,.4)" id="pdHeroPrice">000萬起</div>
        <div style="font-size:.76rem;color:rgba(255,255,255,.7)" id="pdHeroPriceNote">價格說明</div>
      </div>
    </div>
  </div>

  <!-- Gallery strip -->
  <div id="pdGallery" style="display:flex;gap:.4rem;padding:.4rem 0;overflow-x:auto;background:#1B3228;scrollbar-width:none;"></div>

  <!-- Main content -->
  <div style="max-width:1100px;margin:0 auto;padding:2.5rem 2rem 4rem;">

    <!-- Description -->
    <div style="margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid #e0dbd2;">
      <div style="font-family:'Noto Serif TC',serif;font-size:1.05rem;font-weight:700;color:#1B3228;margin-bottom:.9rem;letter-spacing:.05em;">建案內容</div>
      <p id="pdDesc" style="font-size:.88rem;color:#555;line-height:2;letter-spacing:.03em;max-width:800px;"></p>
    </div>

    <!-- Specs grid (3 col) -->
    <div style="margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid #e0dbd2;">
      <div style="font-family:'Noto Serif TC',serif;font-size:1.05rem;font-weight:700;color:#1B3228;margin-bottom:1.2rem;letter-spacing:.05em;">基本規格</div>
      <div id="pdSpecs" style="display:grid;grid-template-columns:repeat(3,1fr);gap:0;border:1px solid #e0dbd2;border-radius:12px;overflow:hidden;"></div>
    </div>

    <!-- Units -->
    <div style="margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid #e0dbd2;">
      <div style="font-family:'Noto Serif TC',serif;font-size:1.05rem;font-weight:700;color:#1B3228;margin-bottom:1.2rem;letter-spacing:.05em;">可售格局</div>
      <div id="pdUnits" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:.85rem;"></div>
    </div>

    <!-- Transport + Amenities side by side -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:2.5rem;">
      <div style="background:#fff;border-radius:14px;padding:1.3rem 1.5rem;border:1.5px solid #eceae6;">
        <div style="font-family:'Noto Serif TC',serif;font-size:.9rem;font-weight:700;color:#1B3228;margin-bottom:1rem;">🚇 交通便利</div>
        <ul id="pdTransport" style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:.6rem;"></ul>
      </div>
      <div style="background:#fff;border-radius:14px;padding:1.3rem 1.5rem;border:1.5px solid #eceae6;">
        <div style="font-family:'Noto Serif TC',serif;font-size:.9rem;font-weight:700;color:#1B3228;margin-bottom:1rem;">🏪 生活機能</div>
        <div id="pdAmenities" style="display:flex;flex-wrap:wrap;gap:.4rem;"></div>
      </div>
    </div>

    <!-- CTA -->
    <div style="background:linear-gradient(135deg,#1B3228,#2c4a3e);border-radius:18px;padding:2.5rem;text-align:center;color:#fff;">
      <div style="font-family:'Noto Serif TC',serif;font-size:1.2rem;font-weight:700;margin-bottom:.5rem;">對這個建案感興趣？</div>
      <div style="font-size:.83rem;color:rgba(255,255,255,.7);margin-bottom:1.5rem;">立即預約專屬看房時間，讓我們的顧問為您詳細介紹</div>
      <div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;">
        <button onclick="openBookingOverlay()" style="background:var(--gold);color:#fff;border:none;border-radius:12px;padding:.75rem 2rem;font-size:.88rem;font-weight:600;cursor:pointer;font-family:inherit;letter-spacing:.04em;transition:opacity .2s;" onmouseover="this.style.opacity='.85'" onmouseout="this.style.opacity='1'">🏠 預約賞屋</button>
        <a href="tel:0800-888-888" style="background:transparent;color:#fff;border:1.5px solid rgba(255,255,255,.4);border-radius:12px;padding:.75rem 2rem;font-size:.88rem;font-weight:600;cursor:pointer;font-family:inherit;text-decoration:none;display:inline-flex;align-items:center;gap:.4rem;transition:border-color .2s;" onmouseover="this.style.borderColor='rgba(255,255,255,.8)'" onmouseout="this.style.borderColor='rgba(255,255,255,.4)'">📞 電話洽詢</a>
      </div>
    </div>

  </div>
</div>
"""

# Insert overlay before </body>
body_end = html.rfind('</body>')
html = html[:body_end] + '\n' + PROJECT_OVERLAY_HTML + '\n' + html[body_end:]
print("1. Overlay HTML:", "OK")

# ── 3. PROJECT DETAIL CSS ──────────────────────────────────────────────────────
PROJECT_DETAIL_CSS = """
/* ── PROJECT DETAIL OVERLAY ──────────────────────────── */
#projDetailOverlay {
  scrollbar-width: thin;
  scrollbar-color: var(--gold) transparent;
}
#projDetailOverlay::-webkit-scrollbar { width: 5px; }
#projDetailOverlay::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 3px; }

#pdGallery::-webkit-scrollbar { display: none; }

.pd-spec-cell {
  padding: .8rem 1.1rem;
  border-right: 1px solid #e0dbd2;
  border-bottom: 1px solid #e0dbd2;
}
.pd-spec-cell:nth-child(3n) { border-right: none; }
.pd-spec-cell:nth-last-child(-n+3) { border-bottom: none; }
.pd-spec-label {
  font-size: .7rem;
  color: #aaa;
  letter-spacing: .1em;
  margin-bottom: .25rem;
}
.pd-spec-value {
  font-size: .88rem;
  font-weight: 600;
  color: #1B3228;
}
.pd-unit-card {
  background: #fff;
  border: 1.5px solid #eceae6;
  border-radius: 12px;
  padding: 1.1rem 1.2rem;
  transition: border-color .2s, box-shadow .2s;
}
.pd-unit-card:hover {
  border-color: rgba(168,136,58,.35);
  box-shadow: 0 4px 16px rgba(44,74,62,.08);
}
.pd-unit-type { font-size: .8rem; color: #888; margin-bottom: .25rem; }
.pd-unit-area { font-size: 1.1rem; font-weight: 700; color: #1B3228; font-family: 'Noto Serif TC', serif; }
.pd-unit-price { font-size: .82rem; color: var(--gold); font-weight: 600; margin-top: .2rem; }
.pd-unit-status {
  display: inline-block;
  font-size: .66rem;
  padding: .18rem .55rem;
  border-radius: 20px;
  margin-top: .4rem;
  font-weight: 600;
}
.pd-unit-status.available { background: rgba(44,74,62,.1); color: #2c4a3e; }
.pd-unit-status.reserved  { background: rgba(200,169,110,.15); color: #a8883a; }
.pd-unit-status.rare      { background: rgba(180,60,60,.1); color: #b03c3c; }
.pd-transport-item {
  display: flex;
  align-items: flex-start;
  gap: .5rem;
  font-size: .8rem;
  color: #555;
  line-height: 1.5;
}
.pd-transport-item::before {
  content: '▸';
  color: var(--gold);
  flex-shrink: 0;
  margin-top: .05rem;
}
.pd-amenity-tag {
  background: rgba(44,74,62,.07);
  color: #2c4a3e;
  border-radius: 20px;
  padding: .3rem .75rem;
  font-size: .76rem;
  font-weight: 500;
}

/* Animate in */
@keyframes pdSlideUp {
  from { opacity: 0; transform: translateY(24px); }
  to   { opacity: 1; transform: translateY(0); }
}
#projDetailOverlay.pd-visible > * {
  animation: pdSlideUp .4s ease both;
}

@media (max-width: 700px) {
  #pdSpecs { grid-template-columns: repeat(2, 1fr) !important; }
  #pdHero  { height: 280px !important; }
  #pdTopBar { padding: .7rem 1rem !important; }
  .pd-spec-cell:nth-child(3n) { border-right: 1px solid #e0dbd2; }
  .pd-spec-cell:nth-child(2n) { border-right: none !important; }
}
"""

style_end = html.rfind('</style>')
html = html[:style_end] + PROJECT_DETAIL_CSS + '\n' + html[style_end:]
print("2. CSS:", "OK")

# ── 4. PROJECT DETAIL JS ───────────────────────────────────────────────────────
PROJECT_DETAIL_JS = PROJECT_DATA_JS + """
function openProjDetail(name) {
  const d = PROJECT_DATA[name];
  if (!d) return;

  // Top bar
  document.getElementById('pdBarName').textContent = name;
  document.getElementById('pdBarLoc').textContent = '📍 ' + d.location;

  // Hero
  document.getElementById('pdHero').style.backgroundImage = "url('" + d.img + "')";
  document.getElementById('pdHeroTag').textContent = d.tag;
  document.getElementById('pdHeroTag').className = 'project-tag' + (d.tagClass ? ' ' + d.tagClass : '');
  document.getElementById('pdHeroName').textContent = name;
  document.getElementById('pdHeroAddr').textContent = '📍 ' + d.address;
  document.getElementById('pdHeroPrice').textContent = d.price;
  document.getElementById('pdHeroPriceNote').textContent = d.priceNote;

  // Gallery
  const gallery = document.getElementById('pdGallery');
  gallery.innerHTML = d.gallery.map(url =>
    `<div style="flex:0 0 180px;height:120px;background:url('${url}') center/cover no-repeat;cursor:pointer;" onclick="document.getElementById('pdHero').style.backgroundImage='url(${url.replace('280','700')}'"></div>`
  ).join('');

  // Description
  document.getElementById('pdDesc').textContent = d.desc;

  // Specs grid
  document.getElementById('pdSpecs').innerHTML = d.specs.map(s =>
    `<div class="pd-spec-cell"><div class="pd-spec-label">${s.label}</div><div class="pd-spec-value">${s.value}</div></div>`
  ).join('');

  // Units
  const statusMap = {'可售':'available','保留中':'reserved','稀缺戶':'rare','僅剩2戶':'rare','預售中':'reserved','預約看屋':'rare'};
  document.getElementById('pdUnits').innerHTML = d.units.map(u =>
    `<div class="pd-unit-card">
      <div class="pd-unit-type">${u.type}</div>
      <div class="pd-unit-area">${u.area}</div>
      <div class="pd-unit-price">${u.price}</div>
      <span class="pd-unit-status ${statusMap[u.status]||'available'}">${u.status}</span>
    </div>`
  ).join('');

  // Transport
  document.getElementById('pdTransport').innerHTML = d.transport.map(t =>
    `<li class="pd-transport-item">${t}</li>`
  ).join('');

  // Amenities
  document.getElementById('pdAmenities').innerHTML = d.amenities.map(a =>
    `<span class="pd-amenity-tag">${a}</span>`
  ).join('');

  // Show overlay
  const overlay = document.getElementById('projDetailOverlay');
  overlay.style.display = 'block';
  overlay.scrollTop = 0;
  document.body.style.overflow = 'hidden';

  // Also pre-fill project in booking overlay
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
}

function closeProjDetail() {
  document.getElementById('projDetailOverlay').style.display = 'none';
  document.body.style.overflow = '';
}

// Close on Escape
document.addEventListener('keydown', function(e) {
  if (e.key === 'Escape') {
    if (document.getElementById('projDetailOverlay').style.display !== 'none') {
      closeProjDetail();
    }
  }
});
"""

script_end = html.rfind('</script>', 0, html.rfind('</body>'))
html = html[:script_end] + '\n' + PROJECT_DETAIL_JS + '\n' + html[script_end:]
print("3. JS:", "OK")

# ── 5. WIRE UP 查看建案 BUTTONS ────────────────────────────────────────────────
projects = [
    ('譽誠沐光苑', 'btn btn-primary">查看建案'),
    ('譽誠和風居', 'btn btn-primary">查看建案'),
    ('譽誠晴山苑', 'btn btn-primary">查看建案'),
    ('譽誠星曜',   'btn btn-primary">查看建案'),
    ('譽誠綠意村', 'btn btn-primary">查看建案'),
]

# Replace each <a href="#" class="btn btn-primary">查看建案</a> by finding project name nearby
for name in ['譽誠沐光苑','譽誠和風居','譽誠晴山苑','譽誠星曜','譽誠綠意村']:
    # Find the project-card block containing this name, then replace its 查看建案 href
    old_btn = f'class="project-name">{name}</div>'
    # Find position of this name in html
    idx = html.find(old_btn)
    if idx < 0:
        print(f"  MISS: {name}")
        continue
    # Now find the next 查看建案 link after this position
    btn_old = '<a href="#" class="btn btn-primary">查看建案</a>'
    btn_new = f'<a href="#" onclick="openProjDetail(\'{name}\');return false;" class="btn btn-primary">查看建案</a>'
    # Replace only the first occurrence after idx
    pos = html.find(btn_old, idx)
    if pos >= 0:
        html = html[:pos] + btn_new + html[pos+len(btn_old):]
        print(f"  Wired: {name}")
    else:
        print(f"  MISS btn: {name}")

print("4. Buttons wired: Done")

# Save
with open('C:/Users/ROG/yuchen-website/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("\nDone! Project detail overlay complete.")
