from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")
text = file.read_text()

# Import CameraCapture
if 'import CameraCapture' not in text:
    text = text.replace(
        'import { supabase } from "../lib/supabase";',
        'import { supabase } from "../lib/supabase";\nimport CameraCapture from "../components/CameraCapture";'
    )

# Add evidence verified state
text = text.replace(
    'const [closingEvidence, setClosingEvidence] = useState("");',
    '''const [closingEvidence, setClosingEvidence] = useState("");
  const [evidenceVerified, setEvidenceVerified] = useState(false);'''
)

# Replace placeholder Opening Evidence button
text = text.replace(
'''      <button>
        Opening Evidence
      </button>''',
'''      <CameraCapture
        label="Closing Evidence"
        onCapture={(fileUrl) => {
          setClosingEvidence(fileUrl);
          setEvidenceVerified(true);
        }}
      />'''
)

# Require verified evidence before handover
text = text.replace(
'''    if (!closingMeter || !closingEvidence) {
      alert("Closing meter and evidence required");
      return;
    }''',
'''    if (!evidenceVerified) {
      alert("Capture and verify closing evidence first.");
      return;
    }

    if (!closingMeter) {
      alert("Closing meter required.");
      return;
    }'''
)

file.write_text(text)

print("Enterprise evidence step 1 patched")
