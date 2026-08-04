from pathlib import Path

files = {}

files["supabase/module7_engine.sql"] = r'''
create or replace function calculate_reconciliation(
    p_pump_shift_id uuid
)

returns uuid

language plpgsql

as $$

declare

    rec_id uuid;

    sales_total numeric := 0;
    payment_total numeric := 0;
    cash_total numeric := 0;
    expense_total numeric := 0;

    variance numeric := 0;
    fraud numeric := 0;


begin


select coalesce(sum(total_amount),0)

into sales_total

from meter_sales

where pump_shift_id = p_pump_shift_id;



select coalesce(sum(amount),0)

into payment_total

from payment_allocations

where pump_shift_id = p_pump_shift_id;



select coalesce(sum(cash_amount),0)

into cash_total

from cash_declarations

where pump_shift_id = p_pump_shift_id;



select coalesce(sum(expenses_amount),0)

into expense_total

from cash_declarations

where pump_shift_id = p_pump_shift_id;



variance :=
sales_total -
(payment_total - expense_total);



if variance = 0 then

    fraud := 0;

else

    fraud :=
    abs(variance) / sales_total * 100;

end if;



insert into reconciliations(

    pump_shift_id,

    meter_sales_amount,

    payment_total,

    cash_declared,

    expenses_amount,

    expected_sales,

    variance_amount,

    variance_percentage,

    fraud_score,

    status

)

values(

    p_pump_shift_id,

    sales_total,

    payment_total,

    cash_total,

    expense_total,

    sales_total,

    variance,

    fraud,

    fraud,

    case

        when variance = 0
        then 'BALANCED'

        when fraud <= 20
        then 'VARIANCE'

        else 'INVESTIGATION'

    end

)

returning id into rec_id;



return rec_id;


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


print("Module 7 calculation engine complete")
