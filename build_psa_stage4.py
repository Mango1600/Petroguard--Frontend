from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

if "validateMeterContinuity" in text:
    print("Already exists")
    raise SystemExit

code = r'''

export function validateMeterContinuity(
  previousClosingMeter,
  nextOpeningMeter
){

  if(
    previousClosingMeter === null ||
    previousClosingMeter === undefined
  ){
    throw new Error(
      "Previous closing meter is required"
    );
  }


  if(
    nextOpeningMeter === null ||
    nextOpeningMeter === undefined
  ){
    throw new Error(
      "Next opening meter is required"
    );
  }


  if(
    Number(previousClosingMeter)
    !==
    Number(nextOpeningMeter)
  ){
    throw new Error(
      "Meter continuity failed"
    );
  }


  return true;

}

'''

file.write_text(text + code)

print("pumpShiftAssignment Stage 4 built")
