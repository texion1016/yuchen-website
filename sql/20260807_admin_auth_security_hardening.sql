-- Keep authorization helpers and invitation data out of the exposed API schema.

grant usage on schema private to authenticated;

create or replace function private.is_admin()
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

revoke all on function private.is_admin() from public;
grant execute on function private.is_admin() to authenticated;

drop policy "projects administrators manage" on public.projects;
drop policy "brokers administrators manage" on public.brokers;
drop policy "registrations administrators manage" on public.client_registrations;
drop policy "bookings administrators manage" on public.bookings;
drop policy "inquiries administrators manage" on public.inquiries;
drop policy "units administrators manage" on public.units;
drop policy "unit deals administrators manage" on public.unit_deals;

create policy "projects administrators manage"
  on public.projects for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "brokers administrators manage"
  on public.brokers for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "registrations administrators manage"
  on public.client_registrations for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "bookings administrators manage"
  on public.bookings for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "inquiries administrators manage"
  on public.inquiries for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "units administrators manage"
  on public.units for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

create policy "unit deals administrators manage"
  on public.unit_deals for all to authenticated
  using ((select private.is_admin()))
  with check ((select private.is_admin()));

drop function public.is_admin();

create policy "service role manages bootstrap administrators"
  on private.bootstrap_admin_emails for all to service_role
  using (true) with check (true);

create policy "service role manages administrator invitations"
  on private.admin_invitations for all to service_role
  using (true) with check (true);

revoke all on function public.rls_auto_enable() from public, anon, authenticated;
revoke all on function public.send_view_reminders() from public, anon, authenticated;
