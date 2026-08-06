from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import Login from "./Login";

export default function Dashboard({staff}) {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      DASHBOARD BASE OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Dashboard base test created")
