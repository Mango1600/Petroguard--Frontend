from pathlib import Path

Path("src/pages/AttendantDashboard.jsx").write_text("""
import CameraCapture from "../components/CameraCapture";

export default function AttendantDashboard() {
  return <div style={{padding:"30px",color:"black",background:"white"}}>
    CameraCapture import OK
  </div>;
}
""")

print("CameraCapture test created")
