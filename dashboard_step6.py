from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";

export default function Dashboard({staff}) {

  const [showTankReadings, setShowTankReadings] = useState(false);
  const [showPumpReadings, setShowPumpReadings] = useState(false);
  const [showFuelSales, setShowFuelSales] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowTankReadings(!showTankReadings)}>
        Tank Readings
      </button>

      <button onClick={() => setShowPumpReadings(!showPumpReadings)}>
        Pump Readings
      </button>

      <button onClick={() => setShowFuelSales(!showFuelSales)}>
        Fuel Sales
      </button>

    </div>
  );
}
""")

print("Dashboard step 6 created")
