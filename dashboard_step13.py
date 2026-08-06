from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import StationManagement from "./StationManagement";

export default function Dashboard({staff}) {

  const [showStationManagement, setShowStationManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowStationManagement(!showStationManagement)}>
        Station Management
      </button>

      {showStationManagement && (
        <StationManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 13 created")
