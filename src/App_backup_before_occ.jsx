import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import ActivateAccount from "./pages/ActivateAccount";

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

  return <Dashboard staff={staff} />;
}