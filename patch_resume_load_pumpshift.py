from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

marker = "return data;\n}\n"

insert = r'''

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

'''

if marker in text:
    text = text.replace(marker, marker + insert, 1)
    FILE.write_text(text)
    print("Open Pump Shift loader added.")
else:
    print("Target location not found.")
