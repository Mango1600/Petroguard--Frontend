from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")

s = p.read_text()

# Fix undefined pumpId using selected pump from props/state
s = s.replace(
    "pump_id: pumpId,",
    "pump_id: pump?.id,"
)

# Fix station field if staff has station_id already
s = s.replace(
    "station_id: staff.station_id,",
    "station_id: staff?.station_id,"
)

# Add validation for pump
s = s.replace(
    'if (!openingMeter) {',
    '''if (!openingMeter || !pump?.id) {
      alert("Opening meter and pump required");
      return;
    }

    if (!openingMeter) {''',
    1
)

p.write_text(s)

print("✅ PetroGuard start shift logic fixed")
