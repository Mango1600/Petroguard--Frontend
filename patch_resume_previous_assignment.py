from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

marker = "return data;\n}\n"

insert = r'''

async function getPreviousAssignment(pumpShiftId){

  const { data, error } = await supabase
    .from("attendant_assignments")
    .select("*")
    .eq("pump_shift_id", pumpShiftId)
    .eq("status", "HANDED_OVER")
    .order("assignment_no", { ascending: false })
    .limit(1)
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}

'''

if marker in text:
    text = text.replace(marker, marker + insert, 1)
    FILE.write_text(text)
    print("Previous HANDED_OVER assignment loader added.")
else:
    print("Target location not found.")
