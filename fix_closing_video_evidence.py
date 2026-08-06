from pathlib import Path

file = Path("src/pages/ClosingVideoEvidence.jsx")

text = file.read_text()

text = text.replace(
    'import CameraCapture from "../components/CameraCapture";',
    'import VideoCapture from "../components/VideoCapture";'
)

old = '''      <CameraCapture
        onCapture={(evidence)=>{
          setVideo(evidence);
        }}
      />'''

new = '''      <VideoCapture
        evidenceType="closing_shift_video"
        onComplete={(evidenceId)=>{
          setVideo(evidenceId);
        }}
      />'''

text = text.replace(old, new)

file.write_text(text)

print("✅ ClosingVideoEvidence repaired.")
