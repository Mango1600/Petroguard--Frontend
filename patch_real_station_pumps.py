from pathlib import Path

files = {}

files["supabase/real_station_pumps.sql"] = r'''
create table if not exists station_pump_configuration (

    id uuid primary key default gen_random_uuid(),

    station_id uuid not null references stations(id),

    pump_id uuid not null references pumps(id),

    product_type text not null
        check (
            product_type in (
                'PMS',
                'AGO',
                'DPK',
                'LPG',
                'CNG',
                'EV'
            )
        ),

    nozzle_number integer,

    active boolean default true,

    created_at timestamptz default now(),

    unique(station_id, pump_id)
);



create or replace function validate_station_pump_configuration()

returns trigger

language plpgsql

as $$

begin

    if not exists (
        select 1
        from pumps p
        where p.id = new.pump_id
          and p.station_id = new.station_id
    ) then
        raise exception 'Pump does not belong to the selected station';
    end if;

    return new;

end;

$$;



drop trigger if exists trg_station_pump_configuration
on station_pump_configuration;



create trigger trg_station_pump_configuration

before insert or update

on station_pump_configuration

for each row

execute function validate_station_pump_configuration();

'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Real station pump configuration complete")
