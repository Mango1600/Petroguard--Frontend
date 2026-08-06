from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")

text = p.read_text()

text = text.replace(
'console.log("Dashboard staff:", staff);',
'console.log("Dashboard staff FULL:", JSON.stringify(staff, null, 2));'
)

p.write_text(text)

print("✅ Staff full debug added")
