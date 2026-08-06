from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import FuelDeliveryManagement from "./FuelDeliveryManagement";

export default function Dashboard({staff}) {

  const [showFuelDeliveryManagement, setShowFuelDeliveryManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowFuelDeliveryManagement(!showFuelDeliveryManagement)}>
        Fuel Delivery Management
      </button>

      {showFuelDeliveryManagement && (
        <FuelDeliveryManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 17 created")
