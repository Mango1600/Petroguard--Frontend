
create table if not exists migration_execution_log (

    id uuid primary key default gen_random_uuid(),

    migration_name text not null,

    execution_status text not null
        check (
            execution_status in (
                'RUNNING',
                'SUCCESS',
                'FAILED'
            )
        ),

    started_at timestamptz not null default now(),

    completed_at timestamptz,

    error_message text

);



create or replace function start_migration_execution(

    p_migration_name text

)

returns uuid

language plpgsql

as $$

declare

    execution_id uuid;

begin

    insert into migration_execution_log(

        migration_name,

        execution_status

    )

    values(

        p_migration_name,

        'RUNNING'

    )

    returning id into execution_id;

    return execution_id;

end;

$$;



create or replace function finish_migration_execution(

    p_execution_id uuid,

    p_status text,

    p_error_message text default null

)

returns void

language plpgsql

as $$

begin

    update migration_execution_log

       set execution_status = p_status,

           completed_at = now(),

           error_message = p_error_message

     where id = p_execution_id;

end;

$$;



create index if not exists idx_migration_execution_status

on migration_execution_log(execution_status);
