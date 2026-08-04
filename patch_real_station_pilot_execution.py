from pathlib import Path

files = {}

files["supabase/real_station_pilot_execution.sql"] = r'''
create table if not exists real_station_pilot_runs (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null references stations(id),

    business_day_id uuid references business_days(id),

    pilot_status text not null
        check (
            pilot_status in (
                'PREPARING',
                'RUNNING',
                'COMPLETED',
                'FAILED'
            )
        )
        default 'PREPARING',

    opened_at timestamptz,

    closed_at timestamptz,

    observations jsonb default '{}'::jsonb,

    created_at timestamptz default now()

);



create index if not exists idx_real_station_pilot_station

on real_station_pilot_runs(station_id);



create or replace function start_real_station_pilot(

    p_station_id uuid,

    p_business_day_id uuid

)

returns uuid

language plpgsql

as $$

declare

    v_pilot_id uuid;

begin

    insert into real_station_pilot_runs (

        station_id,

        business_day_id,

        pilot_status,

        opened_at

    )

    values (

        p_station_id,

        p_business_day_id,

        'RUNNING',

        now()

    )

    returning id into v_pilot_id;

    return v_pilot_id;

end;

$$;



create or replace function finish_real_station_pilot(

    p_pilot_id uuid,

    p_status text,

    p_observations jsonb

)

returns void

language plpgsql

as $$

begin

    update real_station_pilot_runs

       set pilot_status = p_status,

           observations = p_observations,

           closed_at = now()

     where id = p_pilot_id;

end;

$$;
'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Real station pilot execution framework complete")
