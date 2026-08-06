from pathlib import Path

file = Path("src/pages/ShiftClose.jsx")

text = file.read_text()

text = text.replace(
'''onCapture={(x)=>console.log(x)}''',
'''onCapture={() => setPhotoDone(true)}'''
)

file.write_text(text)

print("✅ ShiftClose photo callback fixed.")
