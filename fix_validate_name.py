from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
text = p.read_text()

text = text.replace(
    "validateOpeningEvidence(",
    "validateResumeOpeningEvidence("
)

p.write_text(text)
print("✅ Fixed validateOpeningEvidence → validateResumeOpeningEvidence")
