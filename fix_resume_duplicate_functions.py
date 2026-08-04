from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

# Find duplicate function occurrences
functions = [
    "async function getOpenPumpShift",
    "async function getPreviousAssignment"
]

for fn in functions:
    count = text.count(fn)
    print(fn, "count:", count)

print("Review duplicate functions before removal.")
