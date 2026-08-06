from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")

s = p.read_text()

s = s.replace(
"export default function ShiftClose({ onComplete }) {",
"export default function ShiftClose({ onComplete, loggedInStaff, assignment, shift }) {"
)

old = """<CameraCapture
            label="Closing Evidence"
            onCapture={(evidenceId) => { setPhoto(evidenceId); setPhotoDone(true); }}
          />"""

new = """<CameraCapture
            title="Closing Evidence"
            stationId={shift?.station_id || null}
            uploadedBy={loggedInStaff?.id || null}
            recordId={assignment?.pump_shift_id || null}
            moduleName="SHIFT_CLOSE"
            onCapture={(evidenceId) => { setPhoto(evidenceId); setPhotoDone(true); }}
          />"""

if old not in s:
    raise SystemExit("CameraCapture block not found")

s = s.replace(old, new)

p.write_text(s)

print("ShiftClose evidence props patched")
