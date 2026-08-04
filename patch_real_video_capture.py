from pathlib import Path

file = Path("src/components/CameraCapture.jsx")

if not file.exists():
    print("❌ CameraCapture.jsx not found")
    exit()

code = file.read_text()

code = code.replace(
'const [capturedImage, setCapturedImage] = useState(null);',
'''const [capturedImage, setCapturedImage] = useState(null);
  const [recording, setRecording] = useState(false);
  const [videoUrl, setVideoUrl] = useState(null);
  const mediaRecorderRef = useRef(null);
  const chunksRef = useRef([]);'''
)

insert = r'''

function startRecording() {

  if (!stream) return;

  chunksRef.current = [];

  const recorder = new MediaRecorder(stream);

  mediaRecorderRef.current = recorder;

  recorder.ondataavailable = (event) => {
    if (event.data.size > 0) {
      chunksRef.current.push(event.data);
    }
  };

  recorder.onstop = () => {
    const blob = new Blob(
      chunksRef.current,
      { type: "video/webm" }
    );

    setVideoUrl(URL.createObjectURL(blob));
  };

  recorder.start();
  setRecording(true);
}


function stopRecording() {

  if (mediaRecorderRef.current) {
    mediaRecorderRef.current.stop();
  }

  setRecording(false);
}

'''

code = code.replace(
"function capturePhoto() {",
insert + "\nfunction capturePhoto() {"
)

code = code.replace(
'<button onClick={capturePhoto}>',
'''<button onClick={recording ? stopRecording : startRecording}>
{
recording ? "⏹ Stop Video" : "🔴 Record Video"
}
</button>

<button onClick={capturePhoto}>'''
)

code = code.replace(
'<h3>📹 Video Evidence Capture</h3>',
'<h3>📹 PetroGuard Video Evidence Capture</h3>'
)

file.write_text(code)

print("✅ Video recording support added")
