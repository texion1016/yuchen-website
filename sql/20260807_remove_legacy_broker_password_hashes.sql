-- Legacy browser-side password hashes are no longer authentication material.
update public.brokers set password_hash = null where password_hash is not null;
