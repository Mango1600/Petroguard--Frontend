from pathlib import Path

files = {}

files["supabase/production_go_live.sql"] = r'''
create table if not exists production_deployments (

    id uuid primary key default gen_random_uuid(),

    deployment_name text not null,

    version text not null,

    station_id uuid references stations(id),

    deployment_status text not null
        check (
            deployment_status in (
                'PLANNED',
                'DEPLOYING',
                'LIVE',
                'ROLLED_BACK'
            )
        )
        default 'PLANNED',

    deployed_by uuid,

    deployed_at timestamptz,

    rollback_at timestamptz,

    deployment_notes text,

    created_at timestamptz default now()

);



create index if not exists idx_production_deployments_status

on production_deployments(deployment_status);



create or replace function go_live(

    p_deployment_name text,

    p_version text,

    p_station_id uuid,

    p_deployed_by uuid,

    p_notes text

)

returns uuid

language plpgsql

as $$

declare

    v_deployment_id uuid;

begin

    insert into production_deployments(

        deployment_name,

        version,

        station_id,

        deployment_status,

        deployed_by,

        deployed_at,

        deployment_notes

    )

    values(

        p_deployment_name,

        p_version,

        p_station_id,

        'LIVE',

        p_deployed_by,

        now(),

        p_notes

    )

    returning id into v_deployment_id;

    return v_deployment_id;

end;

$$;
'''

base = Path(".")

for path, content in files.items():
    file = base / path
    file.parent.mkdir(parents=True, exist_ok=True)
    file.write_text(content)
    print(f"Created {path}")

print("Production go-live framework complete")
