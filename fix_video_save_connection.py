from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
t = p.read_text()

# Add service import
if 'uploadVideoEvidence' not in t:
    t = t.replace(
        'import { useRef, useState, useEffect } from "react";',
        'import { useRef, useState, useEffect } from "react";\nimport { uploadVideoEvidence } from "../services/evidenceService";'
    )

# Replace immediate completion
old = """if (onComplete) {
          onComplete(blob);
        }"""

new = """await uploadVideoEvidence({
          videoBlob: blob,
          fileName: `shift-video-${Date.now()}.webm`,
          stationId,
          recordId: shiftId,
          moduleName: "shift",
          uploadedBy: staffId,
          description: evidenceType || "Opening shift video evidence"
        });

        console.log("✅ Video evidence saved");

        if (onComplete) {
          onComplete(blob);
        }"""

if old in t:
    t = t.replace(old, new)
    p.write_text(t)
    print("✅ Video save connection patched")
else:
    print("❌ Completion block not found")
