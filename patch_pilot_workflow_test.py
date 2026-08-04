from pathlib import Path

files = {}

files["supabase/pilot_workflow_tests.sql"] = r'''
create table if not exists pilot_workflow_tests (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    workflow_step text not null,

    status text not null
        check (
            status in (
                'PASS',
                'FAIL',
                'PENDING'
            )
        ),

    details jsonb,

    tested_at timestamptz default now()

);



create index if not exists idx_pilot_workflow_station

on pilot_workflow_tests(station_id);



create or replace function record_pilot_test(
    p_station_id uuid,
    p_step text,
    p_status text,
    p_details jsonb
)

returns uuid

language plpgsql

as $$

declare

    test_id uuid;

begin


insert into pilot_workflow_tests(

    station_id,

    workflow_step,

    status,

    details

)

values(

    p_station_id,

    p_step,

    p_status,

    p_details

)

returning id into test_id;



return test_id;


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


print("Pilot workflow verification complete")
