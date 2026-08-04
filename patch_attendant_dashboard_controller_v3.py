from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
lines = path.read_text().splitlines()

# Add import if missing
import_line = 'import OpenShift from "./OpenShift";'
if import_line not in lines:
    for i, line in enumerate(lines):
        if 'import CameraCapture' in line:
            lines.insert(i + 1, import_line)
            break

# Replace lines 63-69 (0-based indices 62-68)
start = 62
end = 69

replacement = [
'  if (!assignment)',
'    return (',
'      <OpenShift',
'        staff={staff}',
'        onShiftOpened={() => window.location.reload()}',
'      />',
'    );'
]

lines[start:end] = replacement

path.write_text("\n".join(lines) + "\n")

print("AttendantDashboard controller patched successfully.")
