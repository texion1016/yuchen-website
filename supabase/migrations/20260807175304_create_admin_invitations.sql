create table public.admin_invitations (
  email text primary key check (email = lower(email)),
  invited_by uuid not null references auth.users(id) on delete restrict,
  expires_at timestamptz not null,
  accepted_at timestamptz,
  created_at timestamptz not null default now()
);

alter table public.admin_invitations enable row level security;
