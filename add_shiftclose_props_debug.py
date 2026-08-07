from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")
s = p.read_text()

old = 'export default function ShiftClose({ onComplete, loggedInStaff, assignment, shift }) {'

new = '''export default function ShiftClose({ onComplete, loggedInStaff, assignment, shift }) {
  console.log("SHIFT CLOSE PROPS DEBUG", {
    loggedInStaff,
    assignment,
    shift
  });'''

if old in s:
    s = s.replace(old, new)
    p.write_text(s)
    print("✅ Debug added")
else:
    print("❌ Function line not found")
