from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")

text = path.read_text()

# add workflow state
if 'const [page, setPage]' not in text:
    text = text.replace(
        'const [loading, setLoading] = useState(true);',
        '''const [loading, setLoading] = useState(true);
  const [page, setPage] = useState("dashboard");'''
    )

# import ShiftClose
if 'import ShiftClose' not in text:
    text = text.replace(
        'import ResumeAssignment from "./ResumeAssignment";',
        '''import ResumeAssignment from "./ResumeAssignment";
import ShiftClose from "./ShiftClose";'''
    )

# insert controller before main dashboard return
marker = 'return (\n    <div style={{padding:20}}>'

controller = '''
if (page === "shift-close") {
  return (
    <ShiftClose
      staff={staff}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />
  );
}

'''

if controller not in text:
    text = text.replace(marker, controller + marker)

# replace close button
text = text.replace(
    '<button>Close Pump Shift</button>',
    '''<button
onClick={() => setPage("shift-close")}
>
Close Pump Shift
</button>'''
)

path.write_text(text)

print("Module 1 dashboard workflow controller added.")
