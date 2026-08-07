from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

text = text.replace(
'import { useState } from "react";',
'import { useState, useEffect } from "react";\nimport { supabase } from "./lib/supabase";'
)

text = text.replace(
'  const [staff, setStaff] = useState(null);',
'''  const [staff, setStaff] = useState(null);
  const [checkingSession, setCheckingSession] = useState(true);

  useEffect(() => {
    async function checkSession() {
      const { data } = await supabase.auth.getSession();

      if (!data.session) {
        setCheckingSession(false);
        return;
      }

      const user = data.session.user;

      const { data: staffRows } = await supabase
        .from("staff")
        .select("*")
        .eq("user_id", user.id)
        .limit(1);

      if (staffRows && staffRows.length > 0) {
        setStaff(staffRows[0]);
      }

      setCheckingSession(false);
    }

    checkSession();
  }, []);'''
)

text = text.replace(
'  if (!staff) {',
'''  if (checkingSession) {
    return <div style={{padding:20}}>Loading...</div>;
  }

  if (!staff) {'''
)

file.write_text(text)

print("✅ App.jsx session handling added")
