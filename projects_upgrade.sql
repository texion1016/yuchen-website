-- ═══════════════════════════════════════════════════════════════
-- 建案管理擴充：新增 13 個細節欄位 + 為原五案補示範資料
-- 貼進 Supabase SQL Editor 執行一次即可。
-- 執行後：後台「新增/編輯建案」的建築團隊、公設比、車位、管理費、
--         可售格局、社區公設、學區、影片、地圖等欄位才能儲存；
--         官網詳情頁會自動多出對應區塊（沒填的不顯示）。
-- 注意：重跑會覆蓋原五案的示範欄位，不影響你自己新增的建案。
-- ═══════════════════════════════════════════════════════════════

alter table projects
  add column if not exists builder text,        -- 投資建設
  add column if not exists construction text,   -- 營造公司
  add column if not exists architect text,      -- 建築設計
  add column if not exists permit text,         -- 建照號碼
  add column if not exists handover text,       -- 預計交屋
  add column if not exists public_ratio text,   -- 公設比
  add column if not exists parking text,        -- 車位規劃
  add column if not exists mgmt_fee text,       -- 管理費
  add column if not exists units_info text,     -- 可售格局，每行「格局|坪數|總價|狀態」
  add column if not exists facilities text,     -- 社區公設，每行一項
  add column if not exists schools text,        -- 學區，每行一項
  add column if not exists video_url text,      -- 建案影片連結（YouTube）
  add column if not exists map_url text;        -- Google 地圖連結（留空自動用地址）

-- ── 原五案示範資料 ──────────────────────────────────────────────

update projects set
  builder='譽誠建設開發', construction='誠峰營造', architect='尚禾建築師事務所',
  permit='(113)桃市都建字第0888號', handover='2026年Q4',
  public_ratio='32.5%', parking='坡道平面 96 席，另計 138–150 萬', mgmt_fee='每坪 85 元/月',
  facilities=E'迎賓大廳\n健身房\n交誼廳\n兒童遊戲區\n閱覽室\n空中花園',
  schools=E'中壢國小（步行6分鐘）\n中壢國中（步行10分鐘）\n中壢高中'
where name='譽誠沐光苑';

update projects set
  builder='譽誠建設開發', construction='和築營造', architect='隱岳建築師事務所',
  permit='(112)新北建字第1206號', handover='已完工，隨時交屋',
  public_ratio='33.8%', parking='坡道平面 82 席，另計 150–168 萬', mgmt_fee='每坪 92 元/月',
  facilities=E'日式枯山水中庭\n茶道室\n健身房\n空中花園\n宴會交誼廳\n視聽室',
  schools=E'新莊國小（步行5分鐘）\n新莊國中（步行8分鐘）\n輔仁大學'
where name='譽誠和風居';

update projects set
  builder='譽誠建設開發', construction='磐岩營造', architect='山隱建築師事務所',
  permit='(113)中市都建字第0666號', handover='2026年Q2 完工交屋',
  public_ratio='34.2%', parking='坡道平面 108 席，另計 180–220 萬', mgmt_fee='每坪 98 元/月',
  facilities=E'無邊際泳池\n景觀健身房\n宴會廳\n瑜珈教室\n媽媽教室\n高空觀景酒吧',
  schools=E'惠來國小\n至善國中\n逢甲大學'
where name='譽誠晴山苑';

update projects set
  builder='譽誠建設開發', construction='鼎峙營造', architect='曜岳國際建築師事務所',
  permit='(111)北市都建字第2088號', handover='已完工，全裝修交屋',
  public_ratio='35.6%', parking='坡道平面 152 席，另計 250–320 萬', mgmt_fee='每坪 120 元/月',
  facilities=E'空中泳池\n私人影音劇院\n行政酒廊\n健身中心\n溫水SPA\n飯店式管家櫃台',
  schools=E'西湖國小（步行4分鐘）\n麗山國中\n德明財經科技大學'
where name='譽誠星曜';

update projects set
  builder='譽誠建設開發', construction='永築營造', architect='綠邦建築師事務所',
  permit='(113)竹縣建字第0321號', handover='2027年Q1',
  public_ratio='31.2%', parking='坡道平面 196 席，另計 120–140 萬', mgmt_fee='每坪 75 元/月',
  facilities=E'生態中庭花園\n太陽能公共電力\n健身房\n親子共讀室\n洗衣代收站\n雨水回收澆灌系統',
  schools=E'東興國小（步行7分鐘）\n東興國中\n新竹縣實驗中學'
where name='譽誠綠意村';

-- 驗證： select name, builder, public_ratio, parking from projects order by sort;
