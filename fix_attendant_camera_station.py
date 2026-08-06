from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")

text = p.read_text()

old = '''<CameraCapture
        label="Closing Evidence"
        onCapture={(evidenceId) => {
          setClosingEvidence(evidenceId);
          setEvidenceVerified(true);
        }}
      />'''

new = '''<CameraCapture
        title="Closing Evidence"
        stationId={staff?.station_id}
        uploadedBy={staff?.id}
        recordId={assignment?.pump_shift_id}
        moduleName="pump_shift"
        onCapture={(evidenceId) => {
          setClosingEvidence(evidenceId);
          setEvidenceVerified(true);
        }}
      />'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ CameraCapture station props added.")
else:
    print("Nothing patched.")
