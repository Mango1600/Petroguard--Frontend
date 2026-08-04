from pathlib import Path

files = {}

files["supabase/module10_fraud_engine.sql"] = r'''
create extension if not exists pgcrypto;


create table if not exists fraud_alerts (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,

    pump_shift_id uuid,

    reconciliation_id uuid,

    alert_type text not null,

    risk_score numeric not null default 0,

    risk_level text not null
        check (
            risk_level in (
                'LOW',
                'MEDIUM',
                'HIGH',
                'CRITICAL'
            )
        ),

    description text,

    status text default 'OPEN'
        check (
            status in (
                'OPEN',
                'REVIEWED',
                'RESOLVED'
            )
        ),

    created_at timestamptz default now()

);


create index if not exists idx_fraud_alert_shift

on fraud_alerts(pump_shift_id);


create index if not exists idx_fraud_alert_status

on fraud_alerts(status);


'''

base = Path(".")

for path, content in files.items():

    file = base / path
    file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    file.write_text(content)

    print(f"Created {path}")


print("Module 10 fraud database foundation complete")
