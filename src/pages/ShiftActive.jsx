import React, { useState } from "react";
import AttendantHandover from "./AttendantHandover";
import ClosingPumpMeter from "./ClosingPumpMeter";

export default function ShiftActive({shift}){

const [handover,setHandover] = useState(false);
const [closing,setClosing] = useState(false);


return (
<div style={{padding:20}}>

{handover && (
  <AttendantHandover shift={shift}/>
)}


<h2>🟢 SHIFT ACTIVE</h2>

<p>Shift No: {shift?.id}</p>
<p>Pump: Pump 1 (PMS)</p>
<p>Opening Meter: {shift?.opening_meter ?? "Not Available"}</p>

<hr/>

<h3>Status: 🟢 Working</h3>

<button style={{width:"100%",padding:12}}>
🟢 Continue Working
</button>

<br/><br/>

<button
style={{width:"100%",padding:12}}
onClick={()=>setHandover(true)}
>
🤝 Handover Attendant
</button>

<br/><br/>

<button
style={{width:"100%",padding:12}}
onClick={()=>setClosing(true)}
>
🔴 Close Pump Shift
</button>

</div>
)

}