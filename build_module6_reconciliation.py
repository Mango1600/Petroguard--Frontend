from pathlib import Path

page = Path("src/pages/PumpShiftReconciliation.jsx")

content = r'''
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function PumpShiftReconciliation(){

const [shift,setShift] = useState(null);
const [assignments,setAssignments] = useState([]);
const [status,setStatus] = useState("CHECKING");

useEffect(()=>{
load();
},[]);


async function load(){

const {data:shiftData}=await supabase
.from("pump_shifts")
.select("*")
.eq("status","OPEN")
.maybeSingle();


if(!shiftData){
setStatus("NO OPEN PUMP SHIFT");
return;
}

setShift(shiftData);


const {data:assignmentData}=await supabase
.from("attendant_assignments")
.select("*")
.eq("pump_shift_id",shiftData.id)
.order("assignment_no");


setAssignments(assignmentData || []);


validate(
assignmentData || []
);

}



function validate(data){

let result="PASS";


data.forEach(item=>{

if(
!item.opening_evidence ||
!item.closing_evidence
){

result="REVIEW REQUIRED";

}

});


setStatus(result);

}



return (

<div style={{padding:20}}>

<h2>
Pump Shift Reconciliation
</h2>


<p>
Pump Shift:
{shift?.id || "Loading"}
</p>


<h3>
Attendant Assignments
</h3>

{
assignments.map(a=>(

<div key={a.id}>

<p>
Assignment {a.assignment_no}
</p>

<p>
Status: {a.status}
</p>

<p>
Opening Meter: {a.opening_meter}
</p>

<p>
Closing Meter: {a.closing_meter}
</p>

</div>

))

}


<h3>
Reconciliation Status
</h3>

<h2>
{status}
</h2>


</div>

)

}
'''

page.write_text(content)

print("Module 6 Pump Shift Reconciliation created.")
