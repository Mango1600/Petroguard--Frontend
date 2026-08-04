from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

old = """await createAssignment({
                                                          pumpShiftId: pumpShift.id,"""

new = """const newAssignment = await createAssignment({
                                                          pumpShiftId: pumpShift.id,"""

text = text.replace(old, new, 1)

old2 = """      });

      setActiveShift(pumpShift);"""

new2 = """      });

      console.log("NEW ASSIGNMENT CREATED", newAssignment);

      setActiveShift(pumpShift);"""

text = text.replace(old2, new2, 1)

file.write_text(text)

print("Assignment success log added")
