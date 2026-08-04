from pathlib import Path

files = {}

files["supabase/module10_rules.sql"] = r'''
create or replace function generate_fraud_alert(
    p_business_day_id uuid,
    p_pump_shift_id uuid,
    p_reconciliation_id uuid
)

returns uuid

language plpgsql

as $$

declare

    variance_value numeric := 0;
    risk numeric := 0;
    level text;
    alert_id uuid;


begin


select abs(variance_amount)

into variance_value

from reconciliations

where id = p_reconciliation_id;



if variance_value is null then

    variance_value := 0;

end if;



risk :=
case

    when variance_value = 0
        then 0

    when variance_value <= 5000
        then 20

    when variance_value <= 20000
        then 50

    when variance_value <= 50000
        then 75

    else 100

end;



level :=
case

    when risk <= 20
        then 'LOW'

    when risk <= 50
        then 'MEDIUM'

    when risk <= 75
        then 'HIGH'

    else 'CRITICAL'

end;



insert into fraud_alerts(

    business_day_id,

    pump_shift_id,

    reconciliation_id,

    alert_type,

    risk_score,

    risk_level,

    description

)

values(

    p_business_day_id,

    p_pump_shift_id,

    p_reconciliation_id,

    'RECONCILIATION_VARIANCE',

    risk,

    level,

    'Automatic variance analysis generated this fraud alert'

)

returning id into alert_id;



return alert_id;


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


print("Module 10 fraud rules complete")
