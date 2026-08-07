from pathlib import Path

path = Path("src/pages/ShiftClose.jsx")
text = path.read_text(encoding="utf-8")

old = '''  console.log("SHIFT CLOSE PROPS DEBUG", {
    loggedInStaff,
    assignment,
    shift
  });'''

new = '''  alert(JSON.stringify({
    loggedInStaff,
    assignment,
    shift
  }, null, 2));'''

if old in text:
    text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")
    print("✅ Alert debug added.")
else:
    print("❌ Debug block not found.")
