from pathlib import Path

path = Path("src/components/CameraCapture.jsx")
text = path.read_text()

old = """
if (videoRef.current) {
  videoRef.current.srcObject = mediaStream;
}
"""

new = """
if (videoRef.current) {
  videoRef.current.srcObject = mediaStream;
  videoRef.current.muted = true;

  videoRef.current.onloadedmetadata = () => {
    videoRef.current.play();
  };
}
"""

text = text.replace(old, new)

old2 = """
if (!video || !canvas) return;

canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
"""

new2 = """
if (!video || !canvas) return;

if (!video.videoWidth || !video.videoHeight) {
  setError("Camera is not ready. Please wait.");
  return;
}

canvas.width = video.videoWidth;
canvas.height = video.videoHeight;
"""

text = text.replace(old2, new2)

path.write_text(text)

print("Camera preview fix applied.")
