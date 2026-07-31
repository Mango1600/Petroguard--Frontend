import { useState } from "react";
import { supabase } from "../lib/supabase";
import ShiftActive from "./ShiftActive";

export default function AttendantHandover({ shift, currentAttendant }) {

  const [staffId,setStaffId]=useState("");
  const [openingEvidence,setOpeningEvidence]=useState("");
  const [done,setDone]=useState(false);

  async function handover(){

    if(!staffId){
      alert("Select incoming attendant");
      return;
    }

    const now=new Date().toISOString();

    await supabase
      .from("shift_attendants")
      .update({
        status:"HANDED_OVER",
        clock_out:now,
        closing_video:openingEvidence
      })
      .eq("shift_id",shift.id)
      .eq("staff_id",currentAttendant.id);

    await supabase
      .from("shift_attendants")
      .insert([{
        shift_id:shift.id,
        pump_id:shift.pump_id,
        station_id:shift.station_id,
        staff_id:Number(staffId),
        status:"ACTIVE",
        clock_in:now,
        opening_video:openingEvidence
      }]);

    setDone(true);
  }

  if(done){
    return <ShiftActive shift={shift}/>;
  }

  return(
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>

      <h2>🤝 ATTENDANT HANDOVER</h2>

      <p>Shift: {shift.id}</p>
      <p>Pump: {shift.pump_id}</p>

      <input
        style={{width:"100%",padding:12}}
        placeholder="Incoming Staff ID"
        value={staffId}
        onChange={(e)=>setStaffId(e.target.value)}
      />

      <br/><br/>

      <textarea
        style={{width:"100%",padding:12}}
        placeholder="Opening Evidence"
        value={openingEvidence}
        onChange={(e)=>setOpeningEvidence(e.target.value)}
      />

      <br/><br/>

      <button
        style={{width:"100%",padding:15}}
        onClick={handover}
      >
        COMPLETE HANDOVER
      </button>

    </div>
  );
}
