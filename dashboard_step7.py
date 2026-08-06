from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import TankReadings from "./TankReadings";

export default function Dashboard({staff}) {

  const [showTankReadings, setShowTankReadings] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowTankReadings(!showTankReadings)}>
        Tank Readings
      </button>

      {showTankReadings && (
        <TankReadings />
      )}

    </div>
  );
}
""")

print("Dashboard step 7 created")
