from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import FuelPriceManagement from "./FuelPriceManagement";

export default function Dashboard({staff}) {

  const [showFuelPriceManagement, setShowFuelPriceManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowFuelPriceManagement(!showFuelPriceManagement)}>
        Fuel Price Management
      </button>

      {showFuelPriceManagement && (
        <FuelPriceManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 16 created")
