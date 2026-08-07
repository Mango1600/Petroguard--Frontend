from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """.select(`
        id,
        assignment_no,
        status,
        pump_shift_id,
        assigned_at,
        handed_over_at,
        pump_shifts (
          id,
          station_id,
          shift_no,
          status,
          opening_meter,
          closing_meter,
          pumps (
            id,
            pump_name,
            product_type
          ),
          business_days (
            business_date,
            status
          )
        )
      `)"""

new = """.select(`
        *,
        pump_shifts (*)
      `)"""

if old not in text:
    print("❌ Old query not found")
else:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Assignment query simplified")
