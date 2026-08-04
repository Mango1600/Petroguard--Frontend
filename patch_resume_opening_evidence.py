from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

marker = "function validateOpeningMeter"

insert = r'''

function validateOpeningEvidence(openingEvidence){

  if(
    openingEvidence === null ||
    openingEvidence === undefined ||
    openingEvidence === ""
  ){
    throw new Error(
      "Opening evidence is required before an attendant can resume a Pump Shift."
    );
  }

  return true;
}

'''

if marker in text:
    text = text.replace(marker, insert + "\n\n" + marker, 1)
    FILE.write_text(text)
    print("Opening evidence validation added.")
else:
    print("Target function not found.")
