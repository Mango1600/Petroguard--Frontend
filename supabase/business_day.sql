create extension if not exists pgcrypto;

create table if not exists business_days (
    id uuid primary key default gen_random_uuid(),

    station_id uuid not null references stations(id),

    business_date date not null,

    status text not null default 'OPEN'
        check (status in ('OPEN','CLOSED')),

    opened_by uuid references staff(id),
    opened_at timestamptz default now(),

    closed_by uuid references staff(id),
    closed_at timestamptz,

    created_at timestamptz default now(),

    constraint business_day_unique unique (station_id, business_date)
);

create index if not exists idx_business_days_station
on business_days(station_id);

create index if not exists idx_business_days_status
on business_days(status);
