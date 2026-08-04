
create table if not exists production_test_runs (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid,

    station_id uuid not null references stations(id),

    test_name text not null,

    test_status text not null default 'RUNNING'
        check (
            test_status in (
                'RUNNING',
                'PASSED',
                'FAILED'
            )
        ),

    workflow_summary jsonb,

    started_at timestamptz default now(),

    completed_at timestamptz

);



create index if not exists idx_production_test_station

on production_test_runs(station_id);



create or replace function complete_production_test(

    p_test_id uuid,

    p_status text,

    p_summary jsonb

)

returns void

language plpgsql

as $$

begin

    update production_test_runs

       set test_status = p_status,

           workflow_summary = p_summary,

           completed_at = now()

     where id = p_test_id;

end;

$$;
