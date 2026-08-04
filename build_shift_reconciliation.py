from pathlib import Path
import shutil

p = Path("src/pages/ShiftReconciliation.jsx")

if not p.exists():
    print("❌ ShiftReconciliation.jsx not found")
    raise SystemExit

backup = Path("src/pages/ShiftReconciliation_before_production.jsx")
shutil.copy(p, backup)

text = p.read_text(encoding="utf-8")

text = text.replace(
    "export default function FuelSales() {",
    "export default function ShiftReconciliation() {"
)

text = text.replace(
    "<h2>💰 Daily Receipts / Cash Declaration</h2>",
    """<h2>💰 Shift Reconciliation</h2>

      <h4>Attendant Shift Submission</h4>"""
)

text = text.replace(
    "Save Declaration",
    "✅ Submit Shift"
)

text = text.replace(
    "Previous Declarations",
    "📋 Shift History"
)

p.write_text(text, encoding="utf-8")

print("✅ ShiftReconciliation.jsx updated")
print("✅ Backup created:", backup)