from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

old = (
'  if (!assignment)\n'
'  \n'
'  return (\n'
'      <div style={{padding:20}}>\n'
'        <h2>No Active Pump Assignment</h2>\n'
'      </div>\n'
'    );'
)

new = (
'  if (!assignment) {\n'
'    return (\n'
'      <ResumeAssignment\n'
'        staff={staff}\n'
'        pumpShiftId={2}\n'
'      />\n'
'    );\n'
'  }'
)

if old in text:
    text = text.replace(old, new, 1)
    print("Resume flow connected.")
else:
    print("Target block not found.")

path.write_text(text)
