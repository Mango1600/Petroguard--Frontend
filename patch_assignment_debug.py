from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

text = text.replace(
"if (error) {                                        console.log(error);",
"console.log('Assignment query result:', data, error);\\n\\n    if (error) {                                        console.log(error);"
)

file.write_text(text)

print("Assignment debug added")
