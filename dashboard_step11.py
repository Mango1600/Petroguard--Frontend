from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import ManagerDashboard from "./ManagerDashboard";

export default function Dashboard({staff}) {

  const [showManagerDashboard, setShowManagerDashboard] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowManagerDashboard(!showManagerDashboard)}>
        Manager Dashboard
      </button>

      {showManagerDashboard && (
        <ManagerDashboard />
      )}

    </div>
  );
}
""")

print("Dashboard step 11 created")
