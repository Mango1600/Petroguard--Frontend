from pathlib import Path

file = Path("src/pages/OpenShift.jsx")

text = file.read_text()

text = text.replace(
"console.log('Creating assignment', pumpShift);\\n\\n      await createAssignment({",
"console.log('Creating assignment', pumpShift);\n\n      await createAssignment({"
)

file.write_text(text)

print("OpenShift debug line fixed")
