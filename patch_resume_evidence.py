from pathlib import Path

path = Path("src/pages/ResumeAssignment.jsx")

text = path.read_text()

text = text.replace(
'const [message, setMessage] = useState("");',
'''const [message, setMessage] = useState("");
  const [openingMeter, setOpeningMeter] = useState("");
  const [openingEvidence, setOpeningEvidence] = useState("");'''
)

text = text.replace(
'''if(!selectedStaff){
      setMessage("Select attendant");
      return;
    }''',
'''if(!selectedStaff){
      setMessage("Select attendant");
      return;
    }

    if(!openingMeter){
      setMessage("Opening meter required");
      return;
    }

    if(Number(openingMeter) !== Number(previousMeter)){
      setMessage("Opening meter must match previous closing meter");
      return;
    }

    if(!openingEvidence){
      setMessage("Opening evidence required");
      return;
    }'''
)

text = text.replace(
'''opening_meter:previousMeter,
        opening_evidence:"PENDING"''',
'''opening_meter:Number(openingMeter),
        opening_evidence:openingEvidence,
        opening_ai_verified:true,
        evidence_locked:true'''
)

path.write_text(text)

print("Resume evidence rules added.")
