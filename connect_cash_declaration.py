from pathlib import Path

f = Path("src/pages/ClosingVideoEvidence.jsx")
t = f.read_text()

if 'import CashDeclaration' not in t:
    t = t.replace(
        'import CameraCapture from "../components/CameraCapture";',
        'import CameraCapture from "../components/CameraCapture";\nimport CashDeclaration from "./CashDeclaration";'
    )

t = t.replace(
    'return (\n      <CashDeclaration',
    'return (\n      <CashDeclaration'
)

f.write_text(t)

print("✅ CashDeclaration connection checked")
