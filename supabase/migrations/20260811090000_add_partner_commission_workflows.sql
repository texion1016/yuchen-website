-- Partner portals, reviewed sales, and immutable estimated-commission snapshots.
-- All money values are stored in TWD without tax; invoice and settlement workflows
-- are intentionally out of scope for this migration.

alter type public.platform_role add value if not exists 'regional_agent';
alter type public.platform_role add value if not exists 'sourcing_partner';

create table if not exists public.platform_partners (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null unique references auth.users(id) on delete cascade,
  role text not null check (role in ('regional_agent', 'sourcing_partner')),
  display_name text not null,
  phone text,
  region text,
  status text not null default 'active' check (status in ('active', 'suspended')),
  invited_by uuid not null references auth.users(id) on delete restrict,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.projects
  add column if not exists approval_status text not null default 'approved'
    check (approval_status in ('pending', 'approved', 'rejected')),
  add column if not exists submitted_by uuid references auth.users(id) on delete set null,
  add column if not exists regional_agent_user_id uuid references auth.users(id) on delete set null,
  add column if not exists sourcing_partner_user_id uuid references auth.users(id) on delete set null,
  add column if not exists region text,
  add column if not exists platform_commission_rate numeric(5,2) not null default 0
    check (platform_commission_rate between 0 and 100),
  add column if not exists regional_agent_rate numeric(5,2) not null default 0
    check (regional_agent_rate between 0 and 100),
  add column if not exists sourcing_partner_rate numeric(5,2) not null default 0
    check (sourcing_partner_rate between 0 and 100),
  add column if not exists approval_note text,
  add column if not exists approved_by uuid references auth.users(id) on delete set null,
  add column if not exists approved_at timestamptz;

alter table public.broker_companies
  add column if not exists partner_tier text not null default 'standard'
    check (partner_tier in ('standard', 'silver', 'gold', 'platinum', 'diamond')),
  add column if not exists broker_share_rate numeric(5,2) not null default 50
    check (broker_share_rate between 0 and 100);

update public.broker_companies
set broker_share_rate = case partner_tier
  when 'silver' then 53
  when 'gold' then 55
  when 'platinum' then 57
  when 'diamond' then 60
  else 50
end
where broker_share_rate is null or broker_share_rate = 50;

update public.projects
set approval_status = 'approved'
where approval_status is null;

create index if not exists projects_regional_agent_idx
  on public.projects(regional_agent_user_id, approval_status);
create index if not exists projects_sourcing_partner_idx
  on public.projects(sourcing_partner_user_id, approval_status);
create index if not exists projects_approval_status_idx
  on public.projects(approval_status, created_at desc);

create table if not exists public.sale_submissions (
  id uuid primary key default gen_random_uuid(),
  project_id uuid not null references public.projects(id) on delete restrict,
  unit_id uuid not null references public.units(id) on delete restrict,
  broker_id uuid not null references public.brokers(id) on delete restrict,
  broker_company_id uuid not null references public.broker_companies(id) on delete restrict,
  submitted_by uuid not null references auth.users(id) on delete restrict,
  deal_price numeric(14,0) not null check (deal_price > 0),
  deal_date date not null,
  note text,
  status text not null default 'pending' check (status in ('pending', 'approved', 'rejected')),
  reviewed_by uuid references auth.users(id) on delete set null,
  reviewed_at timestamptz,
  review_note text,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create unique index if not exists sale_submissions_one_active_per_unit_idx
  on public.sale_submissions(unit_id)
  where status in ('pending', 'approved');
create index if not exists sale_submissions_project_status_idx
  on public.sale_submissions(project_id, status, deal_date desc);
create index if not exists sale_submissions_company_status_idx
  on public.sale_submissions(broker_company_id, status, deal_date desc);

create table if not exists public.commission_allocations (
  id uuid primary key default gen_random_uuid(),
  sale_submission_id uuid not null references public.sale_submissions(id) on delete restrict,
  project_id uuid not null references public.projects(id) on delete restrict,
  unit_id uuid not null references public.units(id) on delete restrict,
  allocation_role text not null check (allocation_role in ('broker_company', 'regional_agent', 'sourcing_partner', 'platform')),
  recipient_user_id uuid references auth.users(id) on delete set null,
  recipient_company_id uuid references public.broker_companies(id) on delete set null,
  recipient_name text not null,
  commission_base_amount numeric(14,0) not null check (commission_base_amount >= 0),
  share_rate numeric(5,2) not null check (share_rate between 0 and 100),
  estimated_amount numeric(14,0) not null check (estimated_amount >= 0),
  created_at timestamptz not null default now(),
  unique (sale_submission_id, allocation_role)
);

create index if not exists commission_allocations_recipient_user_idx
  on public.commission_allocations(recipient_user_id, created_at desc);
create index if not exists commission_allocations_recipient_company_idx
  on public.commission_allocations(recipient_company_id, created_at desc);
create index if not exists commission_allocations_project_idx
  on public.commission_allocations(project_id, created_at desc);

alter table public.platform_partners enable row level security;
alter table public.sale_submissions enable row level security;
alter table public.commission_allocations enable row level security;

create or replace function private.is_regional_agent()
returns boolean
language sql
stable
security definer
set search_path = public, private, auth, pg_temp
as $$
  select exists (
    select 1 from public.platform_partners
    where user_id = (select auth.uid())
      and role = 'regional_agent'
      and status = 'active'
  );
$$;

create or replace function private.is_sourcing_partner()
returns boolean
language sql
stable
security definer
set search_path = public, private, auth, pg_temp
as $$
  select exists (
    select 1 from public.platform_partners
    where user_id = (select auth.uid())
      and role = 'sourcing_partner'
      and status = 'active'
  );
$$;

revoke all on function private.is_regional_agent() from public, anon;
revoke all on function private.is_sourcing_partner() from public, anon;
grant usage on schema private to authenticated;
grant execute on function private.is_regional_agent() to authenticated;
grant execute on function private.is_sourcing_partner() to authenticated;

drop policy if exists "platform partners administrators manage" on public.platform_partners;
drop policy if exists "platform partners read own profile" on public.platform_partners;
create policy "platform partners administrators manage"
  on public.platform_partners for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));
