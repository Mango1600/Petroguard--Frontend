from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

text = text.replace(
'console.log("ASSIGNMENT INSERT RESULT", {data, error});',
'window.__assignmentDebug = {data, error}; console.log("ASSIGNMENT INSERT RESULT", {data, error});'
)

file.write_text(text)

print("Visible assignment debug added")
