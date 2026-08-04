from pathlib import Path
import re

path = Path("src/pages/ResumeAssignment.jsx")
text = path.read_text()

# Add state
if 'const [instructionAccepted' not in text:
    text = text.replace(
        'const [message, setMessage] = useState("");',
        '''const [message, setMessage] = useState("");
const [instructionAccepted, setInstructionAccepted] = useState(false);'''
    )

# Insert instruction panel before camera
pattern = r'(<CameraCapture[\s\S]*?onCapture=\{setEvidence\}[\s\S]*?\/>)'

replacement = """
<div style={{
background:"#fff8e1",
border:"1px solid #d6b656",
padding:"12px",
borderRadius:"8px",
marginBottom:"15px"
}}>
<h3>📷 OPENING EVIDENCE REQUIRED</h3>

<p><strong>Expected Opening Meter:</strong> {openingMeter}</p>

<p>Photograph ONLY:</p>

<ul>
<li>✓ Pump meter display</li>
<li>✓ Reading showing {openingMeter}</li>
<li>✓ Correct pump</li>
</ul>

<p>Do NOT photograph:</p>

<ul>
<li>✗ Yourself</li>
<li>✗ Another pump</li>
<li>✗ Floor or surroundings</li>
<li>✗ Unrelated objects</li>
</ul>

<label>
<input
type="checkbox"
checked={instructionAccepted}
onChange={(e)=>setInstructionAccepted(e.target.checked)}
/>
{" "}I understand these instructions
</label>
</div>

{instructionAccepted && (
\\1
)}
"""

text = re.sub(pattern, replacement, text, count=1)

path.write_text(text)

print("Opening Evidence Instructions added.")
