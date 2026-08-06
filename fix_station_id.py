from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")

s = p.read_text()

old = """pump_shifts (
          id,
          shift_no,"""

new = """pump_shifts (
          id,
          station_id,
          shift_no,"""

if old not in s:
    raise SystemExit("target not found")

p.write_text(s.replace(old, new))

print("✅ station_id added to pump shift query")
