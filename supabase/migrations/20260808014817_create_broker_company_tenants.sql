-- Broker companies are tenants. Platform administrators manage companies;
-- company owners/managers manage members only within their own company.

create table if not exists public.broker_companies (
  id uuid primary key default gen_random_uuid(),
  legal_name text not null,
  display_name text not null,
  tax_id text,
  contact_name text not null,
  contact_phone text not null,
  status text not null default 'active'
    check (status in ('active', 'suspended', 'ended')),
  created_by uuid not null references auth.users(id) on delete restrict,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (legal_name),
  unique (tax_id)
);

create table if not exists public.broker_company_members (
  id uuid primary key default gen_random_uuid(),
  company_id uuid not null references public.broker_companies(id) on delete cascade,
  user_id uuid not null references auth.users(id) on delete cascade,
  broker_id uuid not null references public.brokers(id) on delete restrict,
  member_role text not null check (member_role in ('owner', 'manager', 'agent')),
  status text not null default 'active' check (status in ('active', 'suspended')),
  invited_by uuid not null references auth.users(id) on delete restrict,
  joined_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (company_id, user_id),
  unique (broker_id)
);

create index if not exists broker_company_members_user_active_idx
  on public.broker_company_members(user_id, company_id)
  where status = 'active';

alter table public.client_registrations
  add column if not exists broker_company_id uuid
  references public.broker_companies(id) on delete restrict;

create index if not exists client_registrations_broker_company_created_idx
  on public.client_registrations(broker_company_id, created_at desc);

alter table public.broker_companies enable row level security;
alter table public.broker_company_members enable row level security;

create or replace function private.current_broker_company_id()
returns uuid
language sql
stable
security definer
set search_path = public, private, auth, pg_temp
as $$
  select company_id
  from public.broker_company_members
  where user_id = (select auth.uid())
    and status = 'active'
  limit 1;
$$;

create or replace function private.is_broker_company_manager(target_company_id uuid)
returns boolean
language sql
stable
security definer
set search_path = public, private, auth, pg_temp
as $$
  select exists (
    select 1
    from public.broker_company_members
    where company_id = target_company_id
      and user_id = (select auth.uid())
      and status = 'active'
      and member_role in ('owner', 'manager')
  );
$$;

revoke all on function private.current_broker_company_id() from public, anon;
revoke all on function private.is_broker_company_manager(uuid) from public, anon;
grant usage on schema private to authenticated;
grant execute on function private.current_broker_company_id() to authenticated;
grant execute on function private.is_broker_company_manager(uuid) to authenticated;

drop policy if exists "broker companies administrators manage" on public.broker_companies;
drop policy if exists "broker companies members read own company" on public.broker_companies;
create policy "broker companies administrators manage"
  on public.broker_companies for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));
create policy "broker companies members read own company"
  on public.broker_companies for select to authenticated
  using (id = (select private.current_broker_company_id()));

drop policy if exists "broker company members administrators manage" on public.broker_company_members;
drop policy if exists "broker company members read same company" on public.broker_company_members;
create policy "broker company members administrators manage"
  on public.broker_company_members for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));
create policy "broker company members read same company"
  on public.broker_company_members for select to authenticated
  using (company_id = (select private.current_broker_company_id()));

drop policy if exists "brokers company managers read team" on public.brokers;
create policy "brokers company managers read team"
  on public.brokers for select to authenticated
  using (exists (
    select 1
    from public.broker_company_members member
    where member.broker_id = public.brokers.id
      and (select private.is_broker_company_manager(member.company_id))
  ));

revoke all on public.broker_companies, public.broker_company_members from anon;
revoke insert, update, delete on public.broker_companies, public.broker_company_members from authenticated;
grant select on public.broker_companies, public.broker_company_members to authenticated;
grant all on public.broker_companies, public.broker_company_members to service_role;

-- New broker reports are irrevocably tied to the writer's company. Company
-- managers can read their company's work; agents keep access to their own work.
drop policy if exists "registrations broker read own" on public.client_registrations;
drop policy if exists "registrations broker submit" on public.client_registrations;
create policy "registrations broker company read scoped"
  on public.client_registrations for select to authenticated
  using (
    broker_id = (select private.current_broker_id())
    or (broker_company_id is not null and (select private.is_broker_company_manager(broker_company_id)))
  );
create policy "registrations broker submit to own company"
  on public.client_registrations for insert to authenticated
  with check (
    broker_id = (select private.current_broker_id())
    and broker_company_id = (select private.current_broker_company_id())
  );

-- Public self-application is retired. New broker identities are created only
-- by the platform administrator or an active company owner/manager invitation.
drop trigger if exists on_auth_user_created_broker on auth.users;

grant select, insert on public.client_registrations to authenticated;
