from pathlib import Path

files = {}

files["supabase/pump_shifts.sql"] = """
create extension if not exists pgcrypto;

create table if not exists pump_shifts (
    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null references business_days(id),

    station_id uuid not null references stations(id),

    pump_id uuid not null references pumps(id),

    status text not null default 'OPEN'
        check(status in ('OPEN','CLOSED')),

    opened_by uuid references staff(id),
    opened_at timestamptz default now(),

    closed_by uuid references staff(id),
    closed_at timestamptz,

    created_at timestamptz default now()
);
"""

files["src/lib/pumpShift.js"] = """
import { supabase } from "./supabase";

export async function getOpenPumpShift(pumpId){
  return await supabase
    .from("pump_shifts")
    .select("*")
    .eq("pump_id", pumpId)
    .eq("status","OPEN")
    .maybeSingle();
}
"""
files["src/pages/PumpShift.jsx"] = """
export default function PumpShift(){
  return (
    <div>
      <h2>Pump Shift</h2>
    </div>
  );
}
"""

files["src/components/PumpShiftCard.jsx"] = """
export default function PumpShiftCard(){
  return (
    <div>
      <h3>Pump Shift</h3>
    </div>
  );
}
"""

files["src/components/PumpShiftStatus.jsx"] = """
export default function PumpShiftStatus(){
  return (
    <div>Status</div>
  );
}
"""

files["src/components/PumpSelector.jsx"] = """
export default function PumpSelector(){
  return (
    <select>
      <option>Select Pump</option>
    </select>
  );
}
"""

for filename, content in files.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")

print("MODULE 2 CREATED")
print("FILES:", len(files))
for f in files:
    print("✓", f)
