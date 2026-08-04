from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

old = """{!evidenceSaved ? (
        {!openingEvidenceDone ? ("""

new = """{!openingEvidenceDone ? ("""

if old in code:
    code = code.replace(old, new)
    p.write_text(code)
    print("✅ Nested JSX condition fixed")
else:
    print("❌ Pattern not found")
