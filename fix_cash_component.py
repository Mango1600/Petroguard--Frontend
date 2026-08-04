from pathlib import Path

file = Path("src/pages/CashDeclaration.jsx")

text = file.read_text()

text = text.replace(
    "export default function ShiftReconciliation({ onBack })",
    "export default function CashDeclaration({ onBack })"
)

file.write_text(text)

print("✅ CashDeclaration component name fixed")
