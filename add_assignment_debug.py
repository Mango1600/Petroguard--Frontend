from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

marker = "const shift = assignment.pump_shifts;"

debug = '''const shift = assignment.pump_shifts;

return (
  <div style={{padding:20}}>
    <pre style={{
      background:"#ffe",
      border:"1px solid #999",
      padding:"10px",
      fontSize:"11px",
      whiteSpace:"pre-wrap"
    }}>
{JSON.stringify({staff, assignment, shift}, null, 2)}
    </pre>
  </div>
);
'''

if marker in text:
    text = text.replace(marker, debug, 1)
    path.write_text(text)
    print("✅ Debug screen added.")
else:
    print("❌ Could not find insertion point.")
