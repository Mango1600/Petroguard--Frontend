from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

text = text.replace(
    '  console.log("ASSIGNMENT PAYLOAD", payload);\n\n',
    ''
)

file.write_text(text)

print("Wrong payload log removed")
