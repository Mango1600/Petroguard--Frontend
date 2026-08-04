from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
t = p.read_text()

t = t.replace(
'import VideoCapture from "../components/VideoCapture";\n',
''
)

start = t.find('  if (showVideo) {')
end = t.find('  if (showPumpReading) {')

if start != -1 and end != -1:
    t = t[:start] + t[end:]

t = t.replace(
'''              setShowVideo(true);''',
'''              await createShift();
              setShowPumpReading(true);'''
)

p.write_text(t)

print("✅ VideoCapture removed from OpenShift")
