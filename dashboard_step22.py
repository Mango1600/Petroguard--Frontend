from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import OperationsAnalysis from "./OperationsAnalysis";

export default function Dashboard({staff}) {

  const [showOperationsAnalysis, setShowOperationsAnalysis] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowOperationsAnalysis(!showOperationsAnalysis)}>
        Operations Analysis
      </button>

      {showOperationsAnalysis && (
        <OperationsAnalysis />
      )}

    </div>
  );
}
""")

print("Dashboard step 22 created")
