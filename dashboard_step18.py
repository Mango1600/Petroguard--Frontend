from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import InventoryManagement from "./InventoryManagement";

export default function Dashboard({staff}) {

  const [showInventoryManagement, setShowInventoryManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowInventoryManagement(!showInventoryManagement)}>
        Inventory Management
      </button>

      {showInventoryManagement && (
        <InventoryManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 18 created")
