from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
t = p.read_text()

old = """function stopRecording() {

  if (mediaRecorderRef.current) {
    mediaRecorderRef.current.stop();
  }

  setRecording(false);
}
"""

new = """function stopRecording() {

  if (
    mediaRecorderRef.current &&
    mediaRecorderRef.current.state !== "inactive"
  ) {
    mediaRecorderRef.current.stop();
  }

  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }

  setRecording(false);
  setCameraOpen(false);
}
"""

t = t.replace(old, new)

t = t.replace(
    'setVideoUrl(URL.createObjectURL(blob));',
    '''setVideoUrl(URL.createObjectURL(blob));
    setCameraOpen(false);'''
)

p.write_text(t)

print("✅ CameraCapture.jsx production video fix applied")
