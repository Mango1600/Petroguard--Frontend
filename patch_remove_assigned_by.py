from pathlib import Path

file = Path("src/lib/pumpShiftAssignment.js")

text = file.read_text()

text = text.replace(
'''
    assigned_by: assignedBy ?? null,

''',
''
)

file.write_text(text)

print("Removed invalid assigned_by field")
