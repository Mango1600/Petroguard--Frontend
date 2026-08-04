from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
t = p.read_text()

t = t.replace(
"const recorderRef = useRef(null);",
"""const recorderRef = useRef(null);
  const streamRef = useRef(null);"""
)

t = t.replace(
"videoRef.current.srcObject = stream;",
"""videoRef.current.srcObject = stream;
      streamRef.current = stream;"""
)

t = t.replace(
"recorderRef.current.start();",
"""recorderRef.current.start(1000);"""
)

t = t.replace(
"""function stopRecording() {
""",
"""function stopRecording() {

    console.log("STOP PRESSED", recorderRef.current?.state);

"""
)

t = t.replace(
"""recorderRef.current.stop();
    }""",
"""recorderRef.current.requestData();
      recorderRef.current.stop();
    }"""
)

p.write_text(t)

print("✅ Recorder stability patch applied")
