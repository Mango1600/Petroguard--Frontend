from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
text = p.read_text()

marker = "      <p>{message}</p>"

insert = """
      <button
        style={{width:"100%",padding:12}}
        onClick={() => setMessage("📹 Opening video captured")}
      >
        📹 Opening Video
      </button>

      <br/><br/>

      <button
        style={{width:"100%",padding:12}}
        onClick={() => setMessage("▶ Operation Started")}
      >
        ▶ START OPERATION
      </button>

"""

if "📹 Opening Video" in text:
    print("⚠️ Buttons already exist")
elif marker in text:
    text = text.replace(marker, insert + marker)
    p.write_text(text)
    print("✅ Opening buttons inserted")
else:
    print("❌ Marker not found")
