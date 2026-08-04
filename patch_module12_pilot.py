from pathlib import Path

files = {}

files["supabase/module12_pilot_check.sql"] = r'''
create table if not exists pilot_checks (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    check_name text not null,

    status text not null

        check (
            status in (
                'PASS',
                'FAIL',
                'PENDING'
            )
        ),

    notes text,

    checked_by uuid,

    created_at timestamptz default now()

);



create index if not exists idx_pilot_station

on pilot_checks(station_id);



create or replace function run_pilot_readiness(
    p_station_id uuid
)

returns jsonb

language plpgsql

as $$

declare

    result jsonb;

begin


select jsonb_build_object(

    'business_day_module',
    exists(
        select 1
        from business_days
        where station_id = p_station_id
    ),


    'pump_module',
    exists(
        select 1
        from pumps
        where station_id = p_station_id
    ),


    'reporting_module',
    exists(
        select 1
        from operational_reports
        where station_id = p_station_id
    )

)

into result;


return result;


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


print("Module 12 pilot readiness complete")
