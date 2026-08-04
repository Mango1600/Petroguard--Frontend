from pathlib import Path

FILE = Path("src/pages/ResumeAssignment.jsx")

text = FILE.read_text()

old = "const businessDay = await getOpenBusinessDay(1);"

new = """const businessDay = await getOpenBusinessDay(
staff?.station_id
);"""

if old in text:
    text = text.replace(old, new, 1)
    FILE.write_text(text)
    print("Hard-coded station removed.")
else:
    print("Station lookup not found.")
