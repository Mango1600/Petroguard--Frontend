create extension if not exists pgcrypto;

create table if not exists pump_shifts (
    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null references business_days(id),

    station_id uuid not null references stations(id),

    pump_id uuid not null references pumps(id),

    status text not null default 'OPEN'
        check(status in ('OPEN','CLOSED')),

    opened_by uuid references staff(id),
    opened_at timestamptz default now(),

    closed_by uuid references staff(id),
    closed_at timestamptz,

    created_at timestamptz default now()
);
