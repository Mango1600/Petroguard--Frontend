from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

text = text.replace(
'''      alert(JSON.stringify(data.session, null, 2));\n''',
''
)

file.write_text(text)

print("✅ Removed App session alert")
