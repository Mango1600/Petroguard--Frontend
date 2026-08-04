from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

old = """
import { supabase } from "../lib/supabase";
"""

new = """
import { supabase } from "../lib/supabase";

async function getOpenBusinessDay(stationId){

  const { data, error } = await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", stationId)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}
"""

if old not in text:
    print("Import block not found.")
else:
    text = text.replace(old, new)
    FILE.write_text(text)
    print("Open Business Day loader added.")
