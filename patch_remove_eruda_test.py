from pathlib import Path

file = Path("src/main.jsx")

text = file.read_text()

text = text.replace(
'import eruda from "eruda";\neruda.init();',
'// eruda disabled for test'
)

file.write_text(text)

print("Eruda disabled for test.")
