from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")

lines = path.read_text().splitlines()

# Add OpenShift import after line 4
if not any("import OpenShift" in line for line in lines):
    lines.insert(4, 'import OpenShift from "./OpenShift";')

# Add state after loading state
if not any("openShiftMode" in line for line in lines):
    for i, line in enumerate(lines):
        if 'const [loading, setLoading] = useState(true);' in line:
            lines.insert(i + 1, '  const [openShiftMode, setOpenShiftMode] = useState(false);')
            break

# Find and replace the no assignment section
start = None
end = None

for i, line in enumerate(lines):
    if line.strip() == "if (!assignment)":
        if i + 1 < len(lines) and "return (" in lines[i + 2]:
            start = i
            end = i + 7
            break

if start is None:
    print("No assignment block not found")
    raise SystemExit

replacement = [
'  if (!assignment && openShiftMode)',
'    return (',
'      <OpenShift',
'        staff={staff}',
'        onShiftOpened={() => window.location.reload()}',
'      />',
'    );',
'',
'  if (!assignment)',
'    return (',
'      <div style={{padding:20}}>',
'        <h2>No Active Pump Assignment</h2>',
'        <button onClick={()=>setOpenShiftMode(true)}>',
'          Open Shift',
'        </button>',
'      </div>',
'    );'
]

lines[start:end] = replacement

path.write_text("\n".join(lines) + "\n")

print("Safe OpenShift line patch completed.")
