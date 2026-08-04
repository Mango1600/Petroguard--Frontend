from pathlib import Path

files = {}

files["supabase/pump_shift_assignments.sql"] = '''
create extension if not exists pgcrypto;

create table if not exists pump_shift_assignments (
    id uuid primary key default gen_random_uuid(),
    business_day_id uuid not null references business_days(id),
    pump_shift_id uuid not null references pump_shifts(id),
    staff_id uuid not null references staff(id),

    status text not null default 'OPEN'
        check (status in ('OPEN','CLOSED')),

    opening_meter numeric,
    closing_meter numeric,

    opening_evidence text,
    closing_evidence text,

    handover_notes text,

    opened_at timestamptz default now(),
    closed_at timestamptz,
    created_at timestamptz default now()
);
'''

files["src/lib/pumpShiftAssignment.js"] = '''
export async function getAssignments() {
  return [];
}
'''
files["src/pages/PumpShiftAssignment.jsx"] = '''
export default function PumpShiftAssignment() {
  return (
    <div>
      <h2>Pump Shift Assignment</h2>
    </div>
  );
}
'''

files["src/components/AssignmentCard.jsx"] = '''
export default function AssignmentCard() {
  return (
    <div>
      <h3>Assignment</h3>
    </div>
  );
}
'''

files["src/components/HandoverCard.jsx"] = '''
export default function HandoverCard() {
  return (
    <div>
      <h3>Handover</h3>
    </div>
  );
}
'''

files["src/components/AssignmentStatus.jsx"] = '''
export default function AssignmentStatus() {
  return (
    <div>
      <h3>Assignment Status</h3>
    </div>
  );
}
'''

for filename, content in files.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")

print("MODULE 3 CREATED")
print("FILES:", len(files))
for f in files:
    print("✓", f)
