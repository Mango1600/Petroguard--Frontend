from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")
text = file.read_text()

text = text.replace(
'''onCapture={(file)=>{
              setOpeningEvidence(file);
            }}''',
'''onCapture={(evidenceId)=>{
              setOpeningEvidence(evidenceId);
            }}'''
)

text = text.replace(
'''onCapture={(file)=>{
              setClosingEvidence(file);
            }}''',
'''onCapture={(evidenceId)=>{
              setClosingEvidence(evidenceId);
            }}'''
)

file.write_text(text)

print("✅ PumpReadings repaired.")
