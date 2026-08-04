from pathlib import Path

path = Path("src/pages/Login.jsx")

text = path.read_text()

text = text.replace('    console.log("AUTH RESULT:", data.user);\n\n', '')
text = text.replace('    console.log("STAFF QUERY RESULT:", staffRows, staffError);\n\n', '')

path.write_text(text)

print("Login logs removed.")
