from pathlib import Path

p = Path("src/App.jsx")
t = p.read_text()

if 'ManagerDashboard' not in t:
    t = t.replace(
        'import Dashboard from "./pages/Dashboard";',
        'import Dashboard from "./pages/Dashboard";\nimport ManagerDashboard from "./pages/ManagerDashboard";\nimport AttendantDashboard from "./pages/AttendantDashboard";'
    )

p.write_text(t)

print("✅ Dashboard imports restored")
