from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

addition = """
async function createResumeAssignment(
  pumpShiftId,
  staffId,
  openingMeter,
  evidence
){

  const { data:last, error:lastError } = await supabase
    .from("attendant_assignments")
    .select("assignment_no")
    .eq("pump_shift_id", pumpShiftId)
    .order("assignment_no", { ascending:false })
    .limit(1)
    .maybeSingle();


  if(lastError){
    throw lastError;
  }


  const { data, error } = await supabase
    .from("attendant_assignments")
    .insert({

      pump_shift_id: pumpShiftId,
      staff_id: staffId,
      assignment_no: (last?.assignment_no || 0) + 1,
      status: "ACTIVE",
      opening_meter: openingMeter,
      opening_evidence: evidence

    })
    .select()
    .single();


  if(error){
    throw error;
  }


  return data;
}

"""

if "async function createResumeAssignment" not in text:

    marker = "function validateResumeOpeningEvidence"

    index = text.find(marker)

    if index != -1:

        end = text.find("\n}\n", index) + 3

        text = text[:end] + "\n" + addition + text[end:]

        file.write_text(text)

        print("Step 6 ACTIVE assignment creation added.")

    else:
        print("Evidence validation function not found.")

else:
    print("Step 6 already exists.")
