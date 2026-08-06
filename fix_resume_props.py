from pathlib import Path

p = Path("src/pages/AttendantDashboard.jsx")
text = p.read_text()

old = '''<ResumeAssignment
                                   staff={staff}
        pumpShiftId={2}
        onResumeSuccess={loadPumpShift}
      />'''

new = '''<ResumeAssignment
        loggedInStaff={staff}
        onResumeSuccess={loadPumpShift}
      />'''

if old in text:
    text = text.replace(old, new)
else:
    text = text.replace("staff={staff}", "loggedInStaff={staff}")
    text = text.replace("pumpShiftId={2}", "")

p.write_text(text)

print("✅ ResumeAssignment props fixed.")
