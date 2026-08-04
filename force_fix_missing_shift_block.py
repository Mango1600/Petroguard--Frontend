from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

target = "  if (!shift) {\n\n\nasync function saveAndStartShift() {"

replacement = """  if (!shift) {
    return (
      <div style={{padding:20}}>
        <h2>⛽ Pump Reading</h2>
        <p>No active shift found.</p>
      </div>
    );
  }


async function saveAndStartShift() {"""

if target in code:
    code = code.replace(target, replacement)
    p.write_text(code)
    print("✅ Shift block fixed")
else:
    # fallback using position
    start = code.find("  if (!shift) {")
    end = code.find("async function saveAndStartShift()", start)

    if start != -1 and end != -1:
        code = code[:start] + replacement + code[end + len("async function saveAndStartShift() {"):]
        p.write_text(code)
        print("✅ Shift block fixed by position")
    else:
        print("❌ Could not locate block")
