from pathlib import Path
import re

p = Path("src/pages/Login.jsx")
text = p.read_text()

pattern = r'''    const staff = \{
      id: 1,
      name: "Admin User",
      role: "Manager",
      status: "active",
      station_id: 1,
    \};

    console\.log\("BYPASS STAFF:", staff\);

    onLogin\(staff\);
    return;
'''

replacement = '''    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id)
      .limit(1);

    console.log("STAFF RESULT", staffRows, staffError);

    if (staffError) {
      setMessage("STAFF ERROR: " + staffError.message);
      return;
    }

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
    return;
'''

new_text = re.sub(pattern, replacement, text, flags=re.DOTALL)

if new_text == text:
    print("❌ Bypass block not found.")
else:
    p.write_text(new_text)
    print("✅ Login restored to real staff lookup.")
