from pathlib import Path
import shutil

backup = Path("src/App_before_test.jsx")
app = Path("src/App.jsx")

if backup.exists():
    shutil.copy(backup, app)
    print("✅ Original App.jsx restored.")
else:
    print("❌ Backup not found.")
