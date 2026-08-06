from pathlib import Path

file = Path("src/pages/TankDipEntry.jsx")
text = file.read_text()

text = text.replace(
    'onCapture={(image) => setEvidenceImage(image)}',
    'onCapture={(evidenceId) => setEvidenceImage(evidenceId)}'
)

file.write_text(text)

print("✅ TankDipEntry callback repaired.")
