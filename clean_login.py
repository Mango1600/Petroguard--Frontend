from pathlib import Path

file = Path("src/pages/Login.jsx")

text = file.read_text(encoding="utf-8")

remove = [
'    console.log("========== AUTH RESULT ==========");\n',
'    console.log("AUTH DATA:", data);\n',
'    console.log("AUTH USER:", data?.user);\n',
'    console.log("AUTH SESSION:", data?.session);\n',
'    console.log("AUTH ERROR:", error);\n',
'    console.log("================================");\n',
]

for line in remove:
    text = text.replace(line, "")

file.write_text(text, encoding="utf-8")

print("✅ Login.jsx cleaned successfully.")
