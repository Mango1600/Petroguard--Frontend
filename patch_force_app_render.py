from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

old = """export default function App() {
  console.log("APP STARTED");
  const [staff, setStaff] = useState(null);
"""

new = """export default function App() {
  return <div style={{padding:"30px",color:"black",background:"white"}}>PETROGUARD APP TEST</div>;

  const [staff, setStaff] = useState(null);
"""

text = text.replace(old, new)

file.write_text(text)

print("Forced App render test applied.")
