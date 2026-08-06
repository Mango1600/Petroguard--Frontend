from pathlib import Path

path = Path("src/pages/TankDipEntry.jsx")
text = path.read_text()

text = text.replace(
    'import { uploadEvidence } from "../services/evidenceService";\n',
    ''
)

path.write_text(text)
print("✅ Removed unused uploadEvidence import.")
