import { useState, useEffect } from "react";
import { supabase } from "./lib/supabase";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";

export default function App() {
  const [staff, setStaff] = useState(null);
  const [checkingSession, setCheckingSession] = useState(true);

  useEffect(() => {
    async function checkSession() {
      const { data } = await supabase.auth.getSession();

      console.log("APP SESSION:", data.session);

      console.log("APP SESSION:", data.session);

      if (!data.session) {
        setCheckingSession(false);
        return;
      }

      const user = data.session.user;

      const { data: staffRows, error: staffError } = await supabase
        .from("staff")
        .select("*")
        .eq("user_id", user.id)
        .limit(1);

      

      console.log("APP STAFF RESULT:", staffRows);
      console.log("APP STAFF ERROR:", staffError);

      if (staffRows && staffRows.length > 0) {
        setStaff(staffRows[0]);
      }

      setCheckingSession(false);
    }

    checkSession();
  }, []);

  if (checkingSession) {
    return <div style={{padding:20}}>Loading...</div>;
  }

  if (!staff) {
    return <Login onLogin={setStaff} />;
  }

  return (
    <Dashboard
      staff={staff}
    />
  );
}
