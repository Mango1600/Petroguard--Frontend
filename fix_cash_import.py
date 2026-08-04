from pathlib import Path

path = Path("src/pages/CashDeclaration.jsx")

text = path.read_text()

# remove broken first line and router dependency
lines = text.splitlines()

new_lines = []

for line in lines:
    if "const navigate = useNavigate" in line:
        continue
    if 'from "react-router-dom"' in line:
        continue
    if line.strip().startswith("import {") and "useState" not in line:
        continue
    new_lines.append(line)

text = "\n".join(new_lines)

# add correct React import
if 'import { useState } from "react";' not in text:
    text = 'import { useState } from "react";\n' + text

path.write_text(text)

print("CashDeclaration import repaired.")
