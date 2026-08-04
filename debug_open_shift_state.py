from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
t = p.read_text()

if 'console.log("OpenShift state"' not in t:
    t = t.replace(
        'return (',
        'console.log("OpenShift state", {showVideo, activeShift, showPumpReading});\n\n  return (',
        1
    )

p.write_text(t)

print("✅ Debug added")
