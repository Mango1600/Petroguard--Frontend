
-- Enable Row Level Security on core control tables

alter table if exists business_day_closures
enable row level security;


alter table if exists manager_approvals
enable row level security;


alter table if exists fraud_alerts
enable row level security;


alter table if exists operational_reports
enable row level security;



-- Basic authenticated access policies

create policy "Authenticated users access business day closures"

on business_day_closures

for all

to authenticated

using (true)

with check (true);



create policy "Authenticated users access approvals"

on manager_approvals

for all

to authenticated

using (true)

with check (true);



create policy "Authenticated users access fraud alerts"

on fraud_alerts

for all

to authenticated

using (true)

with check (true);



create policy "Authenticated users access reports"

on operational_reports

for all

to authenticated

using (true)

with check (true);



