from pathlib import Path

file = Path("src/pages/BusinessDayClose.jsx")

text = file.read_text()

text = text.replace(
    "closing_evidence:\n                    evidence,",
    "closing_evidence:\n                    null,"
)

file.write_text(text)

print("✅ BusinessDayClose.jsx repaired.")
