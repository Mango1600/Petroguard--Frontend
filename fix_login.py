from pathlib import Path

file = Path("src/pages/Login.jsx")
text = file.read_text(encoding="utf-8")

old = """const { data: staff, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id)
      .single();

    if (staffError) {
 console.log("STAFF ERROR:", staffError);
 setMessage(JSON.stringify(staffError));
 return;
}"""

new = """const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);

    if (staffError) {
      console.log(staffError);
      setMessage(staffError.message);
      return;
    }

    if (!staffRows || staffRows.length === 0) {
      setMessage("No staff record linked to this account.");
      return;
    }

    const staff = staffRows[0];"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text, encoding="utf-8")
    print("Login.jsx updated successfully.")
else:
    print("Target block not found.")
