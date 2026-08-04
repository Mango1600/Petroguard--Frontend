from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
text = p.read_text()

old = '''<p><b>Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_id}</p>'''

new = '''<p><b>Opened By:</b> {staff?.name}</p>
      <p><b>Current Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_id}</p>'''

if old in text:
    text = text.replace(old,new)
    p.write_text(text)
    print("✅ Station shift display adjusted")
else:
    print("⚠️ Display block not found")
