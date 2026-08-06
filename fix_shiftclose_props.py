from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")

s = p.read_text()

old = """<ShiftClose
      loggedInStaff={staff}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />"""

new = """<ShiftClose
      loggedInStaff={staff}
      assignment={assignment}
      shift={shift}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />"""

if old not in s:
    raise SystemExit("Target not found")

p.write_text(s.replace(old, new))

print("ShiftClose props patched")
