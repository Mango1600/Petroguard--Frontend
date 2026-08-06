from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

old = """    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);

    console.log("STAFF RESULT", staffRows, staffError);

    if (staffError) {
      setMessage("STAFF ERROR: " + staffError.message);
      return;
    }

    setMessage("STAFF ROWS: " + String(staffRows ? staffRows.length : 0));

    if (!staffRows || staffRows.length === 0) {
      setMessage("No staff record linked to this account.");
      return;
    }

    const staff = staffRows[0];

    if (staff.status !== "active") {
      setMessage("Account is not active");
      return;
    }

    onLogin(staff);
"""

new = """    try {

      const { data: staffRows, error: staffError } = await supabase
        .from("staff")
        .select("*")
        .eq("user_id", user.id);

      if (staffError) throw staffError;

      setMessage("STAFF ROWS: " + (staffRows?.length || 0));

      if (!staffRows || staffRows.length === 0) {
        setMessage("No staff record linked.");
        return;
      }

      const staff = staffRows[0];

      if (staff.status !== "active") {
        setMessage("Account is not active");
        return;
      }

      onLogin(staff);

    } catch (err) {
      console.error(err);
      setMessage("LOGIN ERROR: " + (err.message || String(err)));
      return;
    }
"""

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Login debug patch applied")
else:
    print("❌ Pattern not found. Login.jsx has changed.")
