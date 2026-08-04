import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function AttendantPumpReading({ staff }) {
  const [shift, setShift] = useState(null);
  const [pump, setPump] = useState(null);
  const [openingMeter, setOpeningMeter] = useState("");
  
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
      <p><b>Shift No:</b> {shift?.id}</p>

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

      

      <br/><br/>

      

      <p>{message}</p>
    </div>
  );
}