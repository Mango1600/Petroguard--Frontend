from pathlib import Path

file = Path("src/pages/ShiftClose.jsx")
text = file.read_text()

old = 'onCapture={(image) => { setPhoto(image); setPhotoDone(true); }}'
new = 'onCapture={(evidenceId) => { setPhoto(evidenceId); setPhotoDone(true); }}'

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ ShiftClose repaired.")
else:
    print("Nothing to patch. It may already be repaired or the code has changed.")

