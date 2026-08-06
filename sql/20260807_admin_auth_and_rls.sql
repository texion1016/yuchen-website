-- Secure administrator access for the Yuchen platform.
-- First administrator: davidlin10161016@gmail.com

create schema if not exists private;
revoke all on schema private from public;

create type public.platform_role as enum ('admin', 'broker', 'builder');

create table public.user_roles (
  user_id uuid primary key references auth.users(id) on delete cascade,
  role public.platform_role not null,
  created_at timestamptz not null default now()
);

alter table public.user_roles enable row level security;
revoke all on table public.user_roles from public, anon;
grant select on table public.user_roles to authenticated;

create policy "users can read their own role"
  on public.user_roles for select to authenticated
  using ((select auth.uid()) = user_id);

create table private.bootstrap_admin_emails (
  email text primary key,
  created_at timestamptz not null default now()
);

insert into private.bootstrap_admin_emails (email)
values ('davidlin10161016@gmail.com')
on conflict (email) do nothing;

create table private.admin_invitations (
  email text primary key,
  invited_by uuid not null references auth.users(id) on delete restrict,
  created_at timestamptz not null default now(),
  expires_at timestamptz not null default (now() + interval '7 days'),
  accepted_at timestamptz
);

alter table private.bootstrap_admin_emails enable row level security;
alter table private.admin_invitations enable row level security;
revoke all on table private.bootstrap_admin_emails, private.admin_invitations from public, anon, authenticated;

create or replace function public.is_admin()
returns boolean
language sql
stable
security definer
set search_path = public
as $$
  select exists (
    select 1
    from public.user_roles
    where user_id = (select auth.uid())
      and role = 'admin'
  );
$$;

revoke all on function public.is_admin() from public;
grant execute on function public.is_admin() to authenticated;

create or replace function private.assign_platform_role()
returns trigger
language plpgsql
security definer
set search_path = private, public, pg_catalog
as $$
declare
  invitation private.admin_invitations%rowtype;
begin
  if new.email is null then
    return new;
  end if;

  if exists (
    select 1 from private.bootstrap_admin_emails
    where lower(email) = lower(new.email)
  ) then
    insert into public.user_roles (user_id, role)
    values (new.id, 'admin')
    on conflict (user_id) do update set role = excluded.role;
    return new;
  end if;

  select * into invitation
  from private.admin_invitations
  where lower(email) = lower(new.email)
    and accepted_at is null
    and expires_at > now()
  for update;

  if found then
    insert into public.user_roles (user_id, role)
    values (new.id, 'admin')
    on conflict (user_id) do update set role = excluded.role;

    update private.admin_invitations
    set accepted_at = now()
    where email = invitation.email;
  end if;

  return new;
end;
$$;

revoke all on function private.assign_platform_role() from public;

create trigger assign_platform_role_after_signup
  after insert on auth.users
  for each row execute function private.assign_platform_role();

-- Public visitors may read only published projects and submit a request.
-- All sensitive reads and operational changes require a signed-in administrator.
drop policy if exists "booking_insert" on public.bookings;
drop policy if exists "booking_select" on public.bookings;
drop policy if exists "brokers manage" on public.brokers;
drop policy if exists "brokers_insert" on public.brokers;
drop policy if exists "brokers_select_own" on public.brokers;
drop policy if exists "admin can update registrations" on public.client_registrations;
drop policy if exists "reg_insert" on public.client_registrations;
drop policy if exists "reg_select_all" on public.client_registrations;
drop policy if exists "inquiry_insert" on public.inquiries;
drop policy if exists "inquiry_select" on public.inquiries;
drop policy if exists "projects all" on public.projects;
drop policy if exists "deals all" on public.unit_deals;
drop policy if exists "units all" on public.units;

revoke all on table public.bookings, public.brokers, public.client_registrations,
  public.inquiries, public.projects, public.units, public.unit_deals
  from public, anon, authenticated;

grant select, insert, update, delete on table public.bookings, public.brokers,
  public.client_registrations, public.inquiries, public.projects, public.units,
  public.unit_deals to authenticated;

grant select on table public.projects to anon;
grant insert on table public.bookings, public.brokers, public.client_registrations,
  public.inquiries to anon;

create policy "projects public read published"
  on public.projects for select to anon, authenticated
  using (published is true);

create policy "projects administrators manage"
  on public.projects for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "brokers public application"
  on public.brokers for insert to anon, authenticated
  with check (true);

create policy "brokers administrators manage"
  on public.brokers for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "registrations public submit"
  on public.client_registrations for insert to anon, authenticated
  with check (true);

create policy "registrations administrators manage"
  on public.client_registrations for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "bookings public submit"
  on public.bookings for insert to anon, authenticated
  with check (true);

create policy "bookings administrators manage"
  on public.bookings for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "inquiries public submit"
  on public.inquiries for insert to anon, authenticated
  with check (true);

create policy "inquiries administrators manage"
  on public.inquiries for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "units administrators manage"
  on public.units for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));

create policy "unit deals administrators manage"
  on public.unit_deals for all to authenticated
  using ((select public.is_admin()))
  with check ((select public.is_admin()));
