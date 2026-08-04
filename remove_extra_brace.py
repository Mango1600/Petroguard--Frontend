from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

code = code.rstrip()

if code.endswith("}\n}"):
    code = code[:-2]

p.write_text(code + "\n")

print("✅ Extra closing brace removed")
