-- Give brokers and builders real Supabase Auth identities.  Roles are granted
-- server-side only: broker after admin activation, builder by an admin invite.

alter table public.brokers
  add column if not exists auth_user_id uuid references auth.users(id) on delete set null;

alter table public.brokers
  alter column password_hash drop not null;

create unique index if not exists brokers_auth_user_id_key
  on public.brokers(auth_user_id)
  where auth_user_id is not null;

create table if not exists public.builder_projects (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null references auth.users(id) on delete cascade,
  project_name text not null references public.projects(name) on update cascade on delete cascade,
  created_at timestamptz not null default now(),
  unique (user_id, project_name)
);

alter table public.builder_projects enable row level security;

create or replace function private.current_broker_id()
returns uuid
language sql
stable
security definer
set search_path = public, private, auth, pg_temp
as $$
  select id
  from public.brokers
  where auth_user_id = (select auth.uid())
    and status = 'active'
  limit 1;
$$;

revoke all on function private.current_broker_id() from public, anon;
grant usage on schema private to authenticated;
grant execute on function private.current_broker_id() to authenticated;

create or replace function private.create_broker_application()
returns trigger
language plpgsql
security definer
set search_path = public, private, auth, pg_temp
as $$
begin
  if coalesce(new.raw_user_meta_data ->> 'signup_type', '') = 'broker' then
    insert into public.brokers (auth_user_id, name, company, phone, email, license_no, status)
    values (
      new.id,
      left(coalesce(new.raw_user_meta_data ->> 'broker_name', ''), 100),
      left(coalesce(new.raw_user_meta_data ->> 'broker_company', ''), 150),
      left(coalesce(new.raw_user_meta_data ->> 'broker_phone', ''), 40),
      lower(new.email),
      left(coalesce(new.raw_user_meta_data ->> 'broker_license_no', ''), 80),
      'pending'
    )
    on conflict (email) do update
      set auth_user_id = excluded.auth_user_id;
  end if;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created_broker on auth.users;
create trigger on_auth_user_created_broker
  after insert on auth.users
  for each row execute procedure private.create_broker_application();

create or replace function private.sync_broker_access()
returns trigger
language plpgsql
security definer
set search_path = public, private, auth, pg_temp
as $$
begin
  if new.auth_user_id is null then
    return new;
  end if;

  if new.status = 'active' then
    insert into public.user_roles (user_id, role)
    values (new.auth_user_id, 'broker')
    on conflict (user_id) do update
      set role = excluded.role
      where public.user_roles.role <> 'admin';
  else
    delete from public.user_roles
      where user_id = new.auth_user_id
        and role = 'broker';
  end if;
  return new;
end;
$$;

drop trigger if exists on_broker_access_changed on public.brokers;
create trigger on_broker_access_changed
  after insert or update of auth_user_id, status on public.brokers
  for each row execute procedure private.sync_broker_access();

drop policy if exists "brokers public application" on public.brokers;
drop policy if exists "brokers administrators manage" on public.brokers;
drop policy if exists "brokers read own profile" on public.brokers;
create policy "brokers administrators manage"
  on public.brokers for all to authenticated
  using ((select private.is_admin())) with check ((select private.is_admin()));
create policy "brokers read own profile"
  on public.brokers for select to authenticated
  using (auth_user_id = (select auth.uid()));

drop policy if exists "registrations public submit" on public.client_registrations;
drop policy if exists "registrations administrators manage" on public.client_registrations;
drop policy if exists "registrations broker read own" on public.client_registrations;
drop policy if exists "registrations broker submit" on public.client_registrations;
drop policy if exists "registrations broker update own" on public.client_registrations;
create policy "registrations administrators manage"
  on public.client_registrations for all to authenticated
  using ((select private.is_admin())) with check ((select private.is_admin()));
create policy "registrations broker read own"
  on public.client_registrations for select to authenticated
  using (broker_id = (select private.current_broker_id()));
create policy "registrations broker submit"
  on public.client_registrations for insert to authenticated
  with check (broker_id = (select private.current_broker_id()));
create policy "registrations broker update own"
  on public.client_registrations for update to authenticated
  using (broker_id = (select private.current_broker_id()))
  with check (broker_id = (select private.current_broker_id()));

drop policy if exists "builder projects administrators manage" on public.builder_projects;
drop policy if exists "builder projects read own" on public.builder_projects;
create policy "builder projects administrators manage"
  on public.builder_projects for all to authenticated
  using ((select private.is_admin())) with check ((select private.is_admin()));
create policy "builder projects read own"
  on public.builder_projects for select to authenticated
  using (user_id = (select auth.uid()));

drop policy if exists "units builders read assigned" on public.units;
create policy "units builders read assigned"
  on public.units for select to authenticated
  using (exists (
    select 1 from public.builder_projects bp
    where bp.user_id = (select auth.uid())
      and bp.project_name = public.units.project_name
  ));

drop policy if exists "unit deals builders read assigned" on public.unit_deals;
create policy "unit deals builders read assigned"
  on public.unit_deals for select to authenticated
  using (exists (
    select 1
    from public.units u
    join public.builder_projects bp on bp.project_name = u.project_name
    where u.id = public.unit_deals.unit_id
      and bp.user_id = (select auth.uid())
  ));

grant select, insert, update, delete on public.brokers, public.client_registrations, public.builder_projects, public.units, public.unit_deals to authenticated;
