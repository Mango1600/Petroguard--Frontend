from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

if not file.exists():
    print("❌ CameraCapture.jsx not found")
    exit()

content = file.read_text()

content = content.replace(
'import { useRef, useState, useEffect } from "react";',
'import { useRef, useState, useEffect } from "react";'
)

content = content.replace(
'const [capturedImage, setCapturedImage] = useState(null);',
'const [capturedImage, setCapturedImage] = useState(null);'
)

content = content.replace(
'<h3>📷 Evidence Capture</h3>',
'<h3>📹 Video Evidence Capture</h3>'
)

content = content.replace(
'📷 Capture Evidence',
'📹 Start Evidence Capture'
)

file.write_text(content)

print("✅ Camera evidence label updated")
