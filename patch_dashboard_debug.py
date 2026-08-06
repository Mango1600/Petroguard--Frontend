from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

p.write_text("""
import AttendantDashboard from "./AttendantDashboard";
import ManagerDashboard from "./ManagerDashboard";

export default function Dashboard({staff}) {

  console.log("CURRENT STAFF LOGIN:", staff);

  if(staff?.role === "Manager" || staff?.role === "manager"){
    return <ManagerDashboard staff={staff}/>;
  }

  if(staff?.role === "Attendant" || staff?.role === "attendant"){
    return <AttendantDashboard staff={staff}/>;
  }

  return (
    <div style={{padding:20}}>
      Unknown Role: {staff?.role || "NO ROLE FOUND"}
    </div>
  );
}
""")

print("Dashboard patched")
