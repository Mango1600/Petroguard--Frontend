from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

old = '''  validateMeterContinuity(
    currentClosingMeter,
    currentClosingMeter
  );'''

new = '''  if (
    currentClosingMeter === null ||
    currentClosingMeter === undefined
  ) {
    throw new Error("Closing meter required for handover");
  }'''

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Handover meter validation fixed")
else:
    print("⚠️ Validation block not found")

