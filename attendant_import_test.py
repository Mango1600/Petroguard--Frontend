from pathlib import Path

Path("src/pages/AttendantDashboard.jsx").write_text("""
import ShiftClose from "./ShiftClose";

export default function AttendantDashboard({staff}) {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      SHIFT CLOSE IMPORT TEST OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("ShiftClose test created")
