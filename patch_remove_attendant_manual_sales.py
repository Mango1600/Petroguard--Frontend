from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
'''
      <button
        onClick={() =>
          openSales &&
          openSales({
            pump_shift_id: shift.id,
            pump_id: shift.pump_id,
            business_day_id: shift.business_day_id,
            staff_id: staff.id
          })
        }
      >
        Record Sales
      </button>
''',
'''
      <button>
        Opening Evidence
      </button>
'''
)

file.write_text(text)

print("Attendant manual sales removed")
