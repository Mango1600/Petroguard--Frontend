from pathlib import Path

p = Path("src/App.jsx")
text = p.read_text()

text = text.replace(
'import Login from "./pages/Login";',
'import Login from "./pages/Login";\nimport Welcome from "./pages/Welcome";'
)

text = text.replace(
'const [page, setPage] = useState("login");',
'const [page, setPage] = useState("login");\n  const [showWelcome, setShowWelcome] = useState(false);'
)

text = text.replace(
'onLogin={setStaff}',
'onLogin={(user) => { setStaff(user); setShowWelcome(true); }}'
)

old = '''  const role = (staff.role || "").toLowerCase();
  console.log("LOGIN STAFF:", staff, "ROLE:", role);
'''

new = '''  if (showWelcome) {
    return (
      <Welcome
        staff={staff}
        continueApp={() => setShowWelcome(false)}
      />
    );
  }

  const role = (staff.role || "").toLowerCase();
  console.log("LOGIN STAFF:", staff, "ROLE:", role);
'''

text = text.replace(old, new)

p.write_text(text)

print("✅ Welcome Page connected")
