from pathlib import Path

files = {}

files["supabase/module5_payment_rules.sql"] = r'''
create or replace function validate_payment_allocation()
returns trigger
language plpgsql
as $$

declare
    sale_amount numeric;
    allocated_amount numeric;

begin

    select total_amount
    into sale_amount
    from meter_sales
    where id = new.meter_sale_id;


    select coalesce(sum(amount),0)
    into allocated_amount
    from payment_allocations
    where meter_sale_id = new.meter_sale_id;


    if allocated_amount + new.amount > sale_amount then

        raise exception
        'Payment allocation exceeds calculated sales amount';

    end if;


    return new;

end;

$$;


drop trigger if exists payment_allocation_limit
on payment_allocations;


create trigger payment_allocation_limit

before insert
on payment_allocations

for each row

execute function validate_payment_allocation();


create index if not exists idx_payment_allocations_meter_sale
on payment_allocations(meter_sale_id);

'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Module 5 database rules complete")
