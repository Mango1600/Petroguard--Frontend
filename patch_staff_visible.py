from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

text = text.replace(
'''    if (staffError) {
      setMessage(staffError.message);
      return;
    }
''',
'''    if (staffError) {
      setMessage("STAFF ERROR: " + staffError.message);
      return;
    }

    setMessage("STAFF ROWS: " + String(staffRows ? staffRows.length : 0));
'''
)

p.write_text(text)
print("Visible staff debug added.")
