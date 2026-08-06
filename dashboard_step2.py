from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function Dashboard({ staff }) {

  const [station, setStation] = useState(null);
  const [policy, setPolicy] = useState(null);
  const [modulePermissions, setModulePermissions] = useState([]);

  async function loadStation() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("stations")
      .select("*")
      .eq("id", staff.station_id)
      .single();

    console.log("station:", data, error);
    setStation(data);
  }

  async function loadStationPolicy() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("station_policies")
      .select("*")
      .eq("station_id", staff.station_id)
      .single();

    console.log("policy:", data, error);
    setPolicy(data);
  }

  async function loadModulePermissions() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("module_permissions")
      .select("*")
      .eq("station_id", staff.station_id);

    console.log("permissions:", data, error);
    setModulePermissions(data || []);
  }

  useEffect(() => {
    loadStation();
    loadStationPolicy();
    loadModulePermissions();
  }, []);

  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      DASHBOARD STEP 2 OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Dashboard step 2 created")
