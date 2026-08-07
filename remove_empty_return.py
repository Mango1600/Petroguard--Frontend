from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
"""  return (

  );

""",
""
)

file.write_text(text)

print("✅ Removed empty return")
