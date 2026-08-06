from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

old = '''    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id)
      .limit(1);'''

new = '''    const staffPromise = supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id)
      .limit(1);

    const timeoutPromise = new Promise((_, reject) =>
      setTimeout(() => reject(new Error("STAFF QUERY TIMEOUT")), 10000)
    );

    const { data: staffRows, error: staffError } =
      await Promise.race([staffPromise, timeoutPromise]);'''

if old in text:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Timeout patch applied")
else:
    print("❌ Query block not found")
