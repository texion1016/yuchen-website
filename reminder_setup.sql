-- ═══════════════════════════════════════════════════════════════
-- 帶看前 24 小時 Email 提醒系統
-- 原理：pg_cron 每分鐘檢查一次，帶看時間進入 24 小時窗口的報備
--       透過 pg_net 呼叫 Brevo API 寄信給報備仲介，寄過就標記。
-- 使用：把下面的 BREVO_API_KEY_HERE 換成你的 Brevo API 金鑰
--       （Brevo → SMTP & API → 「API Keys」頁籤 → Generate，
--         注意是 xkeysib- 開頭的 API key，不是 SMTP key！）
--       然後整段貼進 Supabase SQL Editor 執行一次。
-- ═══════════════════════════════════════════════════════════════

-- 1) 啟用擴充功能（已啟用會自動跳過）
create extension if not exists pg_cron;
create extension if not exists pg_net;

-- 2) 加「已提醒」標記欄位
alter table client_registrations
  add column if not exists reminder_sent boolean not null default false;

-- 3) 檢查並寄送提醒的函式
create or replace function public.send_view_reminders()
returns void
language plpgsql
security definer
set search_path = public
as $$
declare
  r record;
  v_ts timestamptz;
begin
  for r in
    select cr.id, cr.registration_no, cr.broker_name, cr.project_name,
           cr.client_name, cr.client_phone, cr.view_date, cr.view_time,
           b.email as broker_email
    from client_registrations cr
    left join brokers b
      on (cr.broker_id is not null and b.id = cr.broker_id)
      or (cr.broker_id is null and b.name = cr.broker_name and b.company = cr.broker_company)
    where cr.reminder_sent = false
      and cr.view_date is not null
      and cr.view_time is not null
      and cr.status <> 'closed'
  loop
    -- 帶看時間（台灣時區）
    v_ts := (r.view_date::text || ' ' || r.view_time)::timestamp
            at time zone 'Asia/Taipei';

    -- 進入「距帶看 ≤ 24 小時」窗口且還沒過期
    if v_ts <= now() + interval '24 hours' and v_ts > now() then
      if r.broker_email is not null then
        perform net.http_post(
          url     := 'https://api.brevo.com/v3/smtp/email',
          headers := jsonb_build_object(
            'api-key',      'BREVO_API_KEY_HERE',
            'Content-Type', 'application/json'
          ),
          body := jsonb_build_object(
            'sender', jsonb_build_object(
              'name',  '譽誠聯合銷售平台',
              'email', 'yuchen.web.service@gmail.com'
            ),
            'to', jsonb_build_array(
              jsonb_build_object('email', r.broker_email, 'name', r.broker_name)
            ),
            'subject', '帶看提醒｜明天 ' || r.view_time || ' ' || r.project_name,
            'htmlContent',
              '<h2>帶看提醒</h2>'
              || '<p>' || r.broker_name || ' 您好，提醒您在 24 小時後有一場帶看：</p>'
              || '<ul>'
              || '<li><b>建案：</b>' || r.project_name || '</li>'
              || '<li><b>時間：</b>' || r.view_date::text || ' ' || r.view_time || '</li>'
              || '<li><b>客戶：</b>' || r.client_name || '（' || r.client_phone || '）</li>'
              || '<li><b>報備編號：</b>' || r.registration_no || '</li>'
              || '</ul>'
              || '<p>— 譽誠聯合銷售平台</p>'
          )
        );
      end if;
      -- 無論有沒有信箱都標記，避免每分鐘重試
      update client_registrations set reminder_sent = true where id = r.id;
    end if;
  end loop;
end;
$$;

-- 4) 排程：每分鐘檢查一次（誤差最多 1 分鐘）
select cron.schedule(
  'view-reminders',
  '* * * * *',
  'select public.send_view_reminders()'
);

-- ═══════════════════════════════════════════════════════════════
-- 測試用（可選）：
--   手動跑一次檢查：  select public.send_view_reminders();
--   看排程狀態：      select * from cron.job;
--   看寄信請求記錄：  select * from net._http_response order by id desc limit 5;
--   停用排程：        select cron.unschedule('view-reminders');
-- ═══════════════════════════════════════════════════════════════
