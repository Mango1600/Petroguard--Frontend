from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

# Add state
if "openingEvidenceDone" not in code:
    code = code.replace(
        'const [message, setMessage] = useState("");',
        'const [message, setMessage] = useState("");\n  const [openingEvidenceDone,setOpeningEvidenceDone]=useState(false);'
    )

# Mark evidence completed after save
code = code.replace(
    'setMessage("✅ Opening Evidence Saved");',
    'setOpeningEvidenceDone(true);\n    setMessage("✅ Opening Evidence Saved");'
)

# Replace CameraCapture rendering
old = '''<CameraCapture
        onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          saveEvidence(evidence);
        }}
      />'''

new = '''{!openingEvidenceDone ? (
      <CameraCapture
        onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          saveEvidence(evidence);
        }}
      />
      ) : (
      <div
        style={{
          padding:15,
          background:"#d4edda",
          borderRadius:8,
          color:"#155724",
          fontWeight:"bold"
        }}
      >
        ✅ Opening Evidence Completed
      </div>
      )}'''

code = code.replace(old, new)

p.write_text(code)

print("✅ Opening evidence callback fixed")
