-- Broker invitations run only in authenticated Edge Functions using the
-- service-role key. The public browser client receives no write permission.
grant select, insert, delete on public.brokers to service_role;
