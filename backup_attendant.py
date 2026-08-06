from pathlib import Path
import shutil

shutil.copy(
    "src/pages/AttendantDashboard.jsx",
    "src/pages/AttendantDashboard.crash.backup.jsx"
)

print("AttendantDashboard backup created")
