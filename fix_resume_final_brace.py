from pathlib import Path

file = Path("src/pages/ResumeAssignment.jsx")

text = file.read_text()

old = """
</div>
}
"""

new = """
</div>
"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("Removed invalid final brace.")
else:
    print("Pattern not found.")
