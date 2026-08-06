from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

old = 'setMessage("Auth OK - Loading staff...");'
new = 'setMessage("MARKER 2026 - BEFORE STAFF QUERY");'

if old in text:
    text = text.replace(old, new, 1)
    p.write_text(text)
    print("✅ Marker inserted")
else:
    print("❌ Marker not found")
