from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

old = """    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });
"""

new = """    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    console.log("AUTH ERROR:", error);
    console.log("AUTH DATA:", data);

    if (error) {
      setMessage(error.message);
      return;
    }

    if (!data?.user) {
      setMessage("No authenticated user returned.");
      return;
    }
"""

if old in text:
    text = text.replace(old, new, 1)
    p.write_text(text)
    print("✅ Auth debug patch applied")
else:
    print("❌ Sign-in block not found")
