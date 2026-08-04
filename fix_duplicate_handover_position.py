from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

start = text.find("  async function handleHandover()")
second = text.find("  async function handleHandover()", start + 1)

if start != -1 and second != -1:
    first_block_end = text.find("  return (", start)

    first_block = text[start:first_block_end]

    text = text[:start] + text[second:first_block_end] + text[first_block_end:]

file.write_text(text)

print("Duplicate handover function removed")
