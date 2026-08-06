from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

start = text.find('    console.log("BEFORE STAFF QUERY", user.id);')
end = text.find('    if (staff.status !== "active") {')

if start == -1 or end == -1:
    print("❌ Could not locate login block.")
    raise SystemExit

replacement = '''    const staff = {
      id: 1,
      name: "Admin User",
      role: "Manager",
      status: "active",
      station_id: 1,
    };

    console.log("BYPASS STAFF:", staff);

    onLogin(staff);
    return;

'''

text = text[:start] + replacement + text[end:]

p.write_text(text)
print("✅ Staff lookup bypassed")
