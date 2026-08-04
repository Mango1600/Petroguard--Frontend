from pathlib import Path

p = Path("src/components/CameraCapture.jsx")
code = p.read_text()

# Hide photo when video exists
code = code.replace(
    "{capturedImage && (",
    "{!videoUrl && capturedImage && ("
)

# Hide video when photo exists
code = code.replace(
    "{videoUrl && (",
    "{!capturedImage && videoUrl && ("
)

# Close workflow after Use Video
code = code.replace(
    'onCapture(videoUrl);\n              setVideoUrl(null);',
    '''onCapture(videoUrl);
              setVideoUrl(null);
              setCapturedImage(null);
              setCameraOpen(false);'''
)

# Close workflow after Use Photo
code = code.replace(
    'onCapture(capturedImage);\n\n      setCapturedImage(null);',
    '''onCapture(capturedImage);

      setVideoUrl(null);
      setCapturedImage(null);'''
)

p.write_text(code)

print("✅ PetroGuard evidence workflow fixed")
