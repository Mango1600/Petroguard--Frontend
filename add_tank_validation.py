from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

old = """
      tank_dip:
        settings?.tank_dip_required ? false : true,
"""

new = """
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
        settings?.tank_dip_required
          ? (
              tanks &&
              tankReadings &&
              tankReadings.length >= tanks.length
            )
          : true,
"""

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Tank dip validation added successfully.")
