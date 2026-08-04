from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

# Move tank query before result object
bad = """
      const { data: tanks } = await supabase
        .from("tanks")
        .select("id")
        .eq("station_id", staff.station_id);


      const { data: tankReadings } = await supabase
        .from("tank_readings")
        .select("id")
        .eq("station_id", staff.station_id)
        .eq("reading_date", today);


      tank_dip:
"""

good = """
      const { data: tanks } = await supabase
        .from("tanks")
        .select("id")
        .eq("station_id", staff.station_id);


      const { data: tankReadings } = await supabase
        .from("tank_readings")
        .select("id")
        .eq("station_id", staff.station_id)
        .eq("reading_date", today);


      const result = {

        attendance: true,

        pump_readings:
          pumps && readings &&
          readings.length >= pumps.length,

        tank_dip:
"""

text = text.replace(bad, good)

path.write_text(text)

print("Syntax structure fixed.")
