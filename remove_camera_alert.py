from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

if not file.exists():
    print("CameraCapture.jsx not found")
    exit()

text = file.read_text()

lines = text.splitlines()

new_lines = []

skip = False

for line in lines:
    if "alert(" in line and "CAMERA PROPS" in line:
        skip = True
        continue

    if skip:
        if "));" in line:
            skip = False
        continue

    new_lines.append(line)

file.write_text("\n".join(new_lines))

print("✅ Camera props alert removed")
