from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

if "nextAssignmentNumber" in text:
    print("Already exists")
    raise SystemExit

append = r'''

export async function nextAssignmentNumber(pumpShiftId){

  if(!pumpShiftId){
    throw new Error("pumpShiftId is required");
  }

  const { data,error } = await supabase
    .from("attendant_assignments")
    .select("assignment_no")
    .eq("pump_shift_id",pumpShiftId)
    .order("assignment_no",{ascending:false})
    .limit(1);

  if(error){
    throw error;
  }

  if(!data || data.length===0){
    return 1;
  }

  return Number(data[0].assignment_no)+1;

}
'''

file.write_text(text + append)

print("pumpShiftAssignment Stage 2 built")
