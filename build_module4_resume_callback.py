from pathlib import Path

# Patch AttendantDashboard
path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

old = """
<ResumeAssignment
        staff={staff}
        pumpShiftId={2}
/>
"""

new = """
<ResumeAssignment
        staff={staff}
        pumpShiftId={2}
        onResumeSuccess={loadPumpShift}
/>
"""

if old in text:
    text = text.replace(old, new)
    print("AttendantDashboard callback added.")
else:
    print("ResumeAssignment block not found.")

path.write_text(text)


# Patch ResumeAssignment
path = Path("src/pages/ResumeAssignment.jsx")
text = path.read_text()

text = text.replace(
"""export default function ResumeAssignment({
pumpShiftId,
staff: loggedInStaff
})""",
"""export default function ResumeAssignment({
pumpShiftId,
staff: loggedInStaff,
onResumeSuccess
})"""
)

old = """
setMessage("Pump Shift resumed successfully.");

}
"""

new = """
setMessage("Pump Shift resumed successfully.");

setEvidence("");
setOpeningMeter("");
setTimeout(() => {
  if(onResumeSuccess){
    onResumeSuccess();
  }
}, 1000);

}
"""

if old in text:
    text = text.replace(old, new)
    print("Resume success transition added.")
else:
    print("Success block not found.")

path.write_text(text)

print("Module 4.4 patch completed.")
