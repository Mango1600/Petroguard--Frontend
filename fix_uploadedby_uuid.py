from pathlib import Path

files = {
    "src/pages/AttendantDashboard.jsx": [
        ("uploadedBy={staff?.id}", "uploadedBy={staff?.user_id}")
    ],
    "src/pages/ShiftClose.jsx": [
        ("uploadedBy: loggedInStaff?.id,", "uploadedBy: loggedInStaff?.user_id,"),
        ("uploadedBy={loggedInStaff?.id || null}", "uploadedBy={loggedInStaff?.user_id || null}")
    ]
}

for filename, replacements in files.items():
    path = Path(filename)

    if not path.exists():
        print(f"❌ Missing: {filename}")
        continue

    text = path.read_text()

    for old, new in replacements:
        if old in text:
            text = text.replace(old, new)
            print(f"✅ Updated {filename}: {old}")
        else:
            print(f"⚠️ Not found in {filename}: {old}")

    path.write_text(text)

print("✅ uploadedBy UUID fix complete")
