create extension if not exists pgcrypto;

create table if not exists pump_shift_assignments (
    id uuid primary key default gen_random_uuid(),
    business_day_id uuid not null references business_days(id),
    pump_shift_id uuid not null references pump_shifts(id),
    staff_id uuid not null references staff(id),

    status text not null default 'OPEN'
        check (status in ('OPEN','CLOSED')),

    opening_meter numeric,
    closing_meter numeric,

    opening_evidence text,
    closing_evidence text,

    handover_notes text,

    opened_at timestamptz default now(),
    closed_at timestamptz,
    created_at timestamptz default now()
);
