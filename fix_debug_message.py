from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """      {JSON.stringify({
        staff,
        assignment,
        message
      }, null, 2)}"""

new = """      {JSON.stringify({
        staff,
        assignment
      }, null, 2)}"""

if old not in text:
    print("❌ Debug block not found")
else:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ Removed invalid message reference")
