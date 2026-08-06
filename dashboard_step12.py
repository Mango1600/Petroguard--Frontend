from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
import { useState } from "react";
import StaffManagement from "./StaffManagement";

export default function Dashboard({staff}) {

  const [showStaffManagement, setShowStaffManagement] = useState(false);

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

      <p>Welcome, {staff?.name}</p>

      <button onClick={() => setShowStaffManagement(!showStaffManagement)}>
        Staff Management
      </button>

      {showStaffManagement && (
        <StaffManagement />
      )}

    </div>
  );
}
""")

print("Dashboard step 12 created")
