from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
"console.log('Dashboard staff:', staff);\\n    if (!staff?.id) return;",
"""console.log("Dashboard staff:", staff);

    if (!staff?.id) return;"""
)

file.write_text(text)

print("Staff debug syntax fixed")
