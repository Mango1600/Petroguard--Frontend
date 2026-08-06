from pathlib import Path

p = Path("src/components/VideoCapture.jsx")

text = p.read_text()

text = text.replace("""
  useEffect(() => {
    startCamera();

    return () => {
      stopCamera();
    };
  }, []);
""", """
  useEffect(() => {
    return () => {
      stopCamera();
    };
  }, []);
""")

text = text.replace("""
      <h3>🎥 PetroGuard Video Evidence</h3>
""", """
      <h3>🎥 PetroGuard Video Evidence</h3>

      {!videoRef.current && (
        <button onClick={startCamera} style={{width:"100%",padding:15}}>
          📷 START CAMERA
        </button>
      )}
""")

p.write_text(text)

print("VideoCapture patched")
