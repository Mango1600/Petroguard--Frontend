from pathlib import Path

file = Path("src/components/VideoCapture.jsx")

text = file.read_text()

# 1. Stop camera after recording/upload
text = text.replace(
"""if (onComplete) {
            onComplete(result);
          }""",
"""stopCamera();
          setSeconds(0);

          if (onComplete) {
            onComplete(result);
          }"""
)

# 2. Reset timer when user stops recording
text = text.replace(
"""setRecording(false);
  }""",
"""setRecording(false);
    setSeconds(0);
  }"""
)

# 3. Change upload module from open_shift to shift_close
text = text.replace(
'moduleName: "open_shift"',
'moduleName: evidenceType'
)

file.write_text(text)

print("✅ VideoCapture.jsx production fix applied.")
