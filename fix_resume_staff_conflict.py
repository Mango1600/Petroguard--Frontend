from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

text = text.replace(
"""export default function ResumeAssignment({
pumpShiftId,
staff
}){

const [staff,setStaff]=useState([]);""",
"""export default function ResumeAssignment({
pumpShiftId,
staff: loggedInStaff
}){

const [attendants,setAttendants]=useState([]);"""
)

text = text.replace(
"""staff?.station_id""",
"""loggedInStaff?.station_id"""
)

text = text.replace(
"""setStaff(data||[]);""",
"""setAttendants(data||[]);"""
)

text = text.replace(
"""{staff.map(s=>""",
"""{attendants.map(s=>"""
)

file.write_text(text)

print("ResumeAssignment staff conflict fixed.")
