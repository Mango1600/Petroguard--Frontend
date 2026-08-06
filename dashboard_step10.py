from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import DailyReconciliation from "./DailyReconciliation";

export default function Dashboard({staff}) {

  const [showDailyReconciliation, setShowDailyReconciliation] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowDailyReconciliation(!showDailyReconciliation)}>
        Daily Reconciliation
      </button>

      {showDailyReconciliation && (
        <DailyReconciliation />
      )}

    </div>
  );
}
""")

print("Dashboard step 10 created")
