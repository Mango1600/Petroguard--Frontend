from pathlib import Path

path = Path("src/components/CameraCapture.jsx")
text = path.read_text()

# Add uploadEvidence import
if 'import { uploadEvidence } from "../services/evidenceService";' not in text:
    text = text.replace(
        'import { useRef, useState } from "react";',
        'import { useRef, useState } from "react";\nimport { uploadEvidence } from "../services/evidenceService";'
    )

# Replace Base64 callback with upload callback
old = """  function usePhoto() {
    if (photo && onCapture) {
      onCapture(photo);
    }
  }"""

new = """  async function usePhoto() {
    if (!photo || !onCapture) return;

    const result = await uploadEvidence({
      imageData: photo,
      fileName: `evidence-${Date.now()}.jpg`,
      moduleName: "camera_capture",
      evidenceType: "PHOTO"
    });

    if (result.success) {
      onCapture(result.evidence.id);
    } else {
      alert("Evidence upload failed.");
    }
  }"""

text = text.replace(old, new)

path.write_text(text)

print("✅ CameraCapture repaired.")
