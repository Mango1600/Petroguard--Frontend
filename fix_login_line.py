from pathlib import Path

path = Path("src/pages/Login.jsx")

lines = path.read_text().splitlines()

fixed = []

for line in lines:
    if "alert(error.message);" in line and "\\n" in line:
        fixed.append("      alert(error.message);")
        fixed.append("      setMessage(error.message);")
    else:
        fixed.append(line)

path.write_text("\n".join(fixed) + "\n")

print("Broken login line fixed.")
