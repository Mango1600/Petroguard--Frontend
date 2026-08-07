from pathlib import Path
import re

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text(encoding="utf-8")

pattern = re.compile(
    r'const shift = assignment\.pump_shifts;\s*'
    r'return\s*\(\s*<div style=\{\{padding:20\}\}>.*?</div>\s*\);\s*',
    re.DOTALL,
)

new_text, count = pattern.subn(
    'const shift = assignment.pump_shifts;\n\n',
    text,
    count=1,
)

if count == 0:
    print("❌ Debug return block not found.")
else:
    path.write_text(new_text, encoding="utf-8")
    print("✅ Debug return block removed successfully.")
