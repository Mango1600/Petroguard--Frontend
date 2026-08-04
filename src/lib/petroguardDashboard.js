import { supabase } from "./supabase";

export async function getDashboardData() {

  const businessDay = await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", 1)
    .order("id", { ascending: false })
    .limit(1)
    .single();

  const attendance = await supabase
    .from("staff_attendance")
    .select("*")
    .eq("station_id", 1);

  const pumps = await supabase
    .from("pump_readings")
    .select("*")
    .eq("station_id", 1)
    .order("id", { ascending: false })
    .limit(5);

  const tanks = await supabase
    .from("tank_readings")
    .select("*")
    .eq("station_id", 1)
    .order("id", { ascending: false })
    .limit(5);

  const reconciliation = await supabase
    .from("daily_reconciliation")
    .select("*")
    .eq("station_id", 1)
    .order("id", { ascending: false })
    .limit(1)
    .single();

  return {
    businessDay: businessDay.data,
    attendance: attendance.data,
    pumps: pumps.data,
    tanks: tanks.data,
    reconciliation: reconciliation.data
  };
}