
create table if not exists pilot_configuration (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    pilot_name text not null,

    environment text default 'PILOT',

    status text default 'READY'
        check (
            status in (
                'READY',
                'RUNNING',
                'COMPLETED'
            )
        ),

    created_at timestamptz default now()

);



create index if not exists idx_pilot_station

on pilot_configuration(station_id);



create table if not exists pilot_test_results (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    test_name text not null,

    result text not null
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

