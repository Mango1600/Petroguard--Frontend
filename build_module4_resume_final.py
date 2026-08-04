from pathlib import Path

path = Path("src/pages/ResumeAssignment.jsx")
text = path.read_text()

# Remove Sahwaad email filter
text = text.replace(
    '.ilike("email","%@sahwaadpet.com")\n',
    ""
)

# Remove attendant selector state
text = text.replace(
    'const [selected,setSelected]=useState("");\n',
    ""
)

# Logged-in attendant automatically
text = text.replace(
    'if(!selected) return setMessage("Select attendant");',
    'const selected = loggedInStaff.id;'
)

# Use logged-in attendant
text = text.replace(
    "staff_id:selected,",
    "staff_id: loggedInStaff.id,"
)

# Remove dropdown UI
import re

text = re.sub(
    r'<select[\s\S]*?</select>\s*<br/><br/>',
    '',
    text,
    flags=re.MULTILINE
)

# Update heading
text = text.replace(
    "Sahwaad Resume Assignment",
    "Resume Pump Shift"
)

# Update success message
text = text.replace(
    "Sahwaad attendant activated",
    "Pump Shift resumed successfully."
)

path.write_text(text)

print("Module 4 Resume Assignment updated.")
