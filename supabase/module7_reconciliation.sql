
create extension if not exists pgcrypto;


create table if not exists reconciliations (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,

    pump_shift_id uuid not null,

    assignment_id uuid,

    meter_sales_amount numeric not null default 0,

    payment_total numeric not null default 0,

    cash_declared numeric not null default 0,

    expenses_amount numeric not null default 0,

    expected_sales numeric not null default 0,

    variance_amount numeric not null default 0,

    variance_percentage numeric not null default 0,

    fraud_score numeric not null default 0,

    status text default 'PENDING'
        check (
            status in (
                'PENDING',
                'BALANCED',
                'VARIANCE',
                'INVESTIGATION',
                'APPROVED'
            )
        ),

    created_at timestamptz default now()

);


create index if not exists idx_reconciliation_shift

on reconciliations(pump_shift_id);

