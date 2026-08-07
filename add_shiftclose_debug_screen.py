from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")

text = p.read_text()

old = '''{console.log("SHIFT CLOSE DEBUG", {
        shift,
        assignment,
        stationId: shift?.station_id,
        uploadedBy: loggedInStaff?.id
      })}'''

new = '''<pre style={{fontSize:12, background:"#eee", padding:10}}>
{JSON.stringify({
  stationId: shift?.station_id,
  uploadedBy: loggedInStaff?.id,
  shift: shift,
  assignment: assignment
}, null, 2)}
</pre>'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Phone debug display added")
else:
    print("❌ Debug block not found")
