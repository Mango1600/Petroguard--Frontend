from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

if "export async function createAssignment" in text:
    print("createAssignment already exists")
    raise SystemExit

code = r'''

export async function createAssignment({

  pumpShiftId,
  staffId,
  assignmentNo,
  openingMeter,
  openingEvidence,
  assignedBy

}){

  if(!pumpShiftId) throw new Error("pumpShiftId is required");
  if(!staffId) throw new Error("staffId is required");
  if(assignmentNo===undefined || assignmentNo===null)
    throw new Error("assignmentNo is required");

  const now = new Date().toISOString();

  const payload = {

    pump_shift_id: pumpShiftId,

    staff_id: staffId,

    assignment_no: assignmentNo,

    status: "ACTIVE",

    opening_meter: openingMeter ?? null,

    opening_evidence: openingEvidence ?? null,

    assigned_by: assignedBy ?? null,

    assigned_at: now

  };

  const { data, error } = await supabase
    .from("attendant_assignments")
    .insert(payload)
    .select()
    .single();

  if(error){
    throw error;
  }

  return data;

}

'''

file.write_text(text + code)

print("pumpShiftAssignment Stage 3 built")
