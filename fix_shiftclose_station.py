from pathlib import Path

file = Path("src/pages/ShiftClose.jsx")

text = file.read_text()

old = "stationId={shift?.station_id || null}"
new = "stationId={shift?.pumps?.station_id || null}"

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ ShiftClose station_id fixed")
else:
    print("⚠️ Pattern not found")
