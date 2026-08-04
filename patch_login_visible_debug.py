from pathlib import Path

path = Path("src/pages/Login.jsx")

text = path.read_text()

text = text.replace(
'setMessage(error.message);',
'alert(error.message);\\n      setMessage(error.message);'
)

path.write_text(text)

print("Visible login error added")
