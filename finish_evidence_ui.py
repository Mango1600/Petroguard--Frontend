from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

start = code.find("<CameraCapture")
end = code.find("/>", start)

if start != -1 and end != -1:
    old = code[start:end+2]

    new = """{!openingEvidenceDone ? (
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
          fontWeight:"bold",
          textAlign:"center"
        }}
      >
        ✅ Opening Evidence Completed
      </div>
    )}"""

    code = code.replace(old, new)

    p.write_text(code)
    print("✅ Opening evidence UI completed")

else:
    print("❌ CameraCapture block not found")
