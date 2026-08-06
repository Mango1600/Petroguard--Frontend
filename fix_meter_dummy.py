from pathlib import Path

file = Path("src/pages/ShiftActive.jsx")

text = file.read_text()

old = 'shift?.opening_meter || 1000'
new = 'shift?.opening_meter ?? "Not Available"'

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("✅ ShiftActive dummy meter removed")
else:
    print("⚠️ Dummy meter not found. File may already be fixed.")

