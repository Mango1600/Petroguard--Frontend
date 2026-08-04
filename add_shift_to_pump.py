from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
'const [stations, setStations] = useState([]);',
'''const [stations, setStations] = useState([]);
  const [staff, setStaff] = useState([]);
  const [shifts, setShifts] = useState([]);'''
)

text = text.replace(
'''const [pumpResult, stationResult] = await Promise.all([
      supabase
        .from("pump_readings")
        .select("*")
        .order("id"),

      supabase
        .from("stations")
        .select("*")
        .order("id"),
    ]);''',
'''const [pumpResult, stationResult, staffResult, shiftResult] = await Promise.all([
      supabase
        .from("pump_readings")
        .select("*")
        .order("id"),

      supabase
        .from("stations")
        .select("*")
        .order("id"),

      supabase
        .from("staff")
        .select("*")
        .order("id"),

      supabase
        .from("staff_shifts")
        .select("*")
        .order("id"),
    ]);'''
)

text = text.replace(
'''setReadings(pumpResult.data || []);
    setStations(stationResult.data || []);
    setLoading(false);''',
'''setReadings(pumpResult.data || []);
    setStations(stationResult.data || []);
    setStaff(staffResult.data || []);
    setShifts(shiftResult.data || []);
    setLoading(false);'''
)

text = text.replace(
'''function getStationName(stationId) {
    const station = stations.find((s) => s.id === stationId);
    return station ? station.name : `Station ${stationId}`;
  }''',
'''function getStationName(stationId) {
    const station = stations.find((s) => s.id === stationId);
    return station ? station.name : `Station ${stationId}`;
  }

  function getStaffName(staffId) {
    const person = staff.find((s) => s.id === staffId);
    return person ? person.name : `Staff ${staffId}`;
  }

  function getShift(shiftId) {
    return shifts.find((s) => s.id === shiftId);
  }'''
)

text = text.replace(
'''<p>Station: {getStationName(reading.station_id)}</p>''',
'''<p>Station: {getStationName(reading.station_id)}</p>

            <p>
              Attendant: {getStaffName(reading.staff_id)}
            </p>

            <p>
              Shift ID: {reading.staff_shift_id || "Not assigned"}
            </p>'''
)

file.write_text(text)

print("Shift support added successfully")
