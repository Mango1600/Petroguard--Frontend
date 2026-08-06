from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";

export default function Dashboard({staff}) {

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <h2>Operations Control Center (OCC)</h2>

      <p>Enterprise Fuel Station Operating System</p>

      <hr />

      <h3>🟢 Business Day: OPEN</h3>

      <p>Welcome, {staff?.name}</p>

      <h3>📈 Today's KPIs</h3>

      <p>⛽ Litres Sold: 0 L</p>
      <p>💰 Expected Revenue: ₦0</p>
      <p>📊 Transactions: 0</p>

    </div>
  );
}
""")

print("Dashboard step 5 created")
