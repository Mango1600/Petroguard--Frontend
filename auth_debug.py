from pathlib import Path

file = Path("src/pages/Login.jsx")
text = file.read_text(encoding="utf-8")

old = """const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });"""

new = """const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    console.log("========== AUTH RESULT ==========");
    console.log("AUTH DATA:", data);
    console.log("AUTH USER:", data?.user);
    console.log("AUTH SESSION:", data?.session);
    console.log("AUTH ERROR:", error);
    console.log("================================");
"""

text = text.replace(old, new)

file.write_text(text, encoding="utf-8")

print("✅ Authentication debugging added.")
