from pathlib import Path

path = Path("src/App.jsx")
text = path.read_text()

import_line = 'import ManagerApproval from "./pages/ManagerApproval";'

if import_line not in text:
    lines = text.splitlines()

    last_import = 0
    for i, line in enumerate(lines):
        if line.startswith("import "):
            last_import = i

    lines.insert(last_import + 1, import_line)
    text = "\n".join(lines)

path.write_text(text)

print("ManagerApproval import added successfully.")
