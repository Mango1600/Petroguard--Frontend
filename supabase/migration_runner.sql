
create table if not exists schema_migrations (

    id uuid primary key default gen_random_uuid(),

    migration_name text not null unique,

    applied_at timestamptz not null default now(),

    applied_by text default current_user

);



create or replace function register_migration(

    p_migration_name text

)

returns uuid

language plpgsql

as $$

declare

    migration_id uuid;

begin

    insert into schema_migrations (

        migration_name

    )

    values (

        p_migration_name

    )

    on conflict (migration_name)
    do nothing

    returning id into migration_id;

    return migration_id;

end;

$$;



create index if not exists idx_schema_migrations_name

on schema_migrations(migration_name);
