from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

target = """if (loading)
    return <div style={{padding:20}}>Loading Pump Shift...</div>;

  if (!assignment) {"""

replacement = """if (loading)
    return <div style={{padding:20}}>Loading Pump Shift...</div>;

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
  );

  if (!assignment) {"""

if target not in text:
    print("❌ Target block not found. No changes made.")
else:
    text = text.replace(target, replacement, 1)
    file.write_text(text)
    print("✅ Staff runtime display inserted.")
