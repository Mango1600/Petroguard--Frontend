create extension if not exists pgcrypto;

create table if not exists meter_sales (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null references business_days(id),

    pump_shift_id uuid not null references pump_shifts(id),

    assignment_id uuid not null references pump_shift_assignments(id),

    pump_id uuid not null references pumps(id),

    opening_meter numeric not null,

    closing_meter numeric not null,

    litres_sold numeric not null,

    unit_price numeric not null,

    total_amount numeric not null,

    calculated_at timestamptz default now()
);
