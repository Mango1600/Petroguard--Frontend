import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function AttendantPumpReading({ staff }) {
  const [shift, setShift] = useState(null);
  const [pump, setPump] = useState(null);
  const [openingMeter, setOpeningMeter] = useState("");
  const [closingMeter, setClosingMeter] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    loadShift();
  }, []);

  async function loadShift() {
    const { data } = await supabase
      .from("staff_shifts")
      .select("*")
      .eq("staff_id", staff.id)
      .eq("status", "open")
      .order("id", { ascending: false })
      .limit(1)
      .maybeSingle();

    console.log("SHIFT DATA:", data);
    setShift(data);

    if (data?.pump_id) {
      const { data: pumpData } = await supabase
        .from("pumps")
        .select("id,pump_name,product_type")
        .eq("id", data.pump_id)
        .single();

      console.log("PUMP DATA:", pumpData);
      setPump(pumpData);
    }
  }

  async function saveReading() {
    if (!closingMeter) {
      setMessage("Enter closing meter");
      return;
    }

    const litres =
      Number(closingMeter) - Number(shift.opening_meter);

    const { error } = await supabase
      .from("pump_readings")
      .insert([{
        pump_id: pump.id,
        staff_id: staff.id,
        station_id: staff.station_id,
        opening_meter: Number(shift.opening_meter),
        closing_meter: Number(closingMeter),
        expected_sales: litres,
        reading_date: new Date().toISOString()
      }]);

    if (error) {
      setMessage(error.message);
      return;
    }

    setMessage("✅ Pump reading saved");
  }

  if (!shift) {
    return (
      <div style={{padding:20}}>
        <h2>⛽ Pump Reading</h2>
        <p>No active shift found.</p>
      </div>
    );
  }

  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h2>⛽ ACTIVE SHIFT</h2>

      <p><b>Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_id}</p>
      <p><b>Status:</b> 🟢 Working</p>

      <hr/>

      <h3>Pump</h3>
      <p><b>Pump:</b> {pump?.pump_name} ({pump?.product_type})</p>

      <input
        type="number"
        placeholder="Current Opening Meter"
        value={openingMeter}
        onChange={(e)=>setOpeningMeter(e.target.value)}
        style={{width:"100%",padding:10}}
      />

      <br/><br/>

      <input
        type="number"
        placeholder="Closing Meter"
        value={closingMeter}
        onChange={(e)=>setClosingMeter(e.target.value)}
        style={{width:"100%",padding:10}}
      />

      <br/><br/>

      <button
        style={{width:"100%",padding:15}}
        onClick={saveReading}
      >
        💾 SAVE PUMP READING
      </button>

      <p>{message}</p>
    </div>
  );
}
