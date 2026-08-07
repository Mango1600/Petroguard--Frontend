from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

text = file.read_text()

old = """    if (!result.success) {
      alert("Evidence upload failed.");
      return;
    }"""

new = """    alert(JSON.stringify(result, null, 2));

    if (!result.success) {
      alert("Evidence upload failed.");
      return;
    }"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ Camera result debug added")
else:
    print("⚠️ Pattern not found")
