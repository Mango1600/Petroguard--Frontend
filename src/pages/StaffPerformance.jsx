import {useEffect,useState} from "react";
import {supabase} from "../lib/supabase";

export default function StaffPerformance(){

const [rows,setRows]=useState([]);

useEffect(()=>{
 load();
},[]);

async function load(){

const {data}=await supabase
.from("shift_attendants")
.select("*")
.order("clock_in",{ascending:false});

setRows(data||[]);
}

return(
<div style={{padding:20}}>

<h2>📊 Staff Performance</h2>

<table border="1" cellPadding="8" width="100%">

<thead>
<tr>
<th>Staff</th>
<th>Pump</th>
<th>Clock In</th>
<th>Clock Out</th>
<th>Status</th>
</tr>
</thead>

<tbody>

{rows.map(r=>

<tr key={r.id}>
<td>{r.staff_name}</td>
<td>{r.pump_id}</td>
<td>{r.clock_in}</td>
<td>{r.clock_out||"ACTIVE"}</td>
<td>{r.status}</td>
</tr>

)}

</tbody>

</table>

</div>
);

}