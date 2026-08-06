from pathlib import Path

p = Path("src/services/evidenceService.js")
text = p.read_text()

old = '''console.error("Evidence Upload Error FULL:", JSON.stringify(error, null, 2));'''

new = '''console.error("Evidence Upload Error FULL:", JSON.stringify(error, null, 2));
    alert("Evidence Error: " + JSON.stringify(error));'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Evidence error popup added")
else:
    print("Already patched or text not found")
