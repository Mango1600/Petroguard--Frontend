from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

old = """
setMessage("Pump Shift resumed successfully.");
"""

new = """
setMessage("Pump Shift resumed successfully.");

setTimeout(() => {

  if(onResumeSuccess){
    onResumeSuccess();
  }

}, 1000);
"""

if "Pump Shift resumed successfully." in text:

    if text.count("onResumeSuccess") < 1:

        text = text.replace(old,new)
        file.write_text(text)
        print("Step 7 dashboard return added.")

    else:
        print("Dashboard return already exists.")

else:
    print("Resume success message not found.")
