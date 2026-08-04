from pathlib import Path

path = Path("src/pages/Dashboard.jsx")
text = path.read_text()

# Remove OpenShift import
text = text.replace(
    'import OpenShift from "./OpenShift";\n',
    ""
)

new = """if (staff?.role?.toLowerCase() === "attendant") {
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => window.location.reload()}
      />
    );
  }"""

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

text = text.replace(new, old)

path.write_text(text)
print("Dashboard restored.")
