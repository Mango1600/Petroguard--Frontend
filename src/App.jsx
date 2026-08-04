import { useState } from "react";
import Login from "./pages/Login";
import AttendantDashboard from "./pages/AttendantDashboard";

export default function App() {
  return <div style={{padding:"30px",color:"black",background:"white"}}>PETROGUARD APP TEST</div>;

  const [staff, setStaff] = useState(null);

  if (!staff) {
    return <Login onLogin={setStaff} />;
  }

  return (
    <AttendantDashboard staff={staff} />
  );
}
