
create table if not exists system_health_checks (

    id uuid primary key default gen_random_uuid(),

    check_name text not null,

    check_status text not null
        check (
            check_status in (
                'PASS',
                'FAIL',
                'PENDING'
            )
        ),

    details jsonb,

    created_at timestamptz default now()

);



create index if not exists idx_health_status

on system_health_checks(check_status);



create or replace function run_system_health_check()

returns jsonb

language plpgsql

as $$

declare

    result jsonb;

begin


select jsonb_build_object(

    'business_day',
    exists(
        select 1 from business_days
    ),


    'pump_shift',
    exists(
        select 1 from pump_shifts
    ),


    'sales',
    exists(
        select 1 from meter_sales
    ),


    'payments',
    exists(
        select 1 from payment_allocations
    ),


    'reconciliation',
    exists(
        select 1 from reconciliations
    ),


    'approval',
    exists(
        select 1 from manager_approvals
    ),


    'fraud',
    exists(
        select 1 from fraud_alerts
    ),


    'reports',
    exists(
        select 1 from operational_reports
    )

)

into result;


return result;


end;

$$;


