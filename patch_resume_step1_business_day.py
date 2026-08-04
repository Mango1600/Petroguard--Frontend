from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

marker = "useEffect(()=>{"

addition = """
async function loadOpenBusinessDay(){

  const { data, error } = await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", loggedInStaff.station_id)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}

"""

if "async function loadOpenBusinessDay" not in text:

    text = text.replace(
        marker,
        addition + marker
    )

    file.write_text(text)

    print("Step 1 OPEN Business Day loader added.")

else:
    print("Step 1 already exists.")
