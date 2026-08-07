from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """return (
    <pre
      style={{
        background: "#ffe",
        border: "1px solid #999",
        padding: "10px",
        fontSize: "11px",
        whiteSpace: "pre-wrap"
      }}
    >
      {JSON.stringify({ staff }, null, 2)}
    </pre>
  );"""

new = """return (
    <pre
      style={{
        background: "#ffe",
        border: "1px solid #999",
        padding: "10px",
        fontSize: "11px",
        whiteSpace: "pre-wrap"
      }}
    >
      {JSON.stringify({
        staff,
        assignment,
        message
      }, null, 2)}
    </pre>
  );"""

if old not in text:
    print("❌ Debug block not found")
else:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ Debug display expanded")
