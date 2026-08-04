from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

# Fix import
old_import = 'import { createAssignment } from "../lib/pumpShiftAssignment";'
new_import = 'import { createAssignment, nextAssignmentNumber } from "../lib/pumpShiftAssignment";'

text = text.replace(old_import, new_import)

# Fix hard-coded assignment number
old_assignment = "assignmentNo: 1,"
new_assignment = "assignmentNo: await nextAssignmentNumber(pumpShift.id),"

if old_assignment in text:
    text = text.replace(old_assignment, new_assignment, 1)
    file.write_text(text)
    print("Assignment number patched successfully")
else:
    print("assignmentNo line not found")
