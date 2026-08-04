from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

# Add OpenShift import if missing
if 'import OpenShift from "./OpenShift";' not in text:
    text = text.replace(
        'import CameraCapture from "../components/CameraCapture";',
        'import CameraCapture from "../components/CameraCapture";\nimport OpenShift from "./OpenShift";'
    )

old = """  if (!assignment)
    return (
      <div style={{padding:20}}>
        <h2>No Active Pump Assignment</h2>
      </div>
    );"""

new = """  if (!assignment) {
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => window.location.reload()}
      />
    );
  }"""

if old not in text:
    print("Target block not found.")
    raise SystemExit

text = text.replace(old, new)

path.write_text(text)

print("AttendantDashboard patched successfully.")
