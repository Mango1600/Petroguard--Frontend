from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = 'session: sessionStorage.getItem("supabase.auth.token")'

new = 'session: "Use APP SESSION console output"'

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Debug display fixed")
else:
    print("❌ Old session line not found")
