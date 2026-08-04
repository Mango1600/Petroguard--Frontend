from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
t = p.read_text()

old = """function stopRecording() {"""

new = """function stopRecording() {

  alert("STOP BUTTON PRESSED");"""

t = t.replace(old, new, 1)

p.write_text(t)

print("✅ Stop button debug patch applied")
