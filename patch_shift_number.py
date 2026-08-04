from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
text = p.read_text()

old = '<p><b>Status:</b> 🟢 Working</p>'

new = '''<p><b>Status:</b> 🟢 Working</p>
      <p><b>Shift No:</b> {shift?.id}</p>'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Shift number added")
else:
    print("⚠️ Status line not found")
