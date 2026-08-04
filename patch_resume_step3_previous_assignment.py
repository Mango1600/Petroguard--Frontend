from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

addition = """
async function loadPreviousHandedOverAssignment(pumpShiftId){

  const { data, error } = await supabase
    .from("attendant_assignments")
    .select("*")
    .eq("pump_shift_id", pumpShiftId)
    .eq("status","HANDED_OVER")
    .order("assignment_no", { ascending:false })
    .limit(1)
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}

"""

if "async function loadPreviousHandedOverAssignment" not in text:

    marker = "async function loadOpenPumpShift"

    index = text.find(marker)

    if index != -1:
        end = text.find("\n}\n", index) + 3

        text = text[:end] + "\n" + addition + text[end:]

        file.write_text(text)

        print("Step 3 previous HANDED_OVER assignment loader added.")

    else:
        print("Step 2 loader not found.")

else:
    print("Step 3 already exists.")
