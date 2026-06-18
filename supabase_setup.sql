-- 譽誠聯合銷售平台 V2 — Supabase 資料庫建立腳本
-- 在 Supabase → SQL Editor 執行此檔案

-- ══ 1. 仲介申請表（不用 Auth，簡單帳號密碼）══
CREATE TABLE IF NOT EXISTS brokers (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  company TEXT NOT NULL,
  phone TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  status TEXT DEFAULT 'pending',  -- pending / active / suspended
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ══ 2. 客戶報備表 ══
CREATE TABLE IF NOT EXISTS client_registrations (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  registration_no TEXT UNIQUE NOT NULL,
  broker_id UUID REFERENCES brokers(id),
  broker_name TEXT,
  broker_company TEXT,
  project_name TEXT NOT NULL,
  client_name TEXT NOT NULL,
  client_phone TEXT NOT NULL,
  note TEXT,
  status TEXT DEFAULT 'pending',  -- pending / confirmed / closed
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ══ 3. 預約帶看表 ══
CREATE TABLE IF NOT EXISTS bookings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  project_name TEXT NOT NULL,
  client_name TEXT NOT NULL,
  client_phone TEXT NOT NULL,
  booking_date DATE,
  time_slot TEXT,
  broker_id UUID REFERENCES brokers(id),
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ══ 4. 案件詢問表 ══
CREATE TABLE IF NOT EXISTS inquiries (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  project_name TEXT,
  name TEXT NOT NULL,
  phone TEXT NOT NULL,
  content TEXT,
  status TEXT DEFAULT 'new',
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ══ RLS 政策（Row Level Security）══

-- brokers: 只能讀自己的資料
ALTER TABLE brokers ENABLE ROW LEVEL SECURITY;
CREATE POLICY "brokers_select_own" ON brokers FOR SELECT USING (true);
CREATE POLICY "brokers_insert" ON brokers FOR INSERT WITH CHECK (true);

-- client_registrations: 仲介只能看自己的報備
ALTER TABLE client_registrations ENABLE ROW LEVEL SECURITY;
CREATE POLICY "reg_insert" ON client_registrations FOR INSERT WITH CHECK (true);
CREATE POLICY "reg_select_all" ON client_registrations FOR SELECT USING (true);

-- bookings: 開放新增與讀取
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
CREATE POLICY "booking_insert" ON bookings FOR INSERT WITH CHECK (true);
CREATE POLICY "booking_select" ON bookings FOR SELECT USING (true);

-- inquiries: 開放新增
ALTER TABLE inquiries ENABLE ROW LEVEL SECURITY;
CREATE POLICY "inquiry_insert" ON inquiries FOR INSERT WITH CHECK (true);
CREATE POLICY "inquiry_select" ON inquiries FOR SELECT USING (true);
