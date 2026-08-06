from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
    "opening_meter_photo: openingEvidence,",
    "opening_meter_photo: null,"
)

text = text.replace(
    "closing_meter_photo: closingEvidence,",
    "closing_meter_photo: null,"
)

file.write_text(text)

print("✅ PumpReadings.jsx repaired.")
