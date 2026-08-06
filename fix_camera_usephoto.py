from pathlib import Path
import re

p = Path("src/components/CameraCapture.jsx")
text = p.read_text()

# Fix the Use Photo button
text = re.sub(
    r'<button([^>]*)>\s*✅\s*Use Photo\s*</button>',
    r'<button\1 onClick={usePhoto}>✅ Use Photo</button>',
    text,
    flags=re.DOTALL
)

# Add debug logging
text = text.replace(
    "const path = await uploadEvidence();",
    """const path = await uploadEvidence();
    console.log("CameraCapture upload path:", path);"""
)

p.write_text(text)
print("✅ CameraCapture updated.")
