from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

old = """export default function App() {
  console.log("APP STARTED");

  const [staff, setStaff] = useState(null);
"""

new = """export default function App() {
  return <div style={{padding:"30px"}}>PETROGUARD APP TEST</div>;

  const [staff, setStaff] = useState(null);
"""

if "PETROGUARD APP TEST" not in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("Temporary App render test added.")
else:
    print("Already added.")
