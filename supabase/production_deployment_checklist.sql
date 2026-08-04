
create table if not exists production_checklist (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null,

    checklist_item text not null,

    status text default 'PENDING'
        check (
            status in (
                'PASS',
                'FAIL',
                'PENDING'
            )
        ),

    verified_by uuid,

    notes text,

    created_at timestamptz default now()

);



create index if not exists idx_production_check_station

on production_checklist(station_id);



create or replace function verify_production_item(

    p_station_id uuid,

    p_item text,

    p_status text,

    p_notes text

)

returns uuid

language plpgsql

as $$

declare

    item_id uuid;

begin


insert into production_checklist(

    station_id,

    checklist_item,

    status,

    notes

)

values(

    p_station_id,

    p_item,

    p_status,

    p_notes

)

returning id into item_id;



return item_id;


end;

$$;


