from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")
text = file.read_text()

text = text.replace(
    'onCapture={(photo) => setEvidence(photo)}',
    'onCapture={(evidenceId) => setEvidence(evidenceId)}'
)

file.write_text(text)

print("✅ ResumeAssignment repaired.")
