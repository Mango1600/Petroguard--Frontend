from pathlib import Path

files = {}

files["supabase/production_database_verification.sql"] = r'''
create table if not exists production_database_verification (

    id uuid primary key default gen_random_uuid(),

    verification_name text not null,

    object_type text not null
        check (
            object_type in (
                'TABLE',
                'VIEW',
                'FUNCTION',
                'TRIGGER',
                'INDEX',
                'POLICY',
                'CONSTRAINT'
            )
        ),

    object_name text not null,

    verification_status text not null default 'PENDING'
        check (
            verification_status in (
                'PENDING',
                'PASS',
                'FAIL'
            )
        ),

    details jsonb,

    verified_at timestamptz

);



create or replace function verify_production_database()

returns jsonb

language plpgsql

as $$

declare

    result jsonb;

begin

    result := jsonb_build_object(

        'business_days',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'business_days'
        ),

        'pump_shifts',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'pump_shifts'
        ),

        'meter_sales',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'meter_sales'
        ),

        'cash_declarations',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'cash_declarations'
        ),

        'reconciliations',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'reconciliations'
        ),

        'manager_approvals',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'manager_approvals'
        ),

        'fraud_alerts',
        exists (
            select 1
            from information_schema.tables
            where table_name = 'fraud_alerts'
        )

    );

    return result;

end;

$$;
'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Production database verification complete")
