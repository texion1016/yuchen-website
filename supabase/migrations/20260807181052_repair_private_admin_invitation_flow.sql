grant usage on schema private to service_role;

grant select, insert, update, delete
on table private.admin_invitations
to service_role;

create index if not exists admin_invitations_invited_by_idx
on private.admin_invitations (invited_by);

create or replace function public.create_admin_invitation(
  invitation_email text,
  invitation_invited_by uuid,
  invitation_expires_at timestamptz
)
returns void
language sql
security invoker
set search_path = ''
as $$
  insert into private.admin_invitations (email, invited_by, expires_at, accepted_at)
  values (lower(invitation_email), invitation_invited_by, invitation_expires_at, null)
  on conflict (email) do update
    set invited_by = excluded.invited_by,
        expires_at = excluded.expires_at,
        accepted_at = null;
$$;

revoke all on function public.create_admin_invitation(text, uuid, timestamptz)
from public, anon, authenticated;
grant execute on function public.create_admin_invitation(text, uuid, timestamptz)
to service_role;

create or replace function public.delete_pending_admin_invitation(invitation_email text)
returns void
language sql
security invoker
set search_path = ''
as $$
  delete from private.admin_invitations
  where email = lower(invitation_email)
    and accepted_at is null;
$$;

revoke all on function public.delete_pending_admin_invitation(text)
from public, anon, authenticated;
grant execute on function public.delete_pending_admin_invitation(text)
to service_role;

drop table if exists public.admin_invitations;
