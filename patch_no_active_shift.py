from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")

text = path.read_text()

old = '''if (!assignment)
    return (
      <div style={{padding:20}}>
        <h2>No Active Pump Assignment</h2>
        <button onClick={()=>setOpenShiftMode(true)}>
          Open Shift
        </button>
      </div>
    );'''

new = '''if (!assignment)
    return (
      <div style={{padding:20}}>
        <h2>Pump Shift Available</h2>
        <p>No active attendant assignment found.</p>
        <p>Existing OPEN Pump Shift can be resumed.</p>

        <button onClick={()=>setOpenShiftMode(true)}>
          Resume Pump Shift
        </button>
      </div>
    );'''

if old in text:
    text = text.replace(old,new)
else:
    print("Target block not found")

path.write_text(text)

print("No Active Shift display updated.")
