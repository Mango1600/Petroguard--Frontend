from pathlib import Path

f = Path("src/pages/CashDeclaration.jsx")
t = f.read_text()

t = t.replace(
"export default function CashDeclaration({ onBack }) {",
"""export default function CashDeclaration({
  onBack,
  shift,
  openingMeter,
  closingMeter,
  litresSold,
  closingVideo
}) {"""
)

f.write_text(t)

print("✅ CashDeclaration now receives shift data")
