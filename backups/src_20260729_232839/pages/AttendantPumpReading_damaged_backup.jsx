import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import ShiftActive from "./ShiftActive";

export default function AttendantPumpReading({ staff }) {
  const [shift, setShift] = useState(null);
  const [pump, setPump] = useState(null);
  const [openingMeter, setOpeningMeter] = useState("");
  
  const [message, setMessage] = useState("");
  const [shiftStarted,setShiftStarted]=useState(false);
  const [openingEvidenceDone,setOpeningEvidenceDone]=useState(false);
  const [evidenceSaved, setEvidenceSaved] = useState(false);
  const [videoEvidence, setVideoEvidence] = useState(null);

  useEffect(() => {
    restoreOpeningEvidence();

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


async function saveAndStartShift() {

  try {

    if (!openingMeter || !pump?.id) {
      return;
    }

    if (!openingMeter) {
      return;
    }

    const { data: shift, error: shiftError } = await supabase
      .from("staff_shifts")
      .insert([{
        station_id: staff?.station_id,
        pump_id: pump?.id,
        status: "open",
        opening_meter: Number(openingMeter),
        opened_by: staff.id,
        start_time: new Date().toISOString()
      }])
      .select()
      .single();


    if (shiftError) {
      console.log(shiftError);
      return;
    }


    const { error: attendantError } = await supabase
      .from("shift_attendants")
      .insert([{
        shift_id: shift.id,
        staff_id: staff.id,
        status: "ACTIVE",
        activity_type: "SHIFT_STARTED",
        start_time: new Date().toISOString()
      }]);


    if (attendantError) {
      console.log(attendantError);
      return;
    }



    window.location.reload();


  } catch (error) {

    console.log(error);

  }

}





async function restoreOpeningEvidence(){

  const { data } = await supabase
    .from("evidence_links")
    .select("record_id,evidence_id")
    .eq("module_name","opening_shift")
    .eq("record_id",String(shift.id))
    .limit(1);

  if(data && data.length){
    setOpeningEvidenceDone(true);
  }

}


async function saveEvidence(fileData){

  try {

    const { data: evidence, error } = await supabase
      .from("evidence")
      .insert([{
        station_id: staff.station_id,
        uploaded_by: staff.user_id,
        evidence_type: "PHOTO",
        file_name: "opening_shift_evidence.jpg",
        file_path: fileData,
        mime_type: "image/jpeg",
        capture_time: new Date().toISOString(),
        description: "Opening shift evidence",
        status: "ACTIVE"
      }])
      .select()
      .single();


    if(error){
      console.log(error);
      return;
    }


    await supabase
      .from("evidence_links")
      .insert([{
        evidence_id: evidence.id,
        module_name: "staff_shifts",
        record_id: String(shift.id)
      }]);


    setEvidenceSaved(true);
    setOpeningEvidenceDone(true);
    setMessage("✅ Opening Evidence Saved");

  } catch(err){

    console.log(err);

  }


if(shiftStarted){
  return (
    <ShiftActive
      shift={{
        id: shift?.id,
        opening_meter: 1000
      }}
    />
  );
}

  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h2>⛽ ACTIVE SHIFT</h2>

      <p><b>Opened By:</b> {staff?.name}</p>
      <p><b>Current Attendant:</b> {staff?.name}</p>
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

      


      <h3>📹 Opening Video Evidence</h3>

      {!openingEvidenceDone ? (
      <CameraCapture
        onCapture={(evidence)=>{
          setVideoEvidence(evidence);
          saveEvidence(evidence);
        }}
      />
    ) : (
      <div
        style={{
          padding:15,
          background:"#d4edda",
          borderRadius:8,
          color:"#155724",
          fontWeight:"bold",
          textAlign:"center"
        }}
      >
        ✅ Opening Evidence Completed
      </div>
    )}

      <br/><br/>

      <button
        style={{width:"100%",padding:12}}
        onClick={() => setShiftStarted(true)}
      >
        ▶ START OPERATION
      </button>

      <p>{message}</p>
    </div>
  );
}