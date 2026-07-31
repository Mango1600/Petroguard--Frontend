import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function AttendantActivity({ shiftId }) {
  const [records,setRecords]=useState([]);

  useEffect(()=>{
    load();
  },[]);

  async function load(){
    const {data}=await supabase
      .from("shift_attendants")
      .select("*")
      .eq("shift_id",shiftId)
      .order("clock_in",{ascending:true});

    setRecords(data||[]);
  }

  return(
    <div style={{padding:20}}>
      <h2>👥 Attendant Activity</h2>

      {records.map(r=>(
        <div key={r.id}
          style={{
            border:"1px solid #ddd",
            borderRadius:8,
            padding:12,
            marginBottom:12
          }}>
          <b>{r.staff_name}</b><br/>
          Clock In: {r.clock_in}<br/>
          Clock Out: {r.clock_out || "ACTIVE"}<br/>
          Status: {r.status}
        </div>
      ))}
    </div>
  );
}
