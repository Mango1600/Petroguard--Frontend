from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
'import CameraCapture from "../components/CameraCapture";',
'import CameraCapture from "../components/CameraCapture";\nimport { handoverAssignment } from "../lib/pumpShiftAssignment";'
)

start = text.find("  async function handleHandover() {")
end = text.find("\n\n  return (", start)

if start == -1 or end == -1:
    print("handleHandover block not found")
    raise SystemExit

new_function = r'''
  async function handleHandover() {

    if (!evidenceVerified) {
      alert("Capture and verify closing evidence first.");
      return;
    }

    if (!closingMeter) {
      alert("Closing meter required.");
      return;
    }


    try {

      await handoverAssignment({

        assignmentId: assignment.id,

        pumpShiftId: assignment.pump_shift_id,

        currentClosingMeter: Number(closingMeter),

        closingEvidence,

        nextStaffId: assignment.staff_id

      });


      loadPumpShift();


    } catch(error) {

      console.log(error);

      alert(error.message);

    }

  }
'''

text = text[:start] + new_function + text[end:]

file.write_text(text)

print("AttendantDashboard service integration complete")
