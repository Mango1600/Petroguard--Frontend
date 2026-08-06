from pathlib import Path

p = Path("src/services/evidenceService.js")

text = p.read_text()

text = text.replace(
"  imageData,\n  fileName,",
"  imageData,\n  videoBlob,\n  fileName,"
)

text = text.replace(
"    const blob = dataURLtoBlob(imageData);",
"""    const blob = videoBlob
      ? videoBlob
      : dataURLtoBlob(imageData);"""
)

text = text.replace(
'contentType: "image/jpeg",',
'''contentType: videoBlob
            ? "video/webm"
            : "image/jpeg",'''
)

text = text.replace(
'mime_type: "image/jpeg",',
'''mime_type: videoBlob
            ? "video/webm"
            : "image/jpeg",'''
)

p.write_text(text)

print("✅ Evidence service now supports video and image")
