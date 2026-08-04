from pathlib import Path

f = Path("src/pages/Dashboard.jsx")
text = f.read_text()

old = """  return (
    <div>"""

new = """  if (staff?.role?.toLowerCase() === "attendant") {
    return (
      <AttendantDashboard staff={staff} />
    );
  }

  return (
    <div>"""

if old not in text:
    print("❌ Could not find the return statement.")
    raise SystemExit

text = text.replace(old, new, 1)

# Add import if missing
if 'import AttendantDashboard' not in text:
    lines = text.splitlines()
    insert_at = 0
    for i, line in enumerate(lines):
        if line.startswith("import"):
            insert_at = i + 1
    lines.insert(insert_at, 'import AttendantDashboard from "./AttendantDashboard";')
    text = "\n".join(lines)

f.write_text(text)

print("✅ Dashboard patched successfully.")
