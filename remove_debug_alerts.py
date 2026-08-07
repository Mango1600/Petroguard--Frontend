from pathlib import Path

files = [
    "src/pages/ShiftClose.jsx",
    "src/components/CameraCapture.jsx"
]

for f in files:
    path = Path(f)

    if not path.exists():
        continue

    text = path.read_text()

    text = text.replace(
        'alert(JSON.stringify({\n  uploadedBy,\n  shift,\n  assignment\n}, null, 2));',
        ''
    )

    text = text.replace(
        'alert(JSON.stringify(result, null, 2));',
        ''
    )

    text = text.replace(
        'alert("USE PHOTO CLICKED");',
        ''
    )

    path.write_text(text)

print("✅ Debug alerts removed")
