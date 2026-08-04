
create extension if not exists pgcrypto;


create table if not exists business_day_closures (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,

    closed_by uuid not null,

    closing_evidence text,

    status text default 'PENDING'
        check (
            status in (
                'PENDING',
                'CLOSED',
                'BLOCKED'
            )
        ),

    closing_notes text,

    closed_at timestamptz default now()

);


create index if not exists idx_business_day_close

on business_day_closures(business_day_id);

