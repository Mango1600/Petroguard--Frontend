from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

start = text.index("  async function handleCloseDay() {")
end = text.index("\n\n\n  useEffect(() => {", start)

new_function = r'''
  async function handleCloseDay() {

    const today = new Date().toISOString().split("T")[0];

    const { data: pumps } = await supabase
      .from("pumps")
      .select("id")
      .eq("station_id", staff.station_id);

    const { data: readings } = await supabase
      .from("pump_readings")
      .select("id")
      .eq("station_id", staff.station_id)
      .eq("reading_date", today);


    const { data: tanks } = await supabase
      .from("tanks")
      .select("id")
      .eq("station_id", staff.station_id);

    const { data: tankReadings } = await supabase
      .from("tank_readings")
      .select("id")
      .eq("station_id", staff.station_id)
      .eq("reading_date", today);


    const { data: payment } = await supabase
      .from("daily_reconciliation")
      .select("*")
      .eq("station_id", staff.station_id)
      .eq("reconciliation_date", today)
      .maybeSingle();


    const { data: approval } = await supabase
      .from("daily_reconciliation")
      .select("status")
      .eq("station_id", staff.station_id)
      .eq("reconciliation_date", today)
      .maybeSingle();


    const result = {

      attendance: true,

      pump_readings:
        pumps &&
        readings &&
        readings.length >= pumps.length,

      tank_dip:
        settings?.tank_dip_required
          ? tanks &&
            tankReadings &&
            tankReadings.length >= tanks.length
          : true,

      payment_summary:
        !!payment &&
        (
          Number(payment.cash_sales || 0) +
          Number(payment.pos_sales || 0) +
          Number(payment.transfer_sales || 0) +
          Number(payment.credit_sales_amount || 0)
        ) > 0,

      manager_approval:
        settings?.manager_approval_required
          ? approval?.status === "Approved"
          : true
    };


    setChecks(result);


    const failed = Object.values(result)
      .some(item => item === false);


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

            pump_readings_completed: result.pump_readings,
            tank_dip_completed: result.tank_dip,
            payment_summary_completed: result.payment_summary,
            manager_approval_completed: result.manager_approval
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
  }
'''

text = text[:start] + new_function + text[end:]

path.write_text(text)

print("handleCloseDay cleaned successfully.")
