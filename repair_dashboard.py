from pathlib import Path

f = Path("src/pages/Dashboard.jsx")
text = f.read_text()

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Manager Dashboard</>}"',
    '"Open Manager Dashboard"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Staff Management</>}"',
    '"Open Staff Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Station Management</>}"',
    '"Open Station Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Pump Management</>}"',
    '"Open Pump Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Tank Management</>}"',
    '"Open Tank Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Fuel Price Management</>}"',
    '"Open Fuel Price Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Fuel Delivery Management</>}"',
    '"Open Fuel Delivery Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Inventory Management</>}"',
    '"Open Inventory Management"'
)

text = text.replace(
    '"{staff?.role !== "Attendant" && <>Open Alerts & Fraud Monitoring</>}"',
    '"Open Alerts & Fraud Monitoring"'
)

f.write_text(text)
print("✅ Dashboard.jsx repaired.")
