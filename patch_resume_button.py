from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

old = '''
        <button onClick={()=>setOpenShiftMode(true)}>
          Resume Pump Shift
        </button>
'''

new = '''
        <button
          onClick={()=>{
            window.location.href="/resume-assignment";
          }}
        >
          Resume Pump Shift
        </button>
'''

if old in text:
    text = text.replace(old, new)
    print("Resume button connected.")
else:
    print("Resume button not found.")

path.write_text(text)
