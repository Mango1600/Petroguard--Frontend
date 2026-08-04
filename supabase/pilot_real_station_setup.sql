
create table if not exists pilot_station_setup (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    setup_type text not null,

    setup_status text default 'PENDING'
        check (
            setup_status in (
                'PENDING',
                'READY',
                'ACTIVE'
            )
        ),

    configuration jsonb not null,

    created_at timestamptz default now()

);


create index if not exists idx_pilot_setup_station

on pilot_station_setup(station_id);



-- Pilot readiness records

insert into pilot_station_setup(

    station_id,

    setup_type,

    setup_status,

    configuration

)

select

    id,

    'STATION_CONFIGURATION',

    'READY',

    jsonb_build_object(

        'modules',
        jsonb_build_array(

            'BUSINESS_DAY',

            'PUMP_SHIFT',

            'ASSIGNMENT',

            'METER_SALES',

            'PAYMENT',

            'CASH_DECLARATION',

            'RECONCILIATION',

            'APPROVAL',

            'FRAUD',

            'REPORTING'

        )

    )

from stations

where not exists (

    select 1

    from pilot_station_setup p

    where p.station_id = stations.id

);



