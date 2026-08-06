from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import TankManagement from "./TankManagement";

export default function Dashboard({staff}) {

  const [showTankManagement, setShowTankManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowTankManagement(!showTankManagement)}>
        Tank Management
      </button>

      {showTankManagement && (
        <TankManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 15 created")
