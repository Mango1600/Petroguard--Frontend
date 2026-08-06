from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import FuelSales from "./FuelSales";

export default function Dashboard({staff}) {

  const [showFuelSales, setShowFuelSales] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowFuelSales(!showFuelSales)}>
        Fuel Sales
      </button>

      {showFuelSales && (
        <FuelSales />
      )}

    </div>
  );
}
""")

print("Dashboard step 9 created")
