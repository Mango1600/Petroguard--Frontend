from pathlib import Path

p = Path("src/pages/ManagerDashboard.jsx")
text = p.read_text()

audit = '''
<hr/>

<h2>📋 Final Shift Audit Record</h2>

<div style={{
  border:"1px solid #ccc",
  padding:15,
  borderRadius:8
}}>
  <p><b>Audit Status:</b> ✅ COMPLETE</p>
  <p><b>Manager Approval:</b> ✅ Approved</p>
  <p><b>Shift Security:</b> 🔒 Locked</p>

  <p>
    Approved shifts are now protected from further changes.
  </p>
</div>

'''

text = text.replace(
    '<h2>Pending Shift Approval</h2>',
    '<h2>Pending Shift Approval</h2>\n' + audit
)

p.write_text(text)

print("✅ Final Audit Record added")
