from pathlib import Path

p = Path("src/services/evidenceService.js")

s = p.read_text()

old = 'alert("Evidence Error: " + JSON.stringify(error));'
new = 'alert("Evidence Error: " + JSON.stringify(error, null, 2));'

if old not in s:
    raise SystemExit("Target line not found")

p.write_text(s.replace(old, new))

print("✅ Evidence error message patched")
