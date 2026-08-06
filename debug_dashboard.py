from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

old = """    if (error) {
      console.log(error);
    }

    setAssignment(data);
"""

new = """    console.log("Dashboard staff:", staff);
    console.log("Active assignment query result:", data);
    console.log("Active assignment query error:", error);

    if (error) {
      console.log(error);
    }

    setAssignment(data);
"""

if old in text:
    p.write_text(text.replace(old, new))
    print("✅ Dashboard debug added.")
else:
    print("❌ Target block not found.")
