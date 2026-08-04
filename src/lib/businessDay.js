import { supabase } from "./supabase";

export async function getOpenBusinessDay(stationId) {
  return await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", stationId)
    .eq("status", "OPEN")
    .maybeSingle();
}

export async function openBusinessDay(stationId, userId) {
  const today = new Date().toISOString().slice(0, 10);

  const { data: existing } = await getOpenBusinessDay(stationId);

  if (existing) {
    throw new Error("Business Day already open.");
  }

  return await supabase.from("business_days").insert({
    station_id: stationId,
    business_date: today,
    status: "OPEN",
    opened_by: userId,
  });
}

export async function closeBusinessDay(businessDayId, userId) {
  return await supabase
    .from("business_days")
    .update({
      status: "CLOSED",
      closed_by: userId,
      closed_at: new Date().toISOString(),
    })
    .eq("id", businessDayId);
}
