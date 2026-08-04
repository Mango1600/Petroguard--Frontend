from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

marker = "export default function ResumeAssignment"

insert = r'''

function validateOpeningMeter(previousClosingMeter, openingMeter){

  if(previousClosingMeter === null || previousClosingMeter === undefined){
    return true;
  }

  if(Number(previousClosingMeter) !== Number(openingMeter)){
    throw new Error(
      "Meter continuity failed. Opening meter must equal previous closing meter."
    );
  }

  return true;
}

'''

if marker in text:
    text = text.replace(marker, insert + "\n\n" + marker, 1)
    FILE.write_text(text)
    print("Meter continuity validation added.")
else:
    print("ResumeAssignment component not found.")
