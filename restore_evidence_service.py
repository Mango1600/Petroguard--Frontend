from pathlib import Path

source = Path("src/services/evidenceService_before_video_20260727.js")
target = Path("src/services/evidenceService.js")

target.write_text(source.read_text())

print("✅ Evidence service restored")
