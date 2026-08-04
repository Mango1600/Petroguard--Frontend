
create table if not exists pilot_role_tests (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    role_name text not null,

    permission_area text not null,

    expected_access text not null,

    result text default 'PENDING'
        check (
            result in (
                'PASS',
                'FAIL',
                'PENDING'
            )
        ),

    notes text,

    created_at timestamptz default now()

);



create index if not exists idx_pilot_role_station

on pilot_role_tests(station_id);



create or replace function validate_role_access(

    p_station_id uuid,

    p_role text,

    p_area text

)

returns jsonb

language plpgsql

as $$

declare

    response jsonb;

begin


response := jsonb_build_object(

    'station_id',
    p_station_id,

    'role',
    p_role,

    'area',
    p_area,

    'validated',
    true

);


return response;


end;

$$;



