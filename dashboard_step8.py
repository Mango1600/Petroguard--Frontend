from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import PumpReadings from "./PumpReadings";

export default function Dashboard({staff}) {

  const [showPumpReadings, setShowPumpReadings] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowPumpReadings(!showPumpReadings)}>
        Pump Readings
      </button>

      {showPumpReadings && (
        <PumpReadings />
      )}

    </div>
  );
}
""")

print("Dashboard step 8 created")
