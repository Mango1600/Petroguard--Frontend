from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
code = p.read_text()

old = """function usePhoto() {
    if (onCapture && capturedImage) {
      onCapture(capturedImage);
    }
  }"""

new = """function usePhoto() {
    if (onCapture && capturedImage) {
      onCapture(capturedImage);

      setCapturedImage(null);
      setCameraOpen(false);

      if (stream) {
        stream.getTracks().forEach((track) => track.stop());
      }
    }
  }"""

if old in code:
    code = code.replace(old, new)
    p.write_text(code)
    print("✅ CameraCapture now exits after Use Photo")
else:
    print("❌ usePhoto() block not found")
