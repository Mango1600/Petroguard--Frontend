
create table if not exists station_readiness_checks (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null references stations(id),

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

    verified_by uuid,

    verified_at timestamptz default now()

);



create index if not exists idx_station_readiness_station

on station_readiness_checks(station_id);



create or replace function verify_station_readiness(

    p_station_id uuid

)

returns jsonb

language plpgsql

as $$

declare

    result jsonb;

begin

    result := jsonb_build_object(

        'station_exists',
        exists(select 1 from stations where id = p_station_id),

        'business_day_ready',
        exists(select 1 from business_days where station_id = p_station_id),

        'pump_configuration_ready',
        exists(select 1 from station_pump_configuration where station_id = p_station_id),

        'staff_ready',
        exists(select 1 from station_staff_roles where station_id = p_station_id and active = true)

    );

    return result;

end;

$$;
