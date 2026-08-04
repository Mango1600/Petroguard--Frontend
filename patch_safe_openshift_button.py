from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

if 'import OpenShift from "./OpenShift";' not in text:
    text = text.replace(
        'import { handoverAssignment } from "../lib/pumpShiftAssignment";',
        'import { handoverAssignment } from "../lib/pumpShiftAssignment";\nimport OpenShift from "./OpenShift";'
    )

text = text.replace(
    'const [loading, setLoading] = useState(true);',
    'const [loading, setLoading] = useState(true);\n  const [openShiftMode, setOpenShiftMode] = useState(false);'
)

old = """  if (!assignment)

  return (
      <div style={{padding:20}}>
        <h2>No Active Pump Assignment</h2>
      </div>
    );"""

new = """  if (!assignment && openShiftMode)
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => window.location.reload()}
      />
    );

  if (!assignment)
    return (
      <div style={{padding:20}}>
        <h2>No Active Pump Assignment</h2>
        <button onClick={()=>setOpenShiftMode(true)}>
          Open Shift
        </button>
      </div>
    );"""

if old not in text:
    print("Target not found")
    raise SystemExit

text = text.replace(old, new)

path.write_text(text)

print("Safe OpenShift controller added")
