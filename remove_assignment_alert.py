from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

old = 'window.__assignmentDebug = {data, error}; alert("Assignment Result: " + JSON.stringify({data, error})); console.log("ASSIGNMENT INSERT RESULT", {data, error});'

new = '''window.__assignmentDebug = { data, error };
  console.log("ASSIGNMENT INSERT RESULT", { data, error });'''

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("Assignment alert removed successfully")
else:
    print("Target debug line not found")
