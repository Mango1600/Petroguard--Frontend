from pathlib import Path

# Fix ShiftClose.jsx
shift = Path("src/pages/ShiftClose.jsx")

if shift.exists():
    text = shift.read_text()

    text = text.replace(
        "<CameraCapture />",
        """<CameraCapture
          stationId={shift.station_id}
          companyId={shift.company_id}
          recordId={shift.id}
          staffId={loggedInStaff.id}
        />"""
    )

    shift.write_text(text)
    print("✅ ShiftClose.jsx updated")
else:
    print("❌ ShiftClose.jsx not found")


# Fix CameraCapture.jsx
camera = Path("src/components/CameraCapture.jsx")

if camera.exists():
    text = camera.read_text()

    text = text.replace(
        "export default function CameraCapture() {",
        """export default function CameraCapture({
  stationId,
  companyId,
  recordId,
  staffId
}) {"""
    )

    old_insert = """file_url,
  evidence_type,
  module_name"""

    new_insert = """station_id: stationId,
  company_id: companyId,
  uploaded_by: staffId,
  record_id: recordId,
  file_url,
  evidence_type: "photo",
  module_name: "camera-capture\""""

    text = text.replace(old_insert, new_insert)

    camera.write_text(text)
    print("✅ CameraCapture.jsx updated")
else:
    print("❌ CameraCapture.jsx not found")


print("🎯 Evidence upload patch completed")
