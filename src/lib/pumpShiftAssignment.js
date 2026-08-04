import { supabase } from "./supabase";

/*
=========================================
Pump Shift Assignment Service
Stage 1
=========================================
*/

export async function getActiveAssignment(staffId) {

  if (!staffId) {
    throw new Error("staffId is required");
  }

  const { data, error } = await supabase
    .from("attendant_assignments")
    .select(`
      *,
      pump_shifts (
        *,
        pumps (*),
        business_days (*)
      )
    `)
    .eq("staff_id", staffId)
    .eq("status", "ACTIVE")
    .maybeSingle();

  if (error) {
    throw error;
  }

  return data;
}


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

    opening_evidence: openingEvidence ?? "PENDING_OPENING_EVIDENCE",
    assigned_at: now,
    evidence_locked: false

  };

  const { data, error } = await supabase
    .from("attendant_assignments")
    .insert(payload)
    .select()
    .single();

  window.__assignmentDebug = { data, error };
  console.log("ASSIGNMENT INSERT RESULT", { data, error });

  if(error){
    throw error;
  }

  return data;

}



export function validateMeterContinuity(
  previousClosingMeter,
  nextOpeningMeter
){

  if(
    previousClosingMeter === null ||
    previousClosingMeter === undefined
  ){
    throw new Error(
      "Previous closing meter is required"
    );
  }


  if(
    nextOpeningMeter === null ||
    nextOpeningMeter === undefined
  ){
    throw new Error(
      "Next opening meter is required"
    );
  }


  if(
    Number(previousClosingMeter)
    !==
    Number(nextOpeningMeter)
  ){
    throw new Error(
      "Meter continuity failed"
    );
  }


  return true;

}



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

