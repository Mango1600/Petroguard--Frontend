from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

marker = """
      {readings.length === 0 ? (
"""

ui = """
      {activeShift && activeAssignment && (
        <div>
          <h3>🟢 Active Pump Shift Capture</h3>

          <p>
            Pump Shift ID: {activeShift.id}
          </p>

          <p>
            Assignment ID: {activeAssignment.id}
          </p>

          <input
            type="number"
            placeholder="Opening Meter"
            value={openingMeter}
            onChange={(e)=>setOpeningMeter(e.target.value)}
          />

          <br />

          <CameraCapture
            onCapture={(file)=>{
              setOpeningEvidence(file);
            }}
          />

          <br />

          <input
            type="number"
            placeholder="Closing Meter"
            value={closingMeter}
            onChange={(e)=>setClosingMeter(e.target.value)}
          />

          <br />

          <CameraCapture
            onCapture={(file)=>{
              setClosingEvidence(file);
            }}
          />

          <br />

          <button onClick={savePumpReading}>
            Save Pump Reading
          </button>

          <hr />
        </div>
      )}

"""

if marker in text:
    text = text.replace(marker, ui + marker)

file.write_text(text)

print("Pump reading capture UI added")
