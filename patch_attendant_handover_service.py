from pathlib import Path

file = Path("src/pages/AttendantHandover.jsx")

text = file.read_text()

# replace imports
text = text.replace(
'import { supabase } from "../lib/supabase";',
'import { handoverAssignment } from "../lib/pumpShiftAssignment";'
)

# replace old handover function
start = text.find("  async function handover(){")
end = text.find("  if(done){")

if start == -1 or end == -1:
    print("handover function block not found")
    raise SystemExit

new_function = r'''
  async function handover(){

    if(!staffId){
      alert("Incoming staff required");
      return;
    }

    try {

      await handoverAssignment({

        assignmentId: shift.assignment_id,

        pumpShiftId: shift.id,

        currentClosingMeter: shift.closing_meter,

        closingEvidence: openingEvidence,

        nextStaffId: Number(staffId)

      });

      setDone(true);

    } catch(error){

      console.log(error);

      alert(error.message);

    }

  }

'''

text = text[:start] + new_function + text[end:]

file.write_text(text)

print("AttendantHandover service patch complete")
