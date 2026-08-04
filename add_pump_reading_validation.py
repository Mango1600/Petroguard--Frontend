from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

old = """
    const result = {

      attendance: true,

      pump_readings: true,

      tank_dip:
        settings?.tank_dip_required ? false : true,

      payment_summary: true,

      manager_approval:
        settings?.manager_approval_required ? false : true
    };
"""

new = """
    const today = new Date().toISOString().split("T")[0];

    const { data: pumps } = await supabase
      .from("pumps")
      .select("id")
      .eq("station_id", staff.station_id);


    const { data: readings } = await supabase
      .from("pump_readings")
      .select("id")
      .eq("station_id", staff.station_id)
      .gte("reading_date", today)
      .lt("reading_date", today + "T23:59:59");


    const result = {

      attendance: true,

      pump_readings:
        pumps && readings &&
        readings.length >= pumps.length,

      tank_dip:
        settings?.tank_dip_required ? false : true,

      payment_summary: true,

      manager_approval:
        settings?.manager_approval_required ? false : true
    };
"""

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Pump readings validation added successfully.")
