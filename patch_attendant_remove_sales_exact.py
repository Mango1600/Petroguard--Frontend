from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
'export default function AttendantDashboard({ staff, openSales }) {',
'export default function AttendantDashboard({ staff }) {'
)

old = '''<button
        onClick={() =>
          openSales &&
          openSales({
            pump_shift_id: shift.id,
            pump_id: shift.pumps.id,
            staff_id: staff.id,
            business_day_id: shift.business_days.id
          })
        }
      >
        Record Sales
      </button>'''

text = text.replace(old, '''<button>
        Opening Evidence
      </button>''')

file.write_text(text)

print("Exact attendant sales removal complete")
