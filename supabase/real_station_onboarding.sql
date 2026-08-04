
create table if not exists station_onboarding (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    onboarding_status text default 'PENDING'
        check (
            onboarding_status in (
                'PENDING',
                'CONFIGURED',
                'ACTIVE'
            )
        ),

    station_profile jsonb not null,

    created_at timestamptz default now()

);



create index if not exists idx_station_onboarding

on station_onboarding(station_id);



create or replace function activate_station_pilot(

    p_station_id uuid,

    p_profile jsonb

)

returns uuid

language plpgsql

as $$

declare

    onboarding_id uuid;

begin


insert into station_onboarding(

    station_id,

    onboarding_status,

    station_profile

)

values(

    p_station_id,

    'CONFIGURED',

    p_profile

)

returning id into onboarding_id;



return onboarding_id;


end;

$$;

