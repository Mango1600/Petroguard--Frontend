from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

if "restoreOpeningEvidence" in code:
    print("✅ Already installed")
    raise SystemExit

# Run on page load
code = code.replace(
    "useEffect(() => {",
    """useEffect(() => {
    restoreOpeningEvidence();
"""
)

# Add function before saveEvidence()
marker = "async function saveEvidence"

func = """
async function restoreOpeningEvidence(){

  const { data } = await supabase
    .from("evidence_links")
    .select("record_id,evidence_id")
    .eq("module_name","opening_shift")
    .eq("record_id",String(shift.id))
    .limit(1);

  if(data && data.length){
    setOpeningEvidenceDone(true);
  }

}

"""

code = code.replace(marker, func + "\n" + marker)

p.write_text(code)

print("✅ Opening evidence restore installed")
