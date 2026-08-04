
import { useEffect,useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";

async function getOpenBusinessDay(stationId){

  const { data, error } = await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", stationId)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}


async function getOpenPumpShift(businessDayId){

  const { data, error } = await supabase
    .from("pump_shifts")
    .select(`
      *,
      pumps(*)
    `)
    .eq("business_day_id", businessDayId)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}



async function getPreviousAssignment(pumpShiftId){

  const { data, error } = await supabase
    .from("attendant_assignments")
    .select("*")
    .eq("pump_shift_id", pumpShiftId)
    .eq("status", "HANDED_OVER")
    .order("assignment_no", { ascending: false })
    .limit(1)
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}






export default function ResumeAssignment({
  loggedInStaff,
  onResumeSuccess
}){

const [message,setMessage] = useState("");
const [previousMeter,setPreviousMeter] = useState("");
const [openingMeter,setOpeningMeter] = useState("");
const [evidence,setEvidence] = useState("");
const [attendants,setAttendants] = useState([]);


async function loadOpenBusinessDay(){

  const { data, error } = await supabase
    .from("business_days")
    .select("*")
    .eq("station_id", loggedInStaff.station_id)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}


async function loadOpenPumpShift(businessDayId){

  const { data, error } = await supabase
    .from("pump_shifts")
    .select(`
      *,
      pumps(*)
    `)
    .eq("business_day_id", businessDayId)
    .eq("status","OPEN")
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}


async function loadPreviousHandedOverAssignment(pumpShiftId){

  const { data, error } = await supabase
    .from("attendant_assignments")
    .select("*")
    .eq("pump_shift_id", pumpShiftId)
    .eq("status","HANDED_OVER")
    .order("assignment_no", { ascending:false })
    .limit(1)
    .maybeSingle();

  if(error){
    throw error;
  }

  return data;
}


function validateResumeMeter(previousMeter, openingMeter){

  if(
    Number(openingMeter) !== Number(previousMeter)
  ){
    throw new Error(
      "Opening meter must match previous closing meter."
    );
  }

  return true;
}


function validateResumeOpeningEvidence(evidence){

  if(!evidence){

    throw new Error(
      "Opening evidence is required before resuming assignment."
    );

  }

  return true;
}


async function createResumeAssignment(
  pumpShiftId,
  staffId,
  openingMeter,
  evidence
){

  const { data:last, error:lastError } = await supabase
    .from("attendant_assignments")
    .select("assignment_no")
    .eq("pump_shift_id", pumpShiftId)
    .order("assignment_no", { ascending:false })
    .limit(1)
    .maybeSingle();


  if(lastError){
    throw lastError;
  }


  const { data, error } = await supabase
    .from("attendant_assignments")
    .insert({

      pump_shift_id: pumpShiftId,
      staff_id: staffId,
      assignment_no: (last?.assignment_no || 0) + 1,
      status: "ACTIVE",
      opening_meter: openingMeter,
      opening_evidence: evidence

    })
    .select()
    .single();


  if(error){
    throw error;
  }


  return data;
}






useEffect(()=>{
  load();
},[]);

async function load(){

try{

const businessDay = await getOpenBusinessDay(
loggedInStaff?.station_id
);

if(!businessDay){
setMessage("No OPEN Business Day found.");
return;
}

const pumpShift = await getOpenPumpShift(businessDay.id);

if(!pumpShift){
setMessage("No OPEN Pump Shift found.");
return;
}

const previous = await getPreviousAssignment(pumpShift.id);

if(previous){
setPreviousMeter(previous.closing_meter);
setOpeningMeter(previous.closing_meter);
}


const {data}=await supabase
.from("staff")
.select("*")
.eq("role","Attendant")
.eq("status","active");

setAttendants(data||[]);

}catch(err){

console.error(err);
setMessage(err.message || "Resume load failed.");

}

}


async function start(){

const selected = loggedInStaff.id;

try{

validateOpeningEvidence(evidence);

validateOpeningMeter(
previousMeter,
openingMeter
);

}catch(err){

return setMessage(err.message);

}


const {data:last}=await supabase
.from("attendant_assignments")
.select("assignment_no")
.eq("pump_shift_id",pumpShiftId)
.order("assignment_no",{ascending:false})
.limit(1)
.single();


await supabase
.from("attendant_assignments")
.insert({
pump_shift_id:pumpShiftId,
staff_id: loggedInStaff.id,
assignment_no:(last?.assignment_no||0)+1,
status:"ACTIVE",
opening_meter:openingMeter,
opening_evidence:evidence
});


setMessage("Pump Shift resumed successfully.");

setEvidence("");
setOpeningMeter("");
setTimeout(() => {
  if(onResumeSuccess){
    onResumeSuccess();
  }
}, 1000);

}


return <div style={{padding:20}}>

<h2>Resume Pump Shift</h2>

<p>Previous Closing Meter: {previousMeter}</p>



<input
value={openingMeter}
onChange={e=>setOpeningMeter(e.target.value)}
placeholder="Opening Meter"
/>

<br/><br/>

<CameraCapture
  title="Opening Evidence"
  mode="photo"
  onCapture={(photo) => setEvidence(photo)}
/>

<br/><br/>

<button onClick={start}>
START ASSIGNMENT
</button>

<p>{message}</p>

</div>

}
