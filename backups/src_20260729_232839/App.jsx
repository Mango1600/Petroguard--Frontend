import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import ManagerDashboard from "./pages/ManagerDashboard";
import AttendantDashboard from "./pages/AttendantDashboard";
import Login from "./pages/Login";
import Welcome from "./pages/Welcome";
import ActivateAccount from "./pages/ActivateAccount";
import StaffManagement from "./pages/StaffManagement";
import ShiftSubmission from "./pages/ShiftSubmission";

export default function App() {
  const [staff, setStaff] = useState(null);
  const [page, setPage] = useState("login");
  const [showWelcome, setShowWelcome] = useState(false);

  if (!staff) {
    if (page === "activate") {
      return (
        <ActivateAccount
          goToLogin={() => setPage("login")}
        />
      );
    }

    return (
      <Login
        onLogin={(user) => { setStaff(user); setShowWelcome(true); }}
        goToActivate={() => setPage("activate")}
      />
    );
  }

  if (showWelcome) {
    return (
      <Welcome
        staff={staff}
        continueApp={() => setShowWelcome(false)}
      />
    );
  }

  const role = (staff.role || "").toLowerCase();
  console.log("LOGIN STAFF:", staff, "ROLE:", role);

  if (role === "developer") {
    return <Dashboard staff={staff} />;
  }

  if (role === "manager") {
    return <ManagerDashboard staff={staff} />;
  }

  return <AttendantDashboard staff={staff} />;
}