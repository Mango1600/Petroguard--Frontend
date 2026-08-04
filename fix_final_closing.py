from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

if not code.rstrip().endswith("}\n"):
    code = code.rstrip() + "\n}\n"

p.write_text(code)

print("✅ Final closing repaired")
