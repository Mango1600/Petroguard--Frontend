from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

old = """if(Number(openingMeter)!==Number(previousMeter))
return setMessage("Meter must match previous closing");

if(!evidence)
return setMessage("Opening evidence required");
"""

new = """try{

validateOpeningEvidence(evidence);

validateOpeningMeter(
previousMeter,
openingMeter
);

}catch(err){

return setMessage(err.message);

}
"""

if old in text:
    text = text.replace(old,new,1)
    FILE.write_text(text)
    print("Resume validation connected.")
else:
    print("Validation block not found.")
