from pathlib import Path
import shutil
import sys

f = Path("src/pages/TankReadings.jsx")

if not f.exists():
    print("TankReadings.jsx not found.")
    sys.exit(1)

text = f.read_text(encoding="utf-8")

backup = f.with_suffix(".jsx.variance.bak")
shutil.copy2(f, backup)

old = """  function getVariance(variance) {
    if (variance < 0) {"""

new = """  function getVariance(variance) {
    if (variance === null || variance === undefined) {
      return {
        label: "🟡 Incomplete Draft",
        note: "Waiting for opening volume and expected volume",
      };
    }

    if (variance < 0) {"""

if old not in text:
    print("Target code not found.")
    sys.exit(1)

text = text.replace(old, new, 1)

f.write_text(text, encoding="utf-8")

print("✅ Tank variance display patched successfully.")
