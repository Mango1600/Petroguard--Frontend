from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """        *,
        pump_shifts (*)
      `)"""

new = """        *,
        pump_shifts (
          *,
          pumps (
            station_id
          )
        )
      `)"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Shift query updated with station_id")
else:
    print("⚠️ Query pattern not found")
