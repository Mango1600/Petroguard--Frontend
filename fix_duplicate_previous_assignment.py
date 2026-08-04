from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

start = "async function getPreviousAssignment(pumpShiftId){"

first = text.find(start)

if first == -1:
    print("Function not found.")
    exit()

second = text.find(start, first + 1)

if second == -1:
    print("No duplicate found.")
    exit()

# Find end of second function by locating next closing pattern
end_marker = "\n}\n"

end = text.find(end_marker, second)

if end == -1:
    print("Could not locate duplicate end.")
    exit()

end = end + len(end_marker)

text = text[:second] + text[end:]

file.write_text(text)

print("Duplicate getPreviousAssignment removed.")
