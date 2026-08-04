from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
text = p.read_text()

old = '''      <br/><br/>

      <p>{message}</p>
'''

new = '''      <br/><br/>

      <button
        style={{width:"100%",padding:12}}
        onClick={() => setMessage("📹 Opening video capture ready")}
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

      <p>{message}</p>
'''

text = text.replace(old, new)

p.write_text(text)

print("✅ Opening video and start operation added")
