from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

# 1. Import ResumeAssignment
if 'import ResumeAssignment from "./ResumeAssignment";' not in text:
    text = text.replace(
        'import OpenShift from "./OpenShift";',
        'import OpenShift from "./OpenShift";\nimport ResumeAssignment from "./ResumeAssignment";'
    )

# 2. Add resumeMode state
text = text.replace(
    'const [openShiftMode, setOpenShiftMode] = useState(false);',
    '''const [openShiftMode, setOpenShiftMode] = useState(false);
const [resumeMode, setResumeMode] = useState(false);'''
)

# 3. Render ResumeAssignment inside the dashboard
marker = 'if (loading)'
insert = '''
if (resumeMode) {
  return (
    <ResumeAssignment
      staff={staff}
      pumpShiftId={2}
    />
  );
}

'''
text = text.replace(marker, insert + marker)

# 4. Change Resume button action
text = text.replace(
    'window.location.href="/resume-assignment";',
    'setResumeMode(true);'
)

path.write_text(text)

print("Resume mode integrated into Attendant Dashboard.")
