from pathlib import Path
import re

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

# Remove only the leftover rendered text block, not setMessage()
pattern = r'\n\s*✅ Opening Evidence Saved\s*\n\s*</[^>]+>\s*\n\s*\)\}'
code = re.sub(pattern, "", code)

p.write_text(code)

print("✅ Final orphan evidence UI removed")
