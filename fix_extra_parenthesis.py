from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")
lines = path.read_text().splitlines()

fixed = []
removed = False

for line in lines:
    if not removed and line.strip() == ");":
        # Remove only the extra one immediately after OpenShift
        # (the previous line is already "      );")
        if fixed and fixed[-1].strip() == ");":
            removed = True
            continue
    fixed.append(line)

path.write_text("\n".join(fixed) + "\n")
print("Extra parenthesis removed.")
