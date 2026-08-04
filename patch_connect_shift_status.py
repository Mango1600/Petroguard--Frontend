from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

# Import ShiftStatus
if 'import ShiftStatus from "./ShiftStatus";' not in text:
    text = text.replace(
        'import OpenShift from "./OpenShift";',
        'import OpenShift from "./OpenShift";\nimport ShiftStatus from "./ShiftStatus";'
    )

# Add new page state
text = text.replace(
    'const [page, setPage] = useState("home");',
    'const [page, setPage] = useState("shiftStatus");'
)

# Replace open page rendering with ShiftStatus
old = '''  if (page === "open")
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => setPage("attendantPump")}
      />
    );
'''

new = '''  if (page === "shiftStatus")
    return (
      <ShiftStatus
        staff={staff}
        onOpenShift={() => setPage("open")}
        onContinueShift={() => setPage("attendantPump")}
        onHandover={() => setPage("attendantPump")}
      />
    );

  if (page === "open")
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => setPage("attendantPump")}
      />
    );
'''

text = text.replace(old, new)

p.write_text(text)
print("✅ Shift Status connected")
