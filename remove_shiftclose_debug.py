from pathlib import Path

file = Path("src/pages/ShiftClose.jsx")

text = file.read_text()

# Remove alert debug block
old_alert = '''  alert(JSON.stringify({
    loggedInStaff,
    assignment,
    shift
  }, null, 2));
'''

text = text.replace(old_alert, "")

# Remove visible debug pre block
start = '''      <pre style={{fontSize:12, background:"#eee", padding:10}}>
{JSON.stringify({
  stationId: shift?.station_id,
  uploadedBy: loggedInStaff?.user_id,
  shift: shift,
  assignment: assignment
}, null, 2)}
</pre>
'''

text = text.replace(start, "")

file.write_text(text)

print("✅ ShiftClose debug removed")
