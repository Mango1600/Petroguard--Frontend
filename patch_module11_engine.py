from pathlib import Path

files = {}

files["supabase/module11_engine.sql"] = r'''
create or replace function generate_daily_report(
    p_business_day_id uuid,
    p_station_id uuid,
    p_generated_by uuid
)

returns uuid

language plpgsql

as $$

declare

    report_id uuid;

    report jsonb;


begin


select jsonb_build_object(

    'business_day',
    p_business_day_id,

    'station',
    p_station_id,


    'total_sales',

    coalesce(

        (
        select sum(total_amount)

        from meter_sales ms

        where ms.business_day_id =
        p_business_day_id

        ),0

    ),


    'payment_summary',

    coalesce(

        (

        select jsonb_agg(pa)

        from payment_allocations pa

        where pa.business_day_id =
        p_business_day_id

        ),

        '[]'::jsonb

    ),



    'fraud_alerts',

    coalesce(

        (

        select count(*)

        from fraud_alerts fa

        where fa.business_day_id =
        p_business_day_id

        ),

        0

    )

)

into report;



insert into operational_reports(

    business_day_id,

    station_id,

    report_type,

    generated_by,

    report_data

)

values(

    p_business_day_id,

    p_station_id,

    'DAILY_OPERATION_REPORT',

    p_generated_by,

    report

)

returning id into report_id;



return report_id;


end;

$$;

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


print("Module 11 reporting engine complete")
