from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

text = text.replace(
    "onLogin(staff);",
    """
console.log("LOGIN SUCCESS", staff);
alert("LOGIN SUCCESS: " + JSON.stringify(staff));
onLogin(staff);
"""
)

p.write_text(text)

print("✅ Login debug added.")
