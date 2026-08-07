from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")

text = p.read_text()

marker = '<div style={{padding:20}}>'

insert = '''<div style={{padding:20}}>
      {console.log("SHIFT CLOSE DEBUG", {
        shift,
        assignment,
        stationId: shift?.station_id,
        uploadedBy: loggedInStaff?.id
      })}
'''

if marker in text:
    text = text.replace(marker, insert, 1)
    p.write_text(text)
    print("✅ Debug added to ShiftClose.jsx")
else:
    print("❌ Marker not found")
