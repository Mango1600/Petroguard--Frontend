from pathlib import Path

path = Path("src/pages/ResumeAssignment.jsx")
text = path.read_text()

# Add CameraCapture import if missing
if 'import CameraCapture from "../components/CameraCapture";' not in text:
    text = text.replace(
        'import { supabase } from "../lib/supabase";',
        'import { supabase } from "../lib/supabase";\nimport CameraCapture from "../components/CameraCapture";'
    )

old = """
<input
value={evidence}
onChange={e=>setEvidence(e.target.value)}
placeholder="Opening Evidence"
/>

<br/><br/>
"""

new = """
<CameraCapture
  title="Opening Evidence"
  mode="photo"
  onCapture={(photo) => setEvidence(photo)}
/>

<br/><br/>
"""

if old in text:
    text = text.replace(old, new)
    print("Opening Evidence replaced with CameraCapture.")
else:
    print("Opening Evidence block not found.")

path.write_text(text)
