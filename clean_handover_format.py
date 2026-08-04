from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
"closing_evidence_time: new Date().toISOString(),                                                    handed_over_at: new Date().toISOString(),",
"""closing_evidence_time: new Date().toISOString(),
        handed_over_at: new Date().toISOString(),"""
)

file.write_text(text)

print("Handover formatting cleaned")
