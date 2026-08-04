from pathlib import Path
import shutil

app = Path("src/App.jsx")

if not app.exists():
    print("❌ src/App.jsx not found")
    raise SystemExit

backup = Path("src/App_before_shift_submission.py_backup.jsx")
shutil.copy(app, backup)

text = app.read_text(encoding="utf-8")

# Add import
import_line = 'import ShiftSubmission from "./pages/ShiftSubmission";'
if import_line not in text:
    imports = text.splitlines()
    last_import = 0
    for i, line in enumerate(imports):
        if line.startswith("import "):
            last_import = i
    imports.insert(last_import + 1, import_line)
    text = "\n".join(imports)

# Add route
old = """  return (
  <Dashboard staff={staff} />
);
"""

new = """  if (page === "shiftSubmission") {
    return <ShiftSubmission staff={staff} />;
  }

  return (
    <Dashboard staff={staff} />
  );
"""

if 'page === "shiftSubmission"' not in text:
    text = text.replace(old, new)

app.write_text(text, encoding="utf-8")

print("✅ App.jsx updated successfully.")
print("✅ Backup created:", backup)
print("🚀 Restart with: npm run dev")

