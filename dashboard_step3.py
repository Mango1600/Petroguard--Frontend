from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function Dashboard({ staff }) {

  const [modulePermissions, setModulePermissions] = useState([]);

  async function loadModulePermissions() {
    if (!staff?.station_id) return;

    const { data } = await supabase
      .from("module_permissions")
      .select("*")
      .eq("station_id", staff.station_id);

    setModulePermissions(data || []);
  }

  useEffect(() => {
    loadModulePermissions();
  }, []);

  function canAccess(moduleName) {
    if (!staff) return false;

    if (staff.role.toLowerCase() === "developer") {
      return true;
    }

    const permission = modulePermissions.find(
      (m) => m.module_name === moduleName
    );

    if (!permission) return false;

    return permission.allowed_roles.includes(
      staff.role.toLowerCase()
    );
  }

  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      DASHBOARD STEP 3 OK<br/>
      User: {staff?.name}<br/>
      Tank Access: {String(canAccess("tank_dip"))}
    </div>
  );
}
""")

print("Dashboard step 3 created")
