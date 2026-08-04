from pathlib import Path

f = Path("src/pages/ShiftStatus.jsx")
text = f.read_text()

# Add a guard after the useState declarations
marker = 'const [openedBy, setOpenedBy] = useState(null);'

guard = '''const [openedBy, setOpenedBy] = useState(null);

  if (!staff) {
    return (
      <div style={{padding:20}}>
        <h2>Loading...</h2>
        <p>Waiting for staff information...</p>
      </div>
    );
  }'''

text = text.replace(marker, guard)

f.write_text(text)

print("✅ ShiftStatus patched.")
