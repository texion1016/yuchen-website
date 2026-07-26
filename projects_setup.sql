-- ═══════════════════════════════════════════════════════════════
-- 建案管理系統：projects 表 + project-images 圖片儲存桶
-- 貼進 Supabase SQL Editor 執行一次。
-- 執行後：管理後台「建案管理」可新增/編輯/刊登/下架/刪除建案並上傳圖片，
--         主頁建案區與報備下拉自動改讀資料庫（讀不到自動退回內建五案）。
-- ═══════════════════════════════════════════════════════════════

create table if not exists projects (
  id uuid primary key default gen_random_uuid(),
  name text not null unique,          -- 建案名稱
  location text,                      -- 地區（桃園市中壢區）
  address text,                       -- 詳細地址
  price text,                         -- 價格數字（萬起），如 988
  price_note text,                    -- 價格備註（附基本輕裝修…）
  tag text,                           -- 卡片標籤（新上架/熱銷中…）
  tag_hot boolean default false,      -- 金色標籤
  badges text,                        -- 房型徽章，逗號分隔（2-3 房,輕裝修）
  description text,                   -- 建案說明
  specs text,                         -- 規格，每行「標籤|內容」
  transport text,                     -- 交通，每行一項
  amenities text,                     -- 生活機能，每行一項
  images jsonb default '[]'::jsonb,   -- 圖片網址陣列（最多 15，第 1 張為封面）
  published boolean default true,     -- 刊登中
  sort int default 100,               -- 排序（小的在前）
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

alter table projects enable row level security;
drop policy if exists "projects all" on projects;
create policy "projects all" on projects for all using (true) with check (true);
grant select, insert, update, delete on projects to anon, authenticated;

-- 圖片儲存桶（公開讀取）
insert into storage.buckets (id, name, public)
values ('project-images', 'project-images', true)
on conflict (id) do nothing;

drop policy if exists "pimg read" on storage.objects;
create policy "pimg read" on storage.objects
  for select using (bucket_id = 'project-images');
drop policy if exists "pimg insert" on storage.objects;
create policy "pimg insert" on storage.objects
  for insert with check (bucket_id = 'project-images');
drop policy if exists "pimg delete" on storage.objects;
create policy "pimg delete" on storage.objects
  for delete using (bucket_id = 'project-images');

-- 驗證： select * from projects;
