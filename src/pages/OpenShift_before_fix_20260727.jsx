import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import AttendantPumpReading from "./AttendantPumpReading";
import VideoCapture from "../components/VideoCapture";


export default function OpenShift({ staff, onShiftOpened }) {
  const [pumps, setPumps] = useState([]);
  const [pumpId, setPumpId] = useState("");
  const [openingMeter, setOpeningMeter] = useState("");
  const [activeShift, setActiveShift] = useState(null);
  const [message, setMessage] = useState("");
  const [showVideo, setShowVideo] = useState(false);
  const [showPumpReading, setShowPumpReading] = useState(false);

  useEffect(() => {
    if (staff?.id) {
      loadPumps();
      loadActiveShift();
    }
  }, [staff?.id]);

  async function loadPumps() {
    const { data, error } = await supabase
      .from("pumps")
      .select("id,pump_name,product_type")
      .eq("id", 1);

    if (error) {
      setMessage(error.message);
      return;
    }

    setPumps(data || []);
  }

  async function loadActiveShift() {
    const { data } = await supabase
      .from("staff_shifts")
      .select("*")
      .eq("staff_id", staff.id)
      .eq("status", "open")
      .order("id", { ascending: false })
      .limit(1)
      .maybeSingle();

    console.log("ACTIVE SHIFT:", data);
    setActiveShift(data);
  }

  async function openShift() {
    if (activeShift) {
      setMessage("⚠️ Shift already open");

      if (onShiftOpened) {
        onShiftOpened();
      }

      return;
    }

    if (!pumpId) {
      setMessage("Select a pump");
      return;
    }

    if (!openingMeter) {
      setMessage("Enter opening meter");
      return;
    }

    const { error } = await supabase
      .from("staff_shifts")
      .insert([{
        staff_id: staff.id,
        station_id: staff.station_id,
        pump_id: Number(pumpId),
        opening_meter: Number(openingMeter),
        shift_date: new Date().toISOString().split("T")[0],
        clock_in: new Date().toLocaleTimeString("en-GB"),
        status: "open"
      }]);

    if (error) {
      setMessage(error.message);
      return;
    }

    setMessage("✅ Shift Opened Successfully");

    if (onShiftOpened) {
      onShiftOpened();
      return;
    }

    loadActiveShift();
  }


  if (showVideo) {
    return (
      <VideoCapture
        stationId={staff.station_id}
        staffId={staff.id}
        recordId={staff.id}
        onComplete={async (result) => {
          console.log("VIDEO CAPTURED:", result);
          setMessage("✅ Video Evidence Recorded");
          setShowVideo(false);

          await loadActiveShift();
        }}
      />
    );
  }

  if (showPumpReading) {
    return <AttendantPumpReading staff={staff} />;
  }

  return (
    <div style={{ padding:20, maxWidth:500, margin:"auto" }}>
      <h2>🟢 OPEN SHIFT</h2>

      <p><b>Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_name || staff?.station_id}</p>

      {activeShift && (
        <>
          <p><b>Status:</b> 🟢 Shift Open</p>
          <p><b>Clock In:</b> {activeShift.clock_in}</p>
        </>
      )}

      {!activeShift && (
      <>
      <p><b>Pump</b></p>

      <select
        value={pumpId}
        onChange={(e)=>setPumpId(e.target.value)}
        style={{width:"100%",padding:10}}
      >
        <option value="">Select Pump</option>
        {pumps.map((pump)=>(
          <option key={pump.id} value={pump.id}>
            {pump.pump_name} ({pump.product_type})
          </option>
        ))}
      </select>

      <br/><br/>

      <input
        type="number"
        placeholder="Opening Meter"
        value={openingMeter}
        onChange={(e)=>setOpeningMeter(e.target.value)}
        style={{width:"100%",padding:10}}
      />

      <br/><br/>
      </>
      )}

      <button
        style={{width:"100%",padding:15}}
        onClick={() => {
          if (activeShift) {
            setShowPumpReading(true);
            return;
          }

          if (!pumpId) {
            setMessage("Select a pump");
            return;
          }

          if (!openingMeter) {
            setMessage("Enter opening meter");
            return;
          }

          setShowVideo(true);
        }}
      >
        {activeShift ? "▶ Continue Working" : "START SHIFT"}
      </button>

      {activeShift && (
        <>
          <button
            style={{width:"100%",padding:15,marginTop:10}}
          >
            🔄 Request Handover
          </button>

          <button
            style={{width:"100%",padding:15,marginTop:10}}
          >
            🚪 Logout
          </button>
        </>
      )}

      <p>{message}</p>
    </div>
  );
}