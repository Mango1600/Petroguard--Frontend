from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

text = text.replace(
"""<ResumeAssignment
        staff={staff}
        pumpShiftId={2}
      />""",
"""<ResumeAssignment
        staff={staff}
        pumpShiftId={2}
        onResumeSuccess={loadPumpShift}
      />"""
)

path.write_text(text)

print("Dashboard resume callback connected.")
