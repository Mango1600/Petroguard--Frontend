from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """async function loadPumpShift() {
    console.log("Dashboard staff FULL:", JSON.stringify(staff, null, 2));"""

new = """async function loadPumpShift() {
    const { data: sessionData } = await supabase.auth.getSession();
    console.log("SUPABASE SESSION:", sessionData);

    console.log("Dashboard staff FULL:", JSON.stringify(staff, null, 2));"""

if old in text:
    file.write_text(text.replace(old, new, 1))
    print("✅ Session debug added")
else:
    print("❌ Target not found")
