import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import ManagerDashboard from "./pages/ManagerDashboard";
import AttendantDashboard from "./pages/AttendantDashboard";
import Login from "./pages/Login";
import ActivateAccount from "./pages/ActivateAccount";
import StaffManagement from "./pages/StaffManagement";

export default function App() {
  const [staff, setStaff] = useState(null);
  const [page, setPage] = useState("login");

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
        onLogin={setStaff}
        goToActivate={() => setPage("activate")}
      />
    );
  }

  const role = (staff.role || "").toLowerCase();

  if (role === "developer") {
    return <Dashboard staff={staff} />;
  }

  if (role === "manager") {
    return <ManagerDashboard staff={staff} />;
  }

  return <AttendantDashboard staff={staff} />;
}
