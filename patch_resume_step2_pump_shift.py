from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

addition = """
async function loadOpenPumpShift(businessDayId){

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

if "async function loadOpenPumpShift" not in text:

    insert_point = "async function loadOpenBusinessDay"

    index = text.find(insert_point)

    if index != -1:
        end = text.find("\n}\n", index) + 3
        text = text[:end] + "\n" + addition + text[end:]

        file.write_text(text)
        print("Step 2 OPEN Pump Shift loader added.")
    else:
        print("Business Day loader not found.")

else:
    print("Step 2 already exists.")
