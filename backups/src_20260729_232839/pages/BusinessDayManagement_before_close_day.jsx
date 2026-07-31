import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function BusinessDayManagement({ staff }) {
 const [businessDay,setBusinessDay]=useState(null);
 useEffect(()=>{loadBusinessDay();},[]);
 async function loadBusinessDay(){
  const {data,error}=await supabase.from("business_days").select("*").eq("station_id",staff.station_id).eq("status","open").single();
  if(error){console.log(error);return;}
  setBusinessDay(data);
 }
 return <div><h2>📅 Business Day Management</h2>{businessDay ? <><p>Status: 🟢 {businessDay.status}</p><p>Date: {businessDay.business_date}</p></> : <p>No open business day found</p>}</div>;
}
