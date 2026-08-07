from pathlib import Path

file = Path("src/App.jsx")

lines = file.read_text().splitlines()

new_lines = []

for line in lines:
    if "alert(" in line:
        continue
    new_lines.append(line)

file.write_text("\n".join(new_lines) + "\n")

print("✅ Removed alert lines from App.jsx")
