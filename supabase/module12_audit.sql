
create extension if not exists pgcrypto;


create table if not exists audit_logs (

    id uuid primary key default gen_random_uuid(),

    user_id uuid,

    action text not null,

    entity_type text not null,

    entity_id uuid,

    details jsonb,

    created_at timestamptz default now()

);



create index if not exists idx_audit_entity

on audit_logs(entity_type, entity_id);



create index if not exists idx_audit_user

on audit_logs(user_id);



create or replace function create_audit_log()

returns trigger

language plpgsql

as $$

begin


insert into audit_logs(

    action,

    entity_type,

    entity_id,

    details

)

values(

    TG_OP,

    TG_TABLE_NAME,

    new.id,

    to_jsonb(new)

);


return new;


end;

$$;



drop trigger if exists audit_business_day_close

on business_day_closures;



create trigger audit_business_day_close

after insert

on business_day_closures

for each row

execute function create_audit_log();



drop trigger if exists audit_manager_approval

on manager_approvals;



create trigger audit_manager_approval

after insert

on manager_approvals

for each row

execute function create_audit_log();



