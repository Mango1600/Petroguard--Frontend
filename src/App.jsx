import { useState } from "react";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";

export default function App() {
  const [staff, setStaff] = useState(null);

  if (!staff) {
    return <Login onLogin={setStaff} />;
  }

  return (
    <Dashboard
      staff={staff}
    />
  );
}
