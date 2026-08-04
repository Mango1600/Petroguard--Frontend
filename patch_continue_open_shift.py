from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

old = '''.from("staff_shifts")
      .select("id")
      .eq("staff_id", staff.id)
      .eq("status", "open")
      .maybeSingle();'''

new = '''.from("staff_shifts")
      .select("id,station_id,status")
      .eq("station_id", staff.station_id)
      .eq("status", "open")
      .maybeSingle();'''

if old in text:
    text = text.replace(old,new)
    p.write_text(text)
    print("✅ Continue existing station shift enabled")
else:
    print("⚠️ Shift query block not found")
