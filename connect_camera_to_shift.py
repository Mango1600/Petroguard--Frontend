from pathlib import Path

file = Path("src/pages/AttendantPumpReading.jsx")

code = file.read_text()

# Add CameraCapture import
if 'CameraCapture' not in code:
    code = code.replace(
        'import { supabase } from "../lib/supabase";',
        'import { supabase } from "../lib/supabase";\nimport CameraCapture from "../components/CameraCapture";'
    )

# Add camera state
if 'videoEvidence' not in code:
    code = code.replace(
        'const [message, setMessage] = useState("");',
        'const [message, setMessage] = useState("");\n  const [videoEvidence, setVideoEvidence] = useState(null);'
    )

# Replace fake opening video button
old = '''<button
        style={{width:"100%",padding:12}}
        onClick={() => setMessage("📹 Opening video captured")}
      >
        📹 Opening Video
      </button>'''

new = '''<h3>📹 Opening Video Evidence</h3>

      <CameraCapture
        onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          setMessage("📹 Opening evidence captured");
        }}
      />'''

code = code.replace(old, new)

file.write_text(code)

print("✅ CameraCapture connected to Active Shift")
