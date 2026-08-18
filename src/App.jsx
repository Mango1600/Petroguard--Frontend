import { useState, useEffect } from "react";
import { supabase } from "./lib/supabase";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";

export default function App() {
  const [staff, setStaff] = useState(null);
  const [checkingSession, setCheckingSession] = useState(true);
  const [sessionIdentity, setSessionIdentity] = useState(null);

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

      setSessionIdentity({
        id: user.id,
        email: user.email,
      });

      console.log("AUTHENTICATED EMAIL:", user.email);
      console.log("AUTHENTICATED USER ID:", user.id);

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
    <>
      <div style={{
        padding: 10,
        background: "#fff3cd",
        borderBottom: "1px solid #e0c36d",
        fontSize: 14
      }}>
        <strong>AUTH SESSION:</strong>{" "}
        {sessionIdentity?.email || "unknown"}
        <br />
        <strong>STAFF:</strong>{" "}
        {staff.name || "-"}
        <br />
        <strong>ROLE:</strong>{" "}
        {staff.role || "-"}
        <br />
        <button
          onClick={async () => {
            await supabase.auth.signOut();
            window.location.reload();
          }}
          style={{
            marginTop: 8,
            padding: "8px 14px"
          }}
        >
          SIGN OUT
        </button>
      </div>

      <Dashboard staff={staff} />
    </>
  );
}
