
create extension if not exists pgcrypto;


create table if not exists manager_approvals (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,

    pump_shift_id uuid not null,

    reconciliation_id uuid not null,

    manager_id uuid not null,

    action text not null
        check (
            action in (
                'APPROVE',
                'REJECT',
                'INVESTIGATION'
            )
        ),

    comments text,

    approval_evidence text,

    created_at timestamptz default now()

);


create index if not exists idx_manager_approval_shift

on manager_approvals(pump_shift_id);

