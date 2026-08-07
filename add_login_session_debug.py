from pathlib import Path

file = Path("src/pages/Login.jsx")

text = file.read_text()

old = """    const user = data.user;

    setMessage("MARKER 2026 - BEFORE STAFF QUERY");"""

new = """    const user = data.user;

    alert(JSON.stringify({
      auth_user: data.user,
      auth_session: data.session
    }, null, 2));

    setMessage("MARKER 2026 - BEFORE STAFF QUERY");"""

if old not in text:
    print("❌ Target not found")
else:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ Login session debug added")
