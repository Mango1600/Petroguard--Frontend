from pathlib import Path

files = {}

files["supabase/module11_reporting.sql"] = r'''
create extension if not exists pgcrypto;


create table if not exists operational_reports (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null,

    station_id uuid not null,

    report_type text not null,

    generated_by uuid,

    report_data jsonb not null,

    created_at timestamptz default now()

);



create index if not exists idx_reports_business_day

on operational_reports(business_day_id);



create index if not exists idx_reports_station

on operational_reports(station_id);



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


print("Module 11 reporting database foundation complete")
