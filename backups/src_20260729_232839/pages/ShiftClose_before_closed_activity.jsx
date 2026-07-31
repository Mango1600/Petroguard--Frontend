import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import VideoCapture from "../components/VideoCapture";

export default function ShiftClose({ staff }) {
  const [shift, setShift] = useState(null);
  const [pump, setPump] = useState(null);
  const [closingMeter, setClosingMeter] = useState("");
  const [message, setMessage] = useState("");
  const [showVideo, setShowVideo] = useState(false);

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

    setShift(data);

    if (data?.pump_id) {
      const { data: pumpData } = await supabase
        .from("pumps")
        .select("id,pump_name,product_type")
        .eq("id", data.pump_id)
        .single();

      setPump(pumpData);
    }
  }

  async function closeShift() {
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

    setMessage(`✅ Closing saved. PetroGuard calculated ${litres} litres`);
    setShowVideo(true);
  }

  if (showVideo) {
    return (
      <VideoCapture
        shiftId={shift.id}
        stationId={staff.station_id}
        staffId={staff.id}
        evidenceType="closing_shift_video"
        onComplete={async () => {
          setShowVideo(false);
        }}
      />
    );
  }

  if (!shift) {
    return <div style={{padding:20}}>No active shift found</div>;
  }

  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h2>🔴 SHIFT CLOSE</h2>

      <p><b>Attendant:</b> {staff.name}</p>
      <p><b>Pump:</b> {pump?.pump_name}</p>
      <p><b>Opening Meter:</b> {shift.opening_meter}</p>

      <input
        type="number"
        placeholder="Closing Meter"
        value={closingMeter}
        onChange={(e)=>setClosingMeter(e.target.value)}
        style={{width:"100%",padding:10}}
      />

      <br/><br/>

      <button
        onClick={closeShift}
        style={{width:"100%",padding:15}}
      >
        💾 SAVE CLOSING METER
      </button>

      <p>{message}</p>
    </div>
  );
}
