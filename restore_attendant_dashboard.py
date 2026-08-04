from pathlib import Path
import shutil

source = Path("src/pages/AttendantDashboard_before_safe_openshift.jsx")
target = Path("src/pages/AttendantDashboard.jsx")

shutil.copy(source, target)

print("AttendantDashboard restored from safe openshift backup.")
