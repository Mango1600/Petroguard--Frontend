from pathlib import Path

path = Path("src/pages/Dashboard.jsx")
text = path.read_text()

# Import OpenShift
if 'import OpenShift from "./OpenShift";' not in text:
    text = text.replace(
        'import AttendantDashboard from "./AttendantDashboard";',
        'import AttendantDashboard from "./AttendantDashboard";\nimport OpenShift from "./OpenShift";'
    )

old = """if (staff?.role?.toLowerCase() === "attendant") {
    return (
      <AttendantDashboard
        staff={staff}
        openSales={(context) => {
          setSalesContext(context);
          setShowFuelSales(true);
        }}
      />
    );
  }"""

new = """if (staff?.role?.toLowerCase() === "attendant") {
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => window.location.reload()}
      />
    );
  }"""

if old not in text:
    print("Target block not found.")
    raise SystemExit

text = text.replace(old, new)

path.write_text(text)

print("Dashboard patched successfully.")
