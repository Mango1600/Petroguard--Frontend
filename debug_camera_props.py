from pathlib import Path

path = Path("src/components/CameraCapture.jsx")
text = path.read_text(encoding="utf-8")

marker = "const [error, setError] = useState(\"\");"

debug = """
  alert("CAMERA PROPS\\n" + JSON.stringify({
    stationId,
    uploadedBy,
    recordId,
    moduleName
  }, null, 2));
"""

if "CAMERA PROPS" in text:
    print("✅ Camera debug already added.")
    raise SystemExit

if marker not in text:
    print("❌ Marker not found.")
    raise SystemExit

text = text.replace(marker, marker + debug)

path.write_text(text, encoding="utf-8")

print("✅ CameraCapture debug added.")
