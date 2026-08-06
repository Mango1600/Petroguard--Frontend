from pathlib import Path
import shutil

files = [
    ("src/pages/ShiftClose.backup.jsx", "src/pages/ShiftClose.jsx"),
    ("src/components/VideoCapture.backup.jsx", "src/components/VideoCapture.jsx"),
    ("src/pages/AttendantDashboard.crash.backup.jsx", "src/pages/AttendantDashboard.jsx"),
]

for src, dst in files:
    if Path(src).exists():
        shutil.copy(src, dst)
        print(f"Restored {dst}")
    else:
        print(f"Backup not found: {src}")

Path("src/services/auditService.js").write_text("""export async function createAuditLog() {
  return true;
}
""")

print("Done.")
