from pathlib import Path
import re

path = Path("src/pages/AttendantDashboard.jsx")
text = path.read_text()

pattern = r'<input\s*placeholder="Closing Evidence"[\s\S]*?/>'

new_text, count = re.subn(pattern, "", text, count=1)

path.write_text(new_text)

print(f"✅ Removed Closing Evidence input ({count} occurrence).")
