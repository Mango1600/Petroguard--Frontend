from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

text = text.replace(
'''return (
    <div style={{padding:30}}>
      <h1>TEST AFTER LOGIN</h1>
      <p>{staff.email}</p>
    </div>
  );''',
'''return (
    <AttendantDashboard staff={staff} />
  );'''
)

file.write_text(text)

print("App restored to AttendantDashboard.")
