from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")
text = file.read_text()

text = text.replace(
    'onCapture={(fileUrl) => {',
    'onCapture={(evidenceId) => {'
)

text = text.replace(
    'setClosingEvidence(fileUrl);',
    'setClosingEvidence(evidenceId);'
)

file.write_text(text)

print("✅ AttendantDashboard repaired.")
