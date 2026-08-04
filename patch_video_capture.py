from pathlib import Path

file = Path("src/components/VideoCapture.jsx")
text = file.read_text()

# Fix recorder.onstop to async only if needed
text = text.replace(
    "recorder.onstop = () => {",
    "recorder.onstop = async () => {"
)

file.write_text(text)

print("✅ VideoCapture async patch applied")
