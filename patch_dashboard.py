#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys

FILE = Path("src/pages/Dashboard.jsx")

if not FILE.exists():
    print("❌ Dashboard.jsx not found.")
    sys.exit(1)

text = FILE.read_text(encoding="utf-8")

backup = FILE.with_suffix(".jsx.bak")
shutil.copy2(FILE, backup)
print(f"✅ Backup created: {backup}")

if "async function loadModulePermissions()" not in text:
    marker = "setStation(data);\n  }\n"

    patch = """

  async function loadModulePermissions() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("module_permissions")
      .select("*")
      .eq("station_id", staff.station_id);

    if (error) {
      console.error("Module permission error:", error);
      return;
    }

    setModulePermissions(data || []);
  }

"""

    if marker in text:
        text = text.replace(marker, marker + patch, 1)
    else:
        print("❌ Could not find insertion point.")
        sys.exit(1)

old = """useEffect(() => {
  loadStation();
  loadStationPolicy();
}, []);"""

new = """useEffect(() => {
  loadStation();
  loadStationPolicy();
  loadModulePermissions();
}, []);"""

text = text.replace(old, new)

FILE.write_text(text, encoding="utf-8")

print("✅ Dashboard patched successfully.")
