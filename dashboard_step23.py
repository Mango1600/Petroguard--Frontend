from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import AttendantDashboard from "./AttendantDashboard";

export default function Dashboard({staff}) {

  return (
    <AttendantDashboard staff={staff}/>
  );
}
""")

print("Attendant full render test created")
