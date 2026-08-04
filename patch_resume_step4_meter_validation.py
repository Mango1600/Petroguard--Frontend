from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

addition = """
function validateResumeMeter(previousMeter, openingMeter){

  if(
    Number(openingMeter) !== Number(previousMeter)
  ){
    throw new Error(
      "Opening meter must match previous closing meter."
    );
  }

  return true;
}

"""

if "function validateResumeMeter" not in text:

    marker = "async function loadPreviousHandedOverAssignment"

    index = text.find(marker)

    if index != -1:
        end = text.find("\n}\n", index) + 3

        text = text[:end] + "\n" + addition + text[end:]

        file.write_text(text)

        print("Step 4 meter continuity validation added.")

    else:
        print("Step 3 loader not found.")

else:
    print("Step 4 already exists.")
