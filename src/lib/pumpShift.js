import { supabase } from "./supabase";

export async function getOpenPumpShift(pumpId){
  return await supabase
    .from("pump_shifts")
    .select("*")
    .eq("pump_id", pumpId)
    .eq("status","OPEN")
    .maybeSingle();
}


export async function nextShiftNumber(businessDayId){

  const { data, error } = await supabase
    .from("pump_shifts")
    .select("shift_no")
    .eq("business_day_id", businessDayId)
    .order("shift_no", { ascending:false })
    .limit(1)
    .maybeSingle();

  if(error){
    throw error;
  }

  return data ? Number(data.shift_no) + 1 : 1;

}


export async function createPumpShift({

  businessDayId,
  pumpId,
  openingMeter,
  openingEvidence,
  staffId

}){

  const shiftNo = await nextShiftNumber(businessDayId);

  const { data, error } = await supabase
    .from("pump_shifts")
    .insert({

      business_day_id: businessDayId,

      pump_id: pumpId,

      shift_no: shiftNo,

      status:"OPEN",

      opening_meter: openingMeter,

      opening_evidence: openingEvidence ?? null,

      opened_by_staff_id: staffId,

      opened_at: new Date().toISOString()

    })
    .select()
    .single();


  if(error){
    throw error;
  }


  return data;

}

