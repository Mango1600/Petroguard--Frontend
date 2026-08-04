from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

old = '''
    if (failed) {

      setMessage(
        "Cannot close Business Day. Pending requirements detected."
      );

    } else {

      setMessage(
        "Business Day Closed Successfully."
      );
    }
'''

new = '''
    if (failed) {

      setMessage(
        "Cannot close Business Day. Pending requirements detected."
      );

    } else {

      const { data: closure, error } = await supabase
        .from("business_day_closures")
        .insert([
          {
            station_id: staff.station_id,
            business_date: today,
            closed_by: staff.id,
            status: "CLOSED",

            pump_readings_completed:
              result.pump_readings,

            tank_dip_completed:
              result.tank_dip,

            payment_summary_completed:
              result.payment_summary,

            manager_approval_completed:
              result.manager_approval
          }
        ])
        .select()
        .single();


      if (error) {
        setMessage(error.message);
        return;
      }


      setMessage(
        "Business Day Closed Successfully. Audit ID: " + closure.id
      );
    }
'''

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Business Day audit insert added successfully.")
