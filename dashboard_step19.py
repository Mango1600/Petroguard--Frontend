from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import AlertsManagement from "./AlertsManagement";

export default function Dashboard({staff}) {

  const [showAlertsManagement, setShowAlertsManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowAlertsManagement(!showAlertsManagement)}>
        Alerts Management
      </button>

      {showAlertsManagement && (
        <AlertsManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 19 created")
