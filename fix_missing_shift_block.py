from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

old = """
  if (!shift) {


async function saveAndStartShift() {
"""

new = """
  if (!shift) {
    return (
      <div style={{padding:20}}>
        <h2>⛽ Pump Reading</h2>
        <p>No active shift found.</p>
      </div>
    );
  }


async function saveAndStartShift() {
"""

if old in code:
    code = code.replace(old,new)
    p.write_text(code)
    print("✅ Missing shift loading block restored")
else:
    print("❌ Pattern not found")