create policy "platform partners read own profile"
  on public.platform_partners for select to authenticated
  using (user_id = (select auth.uid()));

drop policy if exists "projects regional agents read assigned" on public.projects;
drop policy if exists "projects sourcing partners read assigned" on public.projects;
drop policy if exists "projects regional agents submit pending" on public.projects;
create policy "projects regional agents read assigned"
  on public.projects for select to authenticated
  using (regional_agent_user_id = (select auth.uid()) or submitted_by = (select auth.uid()));
create policy "projects sourcing partners read assigned"
  on public.projects for select to authenticated
  using (sourcing_partner_user_id = (select auth.uid()));
create policy "projects regional agents submit pending"
  on public.projects for insert to authenticated
  with check (
    (select private.is_regional_agent())
    and submitted_by = (select auth.uid())
    and regional_agent_user_id = (select auth.uid())
    and approval_status = 'pending'
    and published is false
  );

drop policy if exists "units regional agents read assigned" on public.units;
drop policy if exists "units sourcing partners read assigned" on public.units;
create policy "units regional agents read assigned"
  on public.units for select to authenticated
  using (exists (
    select 1 from public.projects p
    where p.name = public.units.project_name
      and p.regional_agent_user_id = (select auth.uid())
  ));
create policy "units sourcing partners read assigned"
  on public.units for select to authenticated
  using (exists (
    select 1 from public.projects p
    where p.name = public.units.project_name
      and p.sourcing_partner_user_id = (select auth.uid())
  ));

create or replace function private.validate_sale_submission()
returns trigger
language plpgsql
security definer
set search_path = public, private, pg_temp
as $$
declare
  unit_project_name text;
  mapped_project_id uuid;
