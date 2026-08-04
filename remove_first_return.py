from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

start = code.find('  return (\n      <div style={{padding:20}}>')

if start != -1:
    end = code.find('  return (\n    <div style={{padding:20,maxWidth:500', start)

    if end != -1:
        code = code[:start] + code[end:]
        p.write_text(code)
        print("✅ Duplicate pump reading return removed")
    else:
        print("❌ End block not found")
else:
    print("❌ Start block not found")
