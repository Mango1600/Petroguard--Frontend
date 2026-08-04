from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

marker = "async function createShift() {"

insert = """async function createShift() {
    console.log("CREATE SHIFT STARTED", {
      staff: staff?.id,
      pumpId,
      openingMeter
    });
"""

if marker in text:
    text = text.replace(marker, insert, 1)
    file.write_text(text)
    print("Create shift log added")
else:
    print("Marker not found")
