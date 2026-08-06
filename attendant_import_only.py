from pathlib import Path

Path("src/pages/AttendantDashboard.jsx").write_text("""
import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import { handoverAssignment } from "../lib/pumpShiftAssignment";
import ResumeAssignment from "./ResumeAssignment";
import ShiftClose from "./ShiftClose";
import CashDeclaration from "./CashDeclaration";

export default function AttendantDashboard({staff}) {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      ATTENDANT IMPORTS OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Attendant import-only test created")
