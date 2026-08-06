from pathlib import Path

Path("src/pages/ShiftClose.jsx").write_text("""
import VideoCapture from "../components/VideoCapture";

export default function ShiftClose({staff}) {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      SHIFT CLOSE BASE TEST OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("ShiftClose base test created")
