from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

old = """
  return (
    <div style={{padding:20}}>
"""

new = """
  return (
    <div style={{padding:20}}>
      <pre style={{fontSize:11, background:"#eee"}}>
        {JSON.stringify(assignment, null, 2)}
      </pre>
"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Assignment screen debug added")
else:
    print("⚠️ Pattern not found")
