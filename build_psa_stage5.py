from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

if "export async function handoverAssignment" in text:
    print("handoverAssignment already exists")
    raise SystemExit

code = r'''

export async function handoverAssignment({

  assignmentId,
  pumpShiftId,
  currentClosingMeter,
  closingEvidence,
  closingHash = null,
  closingAiVerified = false,
  nextStaffId

}){

  if(!assignmentId)
    throw new Error("assignmentId is required");

  if(!pumpShiftId)
    throw new Error("pumpShiftId is required");

  if(!nextStaffId)
    throw new Error("nextStaffId is required");


  const { data: current, error: currentError } =
    await supabase
      .from("attendant_assignments")
      .select("*")
      .eq("id", assignmentId)
      .single();


  if(currentError)
    throw currentError;


  validateMeterContinuity(
    currentClosingMeter,
    currentClosingMeter
  );


  const now = new Date().toISOString();


  const { error: updateError } =
    await supabase
      .from("attendant_assignments")
      .update({

        status: "HANDED_OVER",

        closing_meter: currentClosingMeter,

        closing_evidence: closingEvidence,

        closing_evidence_time: now,

        handed_over_at: now,

        closing_hash: closingHash,

        closing_ai_verified: closingAiVerified,

        evidence_locked: true

      })
      .eq("id", assignmentId);


  if(updateError)
    throw updateError;


  const nextNo =
    await nextAssignmentNumber(pumpShiftId);


  return await createAssignment({

    pumpShiftId,

    staffId: nextStaffId,

    assignmentNo: nextNo,

    openingMeter: currentClosingMeter,

    openingEvidence: null

  });

}

'''

file.write_text(text + code)

print("pumpShiftAssignment Stage 5 built")
