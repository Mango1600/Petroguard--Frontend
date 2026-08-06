from pathlib import Path
import subprocess

content = subprocess.check_output(
    ["git", "show", "7bdc16f:src/App.jsx"],
    text=True
)

Path("src/App.jsx").write_text(content)

print("Real App.jsx restored")
