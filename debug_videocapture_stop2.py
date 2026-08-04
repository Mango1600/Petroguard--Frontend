from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
t = p.read_text()

start = t.find("function stopRecording()")
end = t.find("function stopCamera()", start)

if start == -1 or end == -1:
    print("❌ Functions not found")
else:
    new_function = """function stopRecording() {

    console.log(
      "STOP CLICK",
      recorderRef.current?.state
    );

    alert(
      "Recorder state: " +
      recorderRef.current?.state
    );

    if (
      recorderRef.current &&
      recorderRef.current.state === "recording"
    ) {
      recorderRef.current.stop();
    }

    setRecording(false);
}

"""

    t = t[:start] + new_function + t[end:]

    p.write_text(t)
    print("✅ stopRecording replaced")
