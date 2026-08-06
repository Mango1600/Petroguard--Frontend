from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import BusinessDayManagement from "./BusinessDayManagement";

export default function Dashboard({staff}) {

  const [showBusinessDayManagement, setShowBusinessDayManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowBusinessDayManagement(!showBusinessDayManagement)}>
        Business Day Management
      </button>

      {showBusinessDayManagement && (
        <BusinessDayManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 20 created")