begin
  select u.project_name into unit_project_name
  from public.units u where u.id = new.unit_id;
  select p.id into mapped_project_id
  from public.projects p where p.name = unit_project_name;
  if unit_project_name is null or mapped_project_id is null or mapped_project_id <> new.project_id then
    raise exception 'The selected unit does not belong to the selected project';
  end if;
  if exists (select 1 from public.units where id = new.unit_id and status = 'sold') then
    raise exception 'This unit is already marked as sold';
  end if;
  return new;
end;
$$;

revoke all on function private.validate_sale_submission() from public, anon, authenticated;

drop trigger if exists validate_sale_submission_before_write on public.sale_submissions;
create trigger validate_sale_submission_before_write
  before insert or update of project_id, unit_id on public.sale_submissions
  for each row execute function private.validate_sale_submission();

drop policy if exists "sale submissions administrators manage" on public.sale_submissions;
drop policy if exists "sale submissions brokers read scoped" on public.sale_submissions;
drop policy if exists "sale submissions brokers submit own" on public.sale_submissions;
drop policy if exists "sale submissions regional agents read assigned" on public.sale_submissions;
drop policy if exists "sale submissions sourcing partners read assigned" on public.sale_submissions;
create policy "sale submissions administrators manage"
  on public.sale_submissions for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));
create policy "sale submissions brokers read scoped"
  on public.sale_submissions for select to authenticated
  using (
    submitted_by = (select auth.uid())
    or (broker_company_id = (select private.current_broker_company_id())
        and (select private.is_broker_company_manager(broker_company_id)))
  );
create policy "sale submissions brokers submit own"
  on public.sale_submissions for insert to authenticated
  with check (
    broker_id = (select private.current_broker_id())
    and broker_company_id = (select private.current_broker_company_id())
    and submitted_by = (select auth.uid())
    and status = 'pending'
  );
create policy "sale submissions regional agents read assigned"
  on public.sale_submissions for select to authenticated
  using (exists (
    select 1 from public.projects p
    where p.id = public.sale_submissions.project_id
      and p.regional_agent_user_id = (select auth.uid())
  ));
create policy "sale submissions sourcing partners read assigned"
  on public.sale_submissions for select to authenticated
  using (exists (
    select 1 from public.projects p
    where p.id = public.sale_submissions.project_id
      and p.sourcing_partner_user_id = (select auth.uid())
  ));

create or replace function private.create_commission_allocations()
returns trigger
language plpgsql
security definer
set search_path = public, private, pg_temp
as $$
declare
  project_row public.projects%rowtype;
  company_row public.broker_companies%rowtype;
  regional_name text;
  sourcing_name text;
  gross_amount numeric(14,0);
  broker_amount numeric(14,0);
  regional_amount numeric(14,0) := 0;
  sourcing_amount numeric(14,0) := 0;
  platform_amount numeric(14,0);
