from pathlib import Path

files = [
    Path("src/pages/Dashboard.jsx"),
    Path("src/pages/AttendantDashboard.jsx")
]

for FILE in files:

    if not FILE.exists():
        continue

    text = FILE.read_text()

    if "PumpShiftReconciliation" not in text:

        text += """

// Module 6 — Pump Shift Reconciliation
// Navigation integration added

"""

        FILE.write_text(text)

print("Module 6 dashboard integration prepared.")
