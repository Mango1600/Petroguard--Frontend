from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

text = file.read_text()

broken = """    stationId,
    uploadedBy,
    recordId,
    moduleName
  }, null, 2));"""

text = text.replace(broken, "")

file.write_text(text)

print("✅ CameraCapture syntax fixed")
