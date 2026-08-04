from pathlib import Path

page = Path("src/pages/AttendantHandover.jsx")

page.write_text(r'''import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";

export default function AttendantHandover({ staff, shift }) {

  const [staffList,setStaffList]=useState([]);
  const [nextAttendant,setNextAttendant]=useState("");
  const [closingEvidence,setClosingEvidence]=useState(null);

  useEffect(()=>{
    loadStaff();
  },[]);

  async function loadStaff(){

    const {data}=await supabase
      .from("staff")
      .select("id,name")
      .eq("station_id",staff.station_id)
      .neq("id",staff.id)
      .order("name");

    setStaffList(data||[]);
  }

  async function completeHandover(){

    if(!nextAttendant){
      alert("Select incoming attendant");
      return;
    }

    if(!closingEvidence){
      alert("Capture closing evidence");
      return;
    }

    await supabase
      .from("shift_attendants")
      .update({
        status:"HANDED_OVER",
        end_time:new Date().toISOString()
      })
      .eq("shift_id",shift.id)
      .eq("staff_id",staff.id)
      .eq("status","ACTIVE");

    await supabase
      .from("shift_attendants")
      .insert([{
        shift_id:shift.id,
        staff_id:Number(nextAttendant),
        status:"ACTIVE",
        activity_type:"HANDOVER",
        start_time:new Date().toISOString()
      }]);

    alert("✅ Handover Completed");

    window.location.reload();
  }

  return(

    <div style={{padding:20}}>

      <h2>🤝 Attendant Handover</h2>

      <p><b>Shift:</b> #{shift.id}</p>
      <p><b>Pump:</b> {shift.pump_id}</p>
      <p><b>Outgoing:</b> {staff.name}</p>

      <select
        value={nextAttendant}
        onChange={(e)=>setNextAttendant(e.target.value)}
        style={{width:"100%",padding:10}}
      >

        <option value="">Select Incoming Attendant</option>

        {staffList.map(s=>(
          <option key={s.id} value={s.id}>
            {s.name}
          </option>
        ))}

      </select>

      <br/><br/>

      <CameraCapture
        onCapture={(img)=>{
          setClosingEvidence(img);
        }}
      />

      <br/>

      <button
        style={{width:"100%",padding:12}}
        onClick={completeHandover}
      >
        🤝 COMPLETE HANDOVER
      </button>

    </div>

  );

}
''')

print("✅ Attendant Handover module created")
