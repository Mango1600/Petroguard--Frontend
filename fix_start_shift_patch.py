from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")

s = p.read_text()

s = s.replace(
'async function saveAndStartShift() {',
'async function saveAndStartShift() {'
)

s = s.replace(
'station_id: stationId,',
'station_id: staff.station_id,'
)

s = s.replace(
'opened_by: staffId,',
'opened_by: staff.id,'
)

s = s.replace(
'staff_id: staffId,',
'staff_id: staff.id,'
)

p.write_text(s)

print("✅ PetroGuard start shift variables fixed")
