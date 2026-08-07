from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")

text = p.read_text()

old = """<CameraCapture
  onCapture={(evidenceId) => { setPhoto(evidenceId); setPhotoDone(true); }}
/>"""

new = """<CameraCapture
  stationId={shift.station_id}
  recordId={shift.id}
  uploadedBy={loggedInStaff.id}
  moduleName="shift_close"
  onCapture={(evidenceId) => {
    setPhoto(evidenceId);
    setPhotoDone(true);
  }}
/>"""

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ ShiftClose camera props fixed")
else:
    print("❌ Target CameraCapture block not found")
