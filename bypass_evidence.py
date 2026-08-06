from pathlib import Path

p = Path("src/pages/ResumeAssignment.jsx")
text = p.read_text()

text = text.replace(
    'const [evidence,setEvidence] = useState("");',
    'const [evidence,setEvidence] = useState("TEST_EVIDENCE");'
)

p.write_text(text)
print("✅ Evidence bypass enabled.")
