from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
text = p.read_text()

# Add state for pumpShiftId
if 'const [pumpShiftId, setPumpShiftId] = useState(null);' not in text:
    text = text.replace(
        'const [attendants,setAttendants] = useState([]);',
        '''const [attendants,setAttendants] = useState([]);
const [pumpShiftId, setPumpShiftId] = useState(null);'''
    )

# Save the pump shift ID after loading it
text = text.replace(
    'const pumpShift = await getOpenPumpShift(businessDay.id);',
    '''const pumpShift = await getOpenPumpShift(businessDay.id);
setPumpShiftId(pumpShift?.id);'''
)

p.write_text(text)
print("✅ ResumeAssignment pumpShiftId fixed.")
