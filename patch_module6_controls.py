from pathlib import Path

files = {}

files["supabase/module6_controls.sql"] = r'''
alter table cash_declarations

add column if not exists cash_count_evidence_required boolean default true;


create unique index if not exists one_declaration_per_shift

on cash_declarations(pump_shift_id);


create or replace function check_cash_declaration_status()

returns trigger

language plpgsql

as $$

begin

    if new.cash_amount < 0
    or new.pos_amount < 0
    or new.bank_transfer_amount < 0
    or new.credit_amount < 0
    or new.expenses_amount < 0

    then

        raise exception
        'Declaration amounts cannot be negative';

    end if;


    return new;

end;

$$;


drop trigger if exists validate_cash_declaration

on cash_declarations;


create trigger validate_cash_declaration

before insert or update

on cash_declarations

for each row

execute function check_cash_declaration_status();

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


print("Module 6 controls complete")
