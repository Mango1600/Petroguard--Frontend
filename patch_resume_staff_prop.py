from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

old = """export default function ResumeAssignment({pumpShiftId}){"""

new = """export default function ResumeAssignment({
pumpShiftId,
staff
}){"""

if old in text:
    text = text.replace(old, new, 1)
    FILE.write_text(text)
    print("ResumeAssignment now accepts logged-in staff.")
else:
    print("Component signature not found.")
