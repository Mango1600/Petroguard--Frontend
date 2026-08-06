from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
text = p.read_text()

text = text.replace(
'''export default function CameraCapture({
  onCapture,
  title = "Evidence Capture"
}) {''',
'''export default function CameraCapture({
  onCapture,
  title = "Evidence Capture",
  stationId = null,
  uploadedBy = null,
  recordId = null,
  moduleName = "camera_capture"
}) {'''
)

text = text.replace(
'''moduleName: "camera_capture",
      evidenceType: "PHOTO"''',
'''moduleName,
      evidenceType: "PHOTO",
      stationId,
      uploadedBy,
      recordId'''
)

p.write_text(text)

print("✅ CameraCapture station support added")
