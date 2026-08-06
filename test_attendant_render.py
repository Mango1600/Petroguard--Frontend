from pathlib import Path

Path("src/pages/AttendantDashboard.jsx").write_text("""
export default function AttendantDashboard({staff}) {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      ATTENDANT DASHBOARD TEST<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("AttendantDashboard replaced")
