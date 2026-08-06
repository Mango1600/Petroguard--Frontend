from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function Dashboard({ staff }) {

  const [station, setStation] = useState(null);
  const [policy, setPolicy] = useState(null);
  const [modulePermissions, setModulePermissions] = useState([]);

  useEffect(() => {
    console.log("Dashboard loaded", staff);
  }, []);

  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      DASHBOARD STEP 1 OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Dashboard step 1 created")
