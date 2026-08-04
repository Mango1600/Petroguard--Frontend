import { useState } from "react";
import { handoverAssignment } from "../lib/pumpShiftAssignment";
import ShiftActive from "./ShiftActive";

export default function AttendantHandover({ shift, currentAttendant }) {

  const [staffId,setStaffId]=useState("");
  const [openingEvidence,setOpeningEvidence]=useState("");
  const [done,setDone]=useState(false);


  async function handover(){

    if(!staffId){
      alert("Incoming staff required");
      return;
    }

    try {

      await handoverAssignment({

        assignmentId: shift.assignment_id,

        pumpShiftId: shift.id,

        currentClosingMeter: shift.closing_meter,

        closingEvidence: openingEvidence,

        nextStaffId: Number(staffId)

      });

      setDone(true);

    } catch(error){

      console.log(error);

      alert(error.message);

    }

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