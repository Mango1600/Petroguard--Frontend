from pathlib import Path

path = Path("src/components/CameraCapture.jsx")
text = path.read_text()

text = text.replace("capturedImage", "capturedPhoto")
text = text.replace("setCapturedImage", "setCapturedPhoto")

path.write_text(text)

print("CameraCapture repaired successfully.")
