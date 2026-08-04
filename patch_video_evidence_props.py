from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
text = p.read_text()

text = text.replace(
"export default function VideoCapture({ onComplete }) {",
"""export default function VideoCapture({
  onComplete,
  shiftId,
  stationId,
  staffId,
  evidenceType
}) {"""
)

p.write_text(text)

print("✅ VideoCapture evidence props added")
