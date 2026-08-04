from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

old = """await createAssignment({"""

new = """console.log("BEFORE CREATE ASSIGNMENT", {
  pumpShiftId: pumpShift.id,
  staffId: staff.id
});

await createAssignment({"""

if old in text:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("OpenShift assignment log added")
else:
    print("Target not found")