begin
  if new.status <> 'approved' or (tg_op = 'UPDATE' and old.status = 'approved') then
    return new;
  end if;

  select * into project_row from public.projects where id = new.project_id;
  select * into company_row from public.broker_companies where id = new.broker_company_id;
  if project_row.approval_status <> 'approved' then
    raise exception 'The project must be approved before a sale can be approved';
  end if;
  if project_row.platform_commission_rate <= 0 then
    raise exception 'The project needs a platform commission rate before this sale can be approved';
  end if;
  if company_row.broker_share_rate is null then
    raise exception 'The broker company needs a commission share rate before this sale can be approved';
  end if;

  gross_amount := round(new.deal_price * project_row.platform_commission_rate / 100, 0);
  broker_amount := round(gross_amount * company_row.broker_share_rate / 100, 0);
  if project_row.regional_agent_user_id is not null then
    select display_name into regional_name from public.platform_partners where user_id = project_row.regional_agent_user_id;
    regional_amount := round(gross_amount * project_row.regional_agent_rate / 100, 0);
  end if;
  if project_row.sourcing_partner_user_id is not null then
    select display_name into sourcing_name from public.platform_partners where user_id = project_row.sourcing_partner_user_id;
    sourcing_amount := round(gross_amount * project_row.sourcing_partner_rate / 100, 0);
  end if;
  platform_amount := gross_amount - broker_amount - regional_amount - sourcing_amount;
  if platform_amount < 0 then
    raise exception 'Partner share rates exceed the platform commission';
  end if;

  insert into public.commission_allocations (
    sale_submission_id, project_id, unit_id, allocation_role, recipient_company_id,
    recipient_name, commission_base_amount, share_rate, estimated_amount
  ) values (
    new.id, new.project_id, new.unit_id, 'broker_company', new.broker_company_id,
    company_row.display_name, gross_amount, company_row.broker_share_rate, broker_amount
  );
  if project_row.regional_agent_user_id is not null then
    insert into public.commission_allocations (
      sale_submission_id, project_id, unit_id, allocation_role, recipient_user_id,
      recipient_name, commission_base_amount, share_rate, estimated_amount
    ) values (
      new.id, new.project_id, new.unit_id, 'regional_agent', project_row.regional_agent_user_id,
      coalesce(regional_name, '區代夥伴'), gross_amount, project_row.regional_agent_rate, regional_amount
    );
  end if;
  if project_row.sourcing_partner_user_id is not null then
    insert into public.commission_allocations (
      sale_submission_id, project_id, unit_id, allocation_role, recipient_user_id,
      recipient_name, commission_base_amount, share_rate, estimated_amount
    ) values (
      new.id, new.project_id, new.unit_id, 'sourcing_partner', project_row.sourcing_partner_user_id,
      coalesce(sourcing_name, '拓案夥伴'), gross_amount, project_row.sourcing_partner_rate, sourcing_amount
    );
  end if;
  insert into public.commission_allocations (
    sale_submission_id, project_id, unit_id, allocation_role,
    recipient_name, commission_base_amount, share_rate, estimated_amount
  ) values (
    new.id, new.project_id, new.unit_id, 'platform',
    '譽誠聯合銷售平台', gross_amount,
    round(platform_amount * 100 / nullif(gross_amount, 0), 2), platform_amount
  );

  update public.units set status = 'sold', updated_at = now() where id = new.unit_id;
  insert into public.unit_deals (unit_id, stage, deal_price, deal_date)
  select new.unit_id, '簽約完成', trim(to_char(new.deal_price, 'FM999,999,999,999')), new.deal_date
  where not exists (select 1 from public.unit_deals where unit_id = new.unit_id and deal_date = new.deal_date);
  return new;
end;
$$;

revoke all on function private.create_commission_allocations() from public, anon, authenticated;

drop trigger if exists create_commission_allocations_after_approval on public.sale_submissions;
create trigger create_commission_allocations_after_approval
  after insert or update of status on public.sale_submissions
  for each row execute function private.create_commission_allocations();

drop policy if exists "commission allocations administrators manage" on public.commission_allocations;
drop policy if exists "commission allocations broker company read own" on public.commission_allocations;
drop policy if exists "commission allocations regional agents read own" on public.commission_allocations;
drop policy if exists "commission allocations sourcing partners read own" on public.commission_allocations;
create policy "commission allocations administrators manage"
  on public.commission_allocations for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));
create policy "commission allocations broker company read own"
  on public.commission_allocations for select to authenticated
  using (
    allocation_role = 'broker_company'
    and recipient_company_id = (select private.current_broker_company_id())
    and (select private.is_broker_company_manager(recipient_company_id))
  );
create policy "commission allocations regional agents read own"
  on public.commission_allocations for select to authenticated
  using (allocation_role = 'regional_agent' and recipient_user_id = (select auth.uid()));
create policy "commission allocations sourcing partners read own"
  on public.commission_allocations for select to authenticated
  using (allocation_role = 'sourcing_partner' and recipient_user_id = (select auth.uid()));

grant select, insert on public.platform_partners to authenticated;
grant select, insert, update on public.sale_submissions to authenticated;
grant select on public.commission_allocations to authenticated;
grant all on public.platform_partners, public.sale_submissions, public.commission_allocations to service_role;
