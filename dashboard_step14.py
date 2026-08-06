from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import PumpManagement from "./PumpManagement";

export default function Dashboard({staff}) {

  const [showPumpManagement, setShowPumpManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowPumpManagement(!showPumpManagement)}>
        Pump Management
      </button>

      {showPumpManagement && (
        <PumpManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 14 created")
