-- ═══════════════════════════════════════════════════════════════
-- 戶況系統：units（戶別狀態表）+ unit_deals（成交／付定資訊表）
-- 貼進 Supabase SQL Editor 執行一次即可。
-- 執行後：管理後台「戶況管理」可改每戶狀態並登錄成交／付定資訊，
--         建商專區立體圖與平面圖即時同步（示範資料自動停用）。
-- ═══════════════════════════════════════════════════════════════

-- 1) 戶別狀態表
create table if not exists units (
  id uuid primary key default gen_random_uuid(),
  project_name text not null,
  floor int not null,
  unit_no text not null,              -- '01'..'05'
  unit_type text,
  size text,
  list_price text,                    -- 開價（對外）
  floor_price text,                   -- 底價（建商協議價）
  status text not null default 'open',-- open未售 / view帶看 / hold已付定 / sold已成交
  view_time text,                     -- 帶看時間（選填）
  updated_at timestamptz default now(),
  unique (project_name, floor, unit_no)
);

-- 2) 成交／付定資訊表
create table if not exists unit_deals (
  id uuid primary key default gen_random_uuid(),
  unit_id uuid not null references units(id) on delete cascade,
  stage text,                         -- 已付定金 / 簽約完成 / 已撥款 / 已交屋 / 已退定
  deal_price text,                    -- 成交價
  deal_date date,                     -- 成交日期
  buyer_name text,                    -- 買方
  deposit_amount text,                -- 定金金額
  deposit_date date,                  -- 付定日期
  sign_due date,                      -- 預計簽約期限
  created_at timestamptz default now()
);

-- 3) 權限（與現行平台一致的開放策略）
alter table units enable row level security;
alter table unit_deals enable row level security;
drop policy if exists "units all" on units;
create policy "units all" on units for all using (true) with check (true);
drop policy if exists "deals all" on unit_deals;
create policy "deals all" on unit_deals for all using (true) with check (true);
grant select, insert, update, delete on units to anon, authenticated;
grant select, insert, update, delete on unit_deals to anon, authenticated;

-- 4) 種子資料：譽誠沐光苑（12 層 × 5 戶）
insert into units (project_name, floor, unit_no, unit_type, size, list_price, floor_price, status)
select '譽誠沐光苑', f.fl, u.no, u.t, u.sz, u.lp, u.fp, (f.sts)[u.idx]
from (values
  (1,  array['sold','sold','sold','sold','sold']),
  (2,  array['sold','sold','sold','view','sold']),
  (3,  array['sold','sold','open','sold','sold']),
  (4,  array['sold','view','sold','sold','open']),
  (5,  array['sold','sold','open','view','sold']),
  (6,  array['open','sold','sold','open','hold']),
  (7,  array['sold','open','view','sold','open']),
  (8,  array['open','sold','hold','open','sold']),
  (9,  array['hold','open','sold','open','open']),
  (10, array['open','open','view','open','sold']),
  (11, array['open','view','open','hold','open']),
  (12, array['open','open','open','open','view'])
) as f(fl, sts)
cross join (values
  (1, '01', '2房2廳1衛', '26.5坪', '988萬',   '938萬'),
  (2, '02', '2房2廳1衛', '28.5坪', '1,028萬', '978萬'),
  (3, '03', '3房2廳2衛', '34.0坪', '1,180萬', '1,120萬'),
  (4, '04', '3房2廳2衛', '35.5坪', '1,220萬', '1,158萬'),
  (5, '05', '2房1廳1衛', '22.0坪', '858萬',   '818萬')
) as u(idx, no, t, sz, lp, fp)
on conflict (project_name, floor, unit_no) do nothing;

-- 5) 種子資料：譽誠星曜（15 層 × 4 戶）
insert into units (project_name, floor, unit_no, unit_type, size, list_price, floor_price, status)
select '譽誠星曜', f.fl, u.no, u.t, u.sz, u.lp, u.fp, (f.sts)[u.idx]
from (values
  (1,  array['sold','sold','view','sold']),
  (2,  array['sold','view','sold','hold']),
  (3,  array['open','sold','open','sold']),
  (4,  array['view','hold','open','sold']),
  (5,  array['open','open','sold','open']),
  (6,  array['open','hold','open','open']),
  (7,  array['open','open','open','open']),
  (8,  array['open','open','view','open']),
  (9,  array['open','open','open','open']),
  (10, array['open','open','open','open']),
  (11, array['open','view','open','open']),
  (12, array['open','open','open','open']),
  (13, array['open','open','open','open']),
  (14, array['open','open','open','open']),
  (15, array['open','open','open','open'])
) as f(fl, sts)
cross join (values
  (1, '01', '3房2廳2衛', '42.5坪', '1,680萬', '1,598萬'),
  (2, '02', '2房2廳1衛', '30.5坪', '1,180萬', '1,120萬'),
  (3, '03', '2房2廳1衛', '30.8坪', '1,190萬', '1,130萬'),
  (4, '04', '3房2廳2衛', '40.0坪', '1,620萬', '1,540萬')
) as u(idx, no, t, sz, lp, fp)
on conflict (project_name, floor, unit_no) do nothing;

-- 6) 已成交戶補一筆基本成交紀錄（價格先帶開價，之後可在後台修正）
insert into unit_deals (unit_id, stage, deal_price, deal_date, buyer_name)
select id, '簽約完成', list_price,
       date '2026-01-10' + (row_number() over (order by project_name, floor, unit_no))::int * 5,
       '買方待補'
from units
where status = 'sold'
  and not exists (select 1 from unit_deals d where d.unit_id = units.id);

-- 7) 已付定戶補一筆付定紀錄（定金約開價 2%）
insert into unit_deals (unit_id, stage, deposit_amount, deposit_date, sign_due)
select id, '已付定金',
       round(regexp_replace(list_price, '\D', '', 'g')::int * 0.02) || '萬',
       date '2026-07-06', date '2026-07-20'
from units
where status = 'hold'
  and not exists (select 1 from unit_deals d where d.unit_id = units.id);

-- ═══════════════════════════════════════════════════════════════
-- 驗證：select project_name, status, count(*) from units group by 1,2 order by 1,2;
-- ═══════════════════════════════════════════════════════════════
