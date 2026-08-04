from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
'import { supabase } from "../lib/supabase";',
'import { supabase } from "../lib/supabase";'
)

text = text.replace(
'''export default function AttendantDashboard({ staff }) {''',
'''export default function AttendantDashboard({ staff, openSales }) {'''
)

text = text.replace(
'''<button>Record Sales</button>''',
'''<button
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
)

file.write_text(text)

print("Attendant Record Sales connection patched")
