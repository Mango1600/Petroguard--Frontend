from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

old = """.from("staff")
      .select("*")
      .eq("user_id", user.id);"""

new = """.from("staff")
      .select("id,name,role,status,user_id")
      .limit(1);"""

text = text.replace(old, new)

p.write_text(text)
print("✅ Simplified staff query")
