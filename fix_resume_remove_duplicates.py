from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

duplicate_previous = """
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

"""

count = text.count(duplicate_previous)

if count > 1:
    text = text.replace(
        duplicate_previous,
        "",
        1
    )

duplicate_pump = """
async function getOpenPumpShift(businessDayId){

  const { data, error } = await supabase
    .from("pump_shifts")
    .select(`
      *,
      pumps(*)
    `)
    .eq("business_day_id", businessDayId)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}

"""

count2 = text.count(duplicate_pump)

if count2 > 1:
    text = text.replace(
        duplicate_pump,
        "",
        1
    )

file.write_text(text)

print("Duplicate Resume functions removed.")
