from pathlib import Path

files = {}

files["supabase/pilot_simulation_tests.sql"] = r'''
create table if not exists pilot_simulation_runs (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    simulation_name text not null,

    status text default 'PENDING'
        check (
            status in (
                'PENDING',
                'RUNNING',
                'PASSED',
                'FAILED'
            )
        ),

    workflow_result jsonb,

    created_at timestamptz default now()

);



create index if not exists idx_simulation_station

on pilot_simulation_runs(station_id);



create or replace function record_simulation_result(

    p_station_id uuid,

    p_status text,

    p_result jsonb

)

returns uuid

language plpgsql

as $$

declare

    run_id uuid;

begin


insert into pilot_simulation_runs(

    station_id,

    simulation_name,

    status,

    workflow_result

)

values(

    p_station_id,

    'FULL_BUSINESS_DAY_SIMULATION',

    p_status,

    p_result

)

returning id into run_id;


return run_id;


end;

$$;



'''

base = Path(".")

for path, content in files.items():

    file = base / path
    file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file.write_text(content)

    print(f"Created {path}")


print("Pilot full business day simulation framework complete")
