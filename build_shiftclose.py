from pathlib import Path

code = r'''import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import VideoCapture from "../components/VideoCapture";

export default function ShiftClose({ loggedInStaff, onComplete }) {
  return (
    <div style={{padding:20}}>
      <h2>Shift Close Builder Loaded</h2>
      <VideoCapture />
      <CameraCapture
        label="Closing Evidence"
        onCapture={(x)=>console.log(x)}
      />
    </div>
  );
}
'''

Path("src/pages/ShiftClose.jsx").write_text(code, encoding="utf-8")

print("✅ ShiftClose.jsx rebuilt successfully.")
