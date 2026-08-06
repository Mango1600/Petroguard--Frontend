from pathlib import Path

text = Path("src/pages/Login.jsx").read_text()

for i, line in enumerate(text.splitlines(), 1):
    print(f"{i:3}: {line}")
