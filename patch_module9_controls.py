from pathlib import Path

files = {}

files["supabase/module9_controls.sql"] = r'''
create or replace function validate_business_day_close()

returns trigger

language plpgsql

as $$

declare

    active_shifts integer;
    pending_reconciliations integer;
    pending_approvals integer;

begin


select count(*)

into active_shifts

from pump_shifts

where business_day_id = new.business_day_id

and status = 'OPEN';



if active_shifts > 0 then

    raise exception
    'Cannot close Business Day. Active Pump Shift exists';

end if;



select count(*)

into pending_reconciliations

from reconciliations r

where r.business_day_id = new.business_day_id

and r.status not in (
    'BALANCED',
    'APPROVED'
);



if pending_reconciliations > 0 then

    raise exception
    'Cannot close Business Day. Reconciliation incomplete';

end if;



select count(*)

into pending_approvals

from manager_approvals ma

where ma.business_day_id = new.business_day_id

and ma.action not in (
    'APPROVE'
);



if pending_approvals > 0 then

    raise exception
    'Cannot close Business Day. Manager approval incomplete';

end if;



return new;


end;

$$;



drop trigger if exists business_day_close_validation

on business_day_closures;



create trigger business_day_close_validation

before insert

on business_day_closures

for each row

execute function validate_business_day_close();


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


print("Module 9 close controls complete")
