from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
text = p.read_text()

replacements = {
    "validateOpeningMeter(": "validateResumeMeter(",
    "validateOpeningEvidence(": "validateResumeOpeningEvidence(",
}

for old, new in replacements.items():
    text = text.replace(old, new)

p.write_text(text)
print("✅ ResumeAssignment validation names fixed.")
