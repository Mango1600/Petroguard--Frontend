from pathlib import Path

file = Path("src/pages/Login.jsx")

text = file.read_text()

old = """    onLogin(staff);
    return;"""

new = """    alert("MARKER 2026 - STAFF FOUND\\\\n" + JSON.stringify(staff, null, 2));

    onLogin(staff);

    alert("MARKER 2026 - AFTER onLogin");

    return;"""

if old not in text:
    print("❌ Target text not found")
else:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Login markers added")
