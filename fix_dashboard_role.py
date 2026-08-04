from pathlib import Path
import re

dashboard = Path("src/pages/Dashboard.jsx")

if not dashboard.exists():
    print("❌ Dashboard.jsx not found")
    raise SystemExit

text = dashboard.read_text(encoding="utf-8")

# List of modules attendants must not see
restricted = [
    "Manager Dashboard",
    "Staff Management",
    "Station Management",
    "Pump Management",
    "Tank Management",
    "Fuel Price Management",
    "Fuel Delivery Management",
    "Inventory Management",
    "Alerts & Fraud Monitoring",
]

# Replace every occurrence with a role check
for name in restricted:
    pattern = rf'Open {re.escape(name)}'
    replacement = (
        '{staff?.role !== "Attendant" && <>'
        f'Open {name}'
        '</>}'
    )
    text = re.sub(pattern, replacement, text)

dashboard.write_text(text, encoding="utf-8")

print("✅ Dashboard updated.")
print("Attendants will no longer see Manager/Admin modules.")
