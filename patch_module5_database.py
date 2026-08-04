from pathlib import Path

files = {}

files["supabase/module5_payment_allocation.sql"] = r'''
create extension if not exists pgcrypto;

create table if not exists payment_allocations (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,
    pump_shift_id uuid not null,
    assignment_id uuid not null,

    meter_sale_id uuid not null,

    payment_method text not null
        check (
            payment_method in (
                'CASH',
                'POS',
                'BANK_TRANSFER',
                'CREDIT'
            )
        ),

    amount numeric not null,

    customer_name text,
    customer_phone text,

    evidence_url text,

    created_at timestamptz default now()
);
'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Module 5 database block complete")
