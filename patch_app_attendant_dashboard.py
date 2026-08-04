from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

text = text.replace(
'import Login from "./pages/Login";',
'import Login from "./pages/Login";\nimport AttendantDashboard from "./pages/AttendantDashboard";'
)

old = '''return (
    <div style={{padding:30}}>
      <h1>✅ LOGIN SUCCESSFUL</h1>
      <p>{staff.email}</p>
      <pre>{JSON.stringify(staff, null, 2)}</pre>
    </div>
  );'''

new = '''return (
    <AttendantDashboard staff={staff} />
  );'''

text = text.replace(old, new)

file.write_text(text)

print("App connected to AttendantDashboard.")
