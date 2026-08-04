from pathlib import Path
import shutil
import sys

f = Path("src/pages/Dashboard.jsx")

if not f.exists():
    print("Dashboard.jsx not found.")
    sys.exit(1)

text = f.read_text(encoding="utf-8")

backup = f.with_suffix(".jsx.canaccess.bak")
shutil.copy2(f, backup)

old = """  function canAccess(task) {
    if (!policy || !staff) return false;

    const role = staff.role.toLowerCase();

    return policy[task + "_role"] === role;
  }"""

new = """  function canAccess(moduleName) {
    if (!staff) return false;

    if (staff.role.toLowerCase() == "developer") return true;

    const permission = modulePermissions.find(
      (m) => m.module_name === moduleName
    );

    if (!permission) return false;

    return permission.allowed_roles.includes(staff.role.toLowerCase());
  }"""

if old not in text:
    print("Old canAccess() not found.")
    sys.exit(1)

text = text.replace(old, new)

f.write_text(text, encoding="utf-8")

print("✅ canAccess patched successfully.")
