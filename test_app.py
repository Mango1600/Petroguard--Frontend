from pathlib import Path

app = Path("src/App.jsx")

app.write_text("""export default function App() {
  return (
    <div style={{padding:"30px", color:"black", background:"white"}}>
      LOGIN TEST
    </div>
  );
}
""")

print("App.jsx replaced with LOGIN TEST")
