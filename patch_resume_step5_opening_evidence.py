from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

addition = """
function validateResumeOpeningEvidence(evidence){

  if(!evidence){

    throw new Error(
      "Opening evidence is required before resuming assignment."
    );

  }

  return true;
}

"""

if "function validateResumeOpeningEvidence" not in text:

    marker = "function validateResumeMeter"

    index = text.find(marker)

    if index != -1:

        end = text.find("\n}\n", index) + 3

        text = text[:end] + "\n" + addition + text[end:]

        file.write_text(text)

        print("Step 5 opening evidence validation added.")

    else:
        print("Meter validation function not found.")

else:
    print("Step 5 already exists.")
