from pathlib import Path

Path("src/lib").mkdir(exist_ok=True)

code = r'''import { supabase } from "./supabase";

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
'''

Path("src/lib/pumpShiftAssignment.js").write_text(code)

print("pumpShiftAssignment Stage 1 built")
