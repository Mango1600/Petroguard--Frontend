from pathlib import Path

files = {}

files["supabase/module8_controls.sql"] = r'''
create or replace function validate_manager_approval()

returns trigger

language plpgsql

as $$

declare

    reconciliation_status text;

begin


select status

into reconciliation_status

from reconciliations

where id = new.reconciliation_id;



if reconciliation_status is null then

    raise exception
    'Reconciliation must exist before approval';

end if;



if reconciliation_status = 'INVESTIGATION'

and new.action = 'APPROVE'

then

    raise exception
    'Investigation cases cannot be approved directly';

end if;



return new;


end;

$$;



drop trigger if exists manager_approval_validation

on manager_approvals;



create trigger manager_approval_validation

before insert

on manager_approvals

for each row

execute function validate_manager_approval();



create index if not exists idx_manager_approval_reconciliation

on manager_approvals(reconciliation_id);

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


print("Module 8 approval controls complete")
