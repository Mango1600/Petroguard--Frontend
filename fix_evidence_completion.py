from pathlib import Path

file = Path("src/pages/AttendantPumpReading.jsx")

code = file.read_text()

# Add evidence saved state
if "evidenceSaved" not in code:
    code = code.replace(
        'const [message, setMessage] = useState("");',
        'const [message, setMessage] = useState("");\n  const [evidenceSaved, setEvidenceSaved] = useState(false);'
    )

# Update successful save
code = code.replace(
    'setMessage("✅ Opening Evidence Saved");',
    'setEvidenceSaved(true);\n    setMessage("✅ Opening Evidence Saved");'
)

# Replace camera display with completion check
old = '''<CameraCapture
        onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          saveEvidence(evidence);
        }}
      />'''

new = '''{!evidenceSaved ? (
        <CameraCapture
          onCapture={(evidence)=>{
            setVideoEvidence(evidence);
            saveEvidence(evidence);
          }}
        />
      ) : (
        <p style={{color:"green",fontWeight:"bold"}}>
          ✅ Opening Evidence Saved
        </p>
      )}'''

code = code.replace(old, new)

file.write_text(code)

print("✅ Evidence completion UI fixed")
