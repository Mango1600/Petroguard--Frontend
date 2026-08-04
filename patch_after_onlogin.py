from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

text = text.replace(
    "onLogin(staff);",
    'onLogin(staff);\n    setMessage("AFTER ONLOGIN");'
)

p.write_text(text)
print("Patched.")
