from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

# Add state for dynamic pump shift
old = 'const [message,setMessage]=useState("");'

new = '''const [message,setMessage]=useState("");
const [activePumpShiftId,setActivePumpShiftId]=useState(null);'''

text = text.replace(old, new)

# Save OPEN pump shift id after loading
old = 'const pumpShift = await getOpenPumpShift(businessDay.id);'

new = '''const pumpShift = await getOpenPumpShift(businessDay.id);

setActivePumpShiftId(pumpShift.id);'''

text = text.replace(old, new)

# Replace lookup
old = '''
.eq("pump_shift_id",pumpShiftId)
.order("assignment_no",{ascending:false})
'''

new = '''
.eq("pump_shift_id",activePumpShiftId)
.order("assignment_no",{ascending:false})
'''

text = text.replace(old, new)

# Replace insert payload
old = '''
pump_shift_id:pumpShiftId,
'''

new = '''
pump_shift_id:activePumpShiftId,
'''

text = text.replace(old, new)

file.write_text(text)

print("Resume Assignment now uses dynamic OPEN Pump Shift ID.")
