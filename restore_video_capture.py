from pathlib import Path

source = Path("src/components/VideoCapture_before_mediafix_20260727.jsx")
target = Path("src/components/VideoCapture.jsx")

text = source.read_text()

text = text.replace(
"  recordId\n}",
"  shiftId,\n  evidenceType = \"SHIFT_VIDEO\"\n}"
)

text = text.replace(
"recordId,\n          moduleName: \"open_shift\"",
"recordId: shiftId || \"PENDING\",\n          moduleName: \"open_shift\""
)

text = text.replace(
"fileName: \"opening_shift_video.webm\"",
"fileName: \"shift_evidence.webm\""
)

target.write_text(text)

print("✅ VideoCapture restored with current workflow props")

