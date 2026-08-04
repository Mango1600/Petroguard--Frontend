from pathlib import Path

p = Path("src/pages/ManagerDashboard.jsx")
text = p.read_text()

text = text.replace(
'''status:"approved",
      approved_at:new Date().toISOString()''',
'''status:"approved",
      approved_at:new Date().toISOString(),
      locked:true,
      locked_at:new Date().toISOString()'''
)

text = text.replace(
'alert("✅ Shift Approved");',
'alert("✅ Shift Approved and Locked 🔒");'
)

p.write_text(text)

print("✅ Shift Lock added")
