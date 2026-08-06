-- The first administrator may have signed up before the role trigger existed.
-- Backfill only the explicitly approved bootstrap address.
insert into public.user_roles (user_id, role)
select u.id, 'admin'::public.platform_role
from auth.users u
join private.bootstrap_admin_emails b on lower(b.email) = lower(u.email)
on conflict (user_id) do update set role = excluded.role;
