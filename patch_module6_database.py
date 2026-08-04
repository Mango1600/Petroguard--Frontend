from pathlib import Path

files = {}

files["supabase/module6_cash_declaration.sql"] = r'''
create extension if not exists pgcrypto;


create table if not exists cash_declarations (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,
    pump_shift_id uuid not null,
    assignment_id uuid not null,

    attendant_id uuid not null,

    cash_amount numeric default 0,
    pos_amount numeric default 0,
    bank_transfer_amount numeric default 0,
    credit_amount numeric default 0,

    expenses_amount numeric default 0,

    cash_count_evidence text,
    supporting_evidence text,

    submitted_at timestamptz default now(),

    status text default 'SUBMITTED'
        check (
            status in (
                'SUBMITTED',
                'REVIEWED',
                'APPROVED',
                'REJECTED'
            )
        )
);


create index if not exists idx_cash_declaration_shift

on cash_declarations(pump_shift_id);

'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Module 6 database foundation complete")
