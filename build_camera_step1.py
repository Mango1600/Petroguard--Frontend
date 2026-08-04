from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

content = file.read_text()

start = content.find("export default function CameraCapture(")

if start == -1:
    raise SystemExit("CameraCapture component not found")

header = '''import { useRef, useState, useEffect } from "react";

export default function CameraCapture({
  onCapture,
  mode = "both",
  title = "Enterprise Evidence Capture"
}) {
'''

rest = content[start:]
brace = rest.find("{")
body = rest[brace+1:]

states = '''
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const mediaRecorderRef = useRef(null);

  const [cameraOpen, setCameraOpen] = useState(false);
  const [stream, setStream] = useState(null);

  const [capturedPhoto, setCapturedPhoto] = useState(null);
  const [recordedVideo, setRecordedVideo] = useState(null);

  const [recording, setRecording] = useState(false);

  const [gps, setGps] = useState(null);
  const [deviceInfo, setDeviceInfo] = useState("");
  const [networkInfo, setNetworkInfo] = useState("");
  const [batteryLevel, setBatteryLevel] = useState("");
  const [timestamp, setTimestamp] = useState("");
  const [shaHash, setShaHash] = useState("");
  const [aiVerified] = useState(false);

  const [error, setError] = useState("");
'''

# Remove the old refs/state declarations up to the first useEffect
idx = body.find("useEffect(")
if idx == -1:
    raise SystemExit("useEffect not found")

new_body = states + "\n" + body[idx:]

file.write_text(header + new_body)

print("Enterprise Camera Step 1 complete")
