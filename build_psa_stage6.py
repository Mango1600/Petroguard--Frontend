from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

if "export async function closeAssignment" in text:
    print("closeAssignment already exists")
    raise SystemExit

code = r'''

export async function closeAssignment({

  assignmentId,
  closingMeter,
  closingEvidence,
  closingHash = null,
  closingAiVerified = false

}){

  if(!assignmentId)
    throw new Error("assignmentId is required");

  if(closingMeter === undefined || closingMeter === null)
    throw new Error("closingMeter is required");


  const now = new Date().toISOString();


  const { data, error } = await supabase
    .from("attendant_assignments")
    .update({

      status: "CLOSED",

      closing_meter: closingMeter,

      closing_evidence: closingEvidence ?? null,

      closing_evidence_time: now,

      closing_hash: closingHash,

      closing_ai_verified: closingAiVerified,

      evidence_locked: true

    })
    .eq("id", assignmentId)
    .select()
    .single();


  if(error)
    throw error;


  return data;

}

'''

file.write_text(text + code)

print("pumpShiftAssignment Stage 6 built")
