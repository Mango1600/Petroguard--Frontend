from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")

s = p.read_text()

old = """if(previous){
setPreviousMeter(previous.closing_meter);
setOpeningMeter(previous.closing_meter);
}"""

new = """if(previous){
setPreviousMeter(previous.closing_meter);

const { data: activeAssignment } = await supabase
.from("attendant_assignments")
.select("opening_meter")
.eq("pump_shift_id", pumpShift.id)
.eq("status", "ACTIVE")
.maybeSingle();

if(activeAssignment?.opening_meter){
  setOpeningMeter(activeAssignment.opening_meter);
  setPreviousMeter(activeAssignment.opening_meter);
}else{
  setOpeningMeter(previous.closing_meter);
}
}"""

if old not in s:
    raise SystemExit("Target block not found")

p.write_text(s.replace(old, new))

print("✅ Resume meter logic patched")
