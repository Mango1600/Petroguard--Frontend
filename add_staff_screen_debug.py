from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """if (loading)
  return <div style={{padding:20}}>Loading Pump Shift...</div>;"""

new = """if (loading)
  return (
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

if old not in text:
    print("❌ Loading block not found. No changes made.")
else:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ Staff debug display added to AttendantDashboard.jsx")
