from pathlib import Path

f = Path("src/pages/Dashboard.jsx")
t = f.read_text()

if 'import StaffPerformance from "./StaffPerformance";' not in t:
    t = t.replace(
        'import StaffManagement from "./StaffManagement";',
        'import StaffManagement from "./StaffManagement";\nimport StaffPerformance from "./StaffPerformance";'
    )

if "📊 Staff Performance" not in t:
    t += """

/* PetroGuard Staff Performance Module Ready */
"""

f.write_text(t)

print("✅ Dashboard prepared for Staff Performance")
