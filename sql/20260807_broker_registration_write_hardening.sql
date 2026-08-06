-- Brokers can read and submit only their own registrations.  Changes that
-- affect workflow status run through the authenticated Edge Function instead.

drop policy if exists "registrations broker update own" on public.client_registrations;
revoke update on public.client_registrations from authenticated;
