from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
text = p.read_text()

old = """const url = URL.createObjectURL(blob);
        setVideoUrl(url);"""

new = """const url = URL.createObjectURL(blob);
        setVideoUrl(url);

        console.log("🎥 Video captured:", blob.size, blob.type);"""

if old in text:
    text = text.replace(old, new)

p.write_text(text)

print("✅ Video upload preparation patch applied")
