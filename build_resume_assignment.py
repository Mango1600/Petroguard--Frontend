from pathlib import Path

path = Path("src/pages/ResumeAssignment.jsx")

path.write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ResumeAssignment({ pumpShiftId }) {

  const [attendants, setAttendants] = useState([]);
  const [selectedStaff, setSelectedStaff] = useState("");
  const [previousMeter, setPreviousMeter] = useState(0);
  const [message, setMessage] = useState("");

  useEffect(() => {
    loadData();
  }, []);


  async function loadData(){

    const { data: last } = await supabase
      .from("attendant_assignments")
      .select("closing_meter")
      .eq("pump_shift_id", pumpShiftId)
      .order("assignment_no", {ascending:false})
      .limit(1)
      .single();


    if(last){
      setPreviousMeter(last.closing_meter || 0);
    }


    const { data } = await supabase
      .from("staff")
      .select("*")
      .eq("role","Attendant")
      .eq("status","active");


    setAttendants(data || []);

  }


  async function startAssignment(){

    if(!selectedStaff){
      setMessage("Select attendant");
      return;
    }


    const { data: last } = await supabase
      .from("attendant_assignments")
      .select("assignment_no")
      .eq("pump_shift_id", pumpShiftId)
      .order("assignment_no",{ascending:false})
      .limit(1)
      .single();


    const nextNo = (last?.assignment_no || 0) + 1;


    const {error} = await supabase
      .from("attendant_assignments")
      .insert({
        pump_shift_id:pumpShiftId,
        staff_id:selectedStaff,
        assignment_no:nextNo,
        status:"ACTIVE",
        opening_meter:previousMeter,
        opening_evidence:"PENDING"
      });


    if(error){
      setMessage(error.message);
      return;
    }


    setMessage("Assignment started successfully");

  }


  return (
    <div style={{padding:20}}>

      <h2>Resume Pump Shift</h2>

      <p>
        Previous Closing Meter:
        {previousMeter}
      </p>


      <select
        value={selectedStaff}
        onChange={e=>setSelectedStaff(e.target.value)}
      >

        <option value="">
          Select Attendant
        </option>

        {attendants.map(a=>
          <option key={a.id} value={a.id}>
            {a.name}
          </option>
        )}

      </select>


      <br/><br/>


      <button onClick={startAssignment}>
        Start Assignment
      </button>


      <p>{message}</p>

    </div>
  );
}
""")

print("Resume Assignment page created.")
