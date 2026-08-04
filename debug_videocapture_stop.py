from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
t = p.read_text()

old = """function stopRecording() {
    if (recorderRef.current &&
        recorderRef.current.state === "recording") {
      recorderRef.current.stop();
    }

    setRecording(false);
}"""

new = """function stopRecording() {

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
}"""

if old in t:
    t = t.replace(old, new)
    p.write_text(t)
    print("✅ Debug stop patch applied")
else:
    print("❌ stopRecording pattern not found")
