from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

target = 'import { handoverAssignment } from "../lib/pumpShiftAssignment";\n'

if 'import ResumeAssignment from "./ResumeAssignment";' not in text:
    text = text.replace(
        target,
        target + 'import ResumeAssignment from "./ResumeAssignment";\n'
    )
    path.write_text(text)
    print("ResumeAssignment import added.")
else:
    print("ResumeAssignment import already exists.")
