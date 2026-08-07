from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

text = text.replace(
"""          pumps (
            station_id
          )""",
"""          pumps (
            station_id,
            pump_name,
            product_type
          ),
          business_days (
            business_date
          )"""
)

path.write_text(text)
print("✅ Query updated")
