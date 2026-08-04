
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function PumpShiftReconciliation(){

const [shift,setShift] = useState(null);
const [assignments,setAssignments] = useState([]);
const [status,setStatus] = useState("CHECKING");
const [auditTime,setAuditTime] = useState("");
const [gps,setGps] = useState(null);
const [variance,setVariance] = useState(0);
const [meterStatus,setMeterStatus] = useState("CHECKING");
const [evidenceStatus,setEvidenceStatus] = useState("CHECKING");

useEffect(()=>{
load();
captureAudit();
},[]);


function captureAudit(){

setAuditTime(
new Date().toLocaleString()
);


if(navigator.geolocation){

navigator.geolocation.getCurrentPosition(
(position)=>{

setGps({
latitude: position.coords.latitude,
longitude: position.coords.longitude,
accuracy: position.coords.accuracy
});

}
);

}

}


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



async function validate(data){

let result="PASS";


let evidenceOK=true;

data.forEach(item=>{

if(
!item.opening_evidence ||
!item.closing_evidence
){

evidenceOK=false;

}

});


setEvidenceStatus(
evidenceOK ? "COMPLETE" : "MISSING"
);


if(!evidenceOK){

result="REVIEW REQUIRED";

}


let opening = Number(
data[0]?.opening_meter || 0
);


let closing = Number(
data[data.length-1]?.closing_meter || 0
);


let movement = closing - opening;


setMeterStatus(
movement >= 0 ? "OK" : "CHECK"
);


setVariance(movement);


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
Meter Movement
</h3>

<p>
Total Meter Movement: {variance}
</p>

<p>
Meter Status: {meterStatus}
</p>


<h3>
Evidence Status
</h3>

<p>
{evidenceStatus}
</p>


<h3>
Audit Information
</h3>

<p>
Date / Time:
{auditTime}
</p>

<p>
GPS:
{
gps
?
`${gps.latitude}, ${gps.longitude} (±${gps.accuracy}m)`
:
"Waiting for location..."
}
</p>


<h3>
Reconciliation Status
</h3>

<h2>
{status}
</h2>


</div>

)

}
