from pathlib import Path

p = Path("src/pages/Login.jsx")
text = p.read_text()

text = text.replace(
'''    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);
''',
'''    setMessage("Auth OK - Loading staff...");
    
    const { data: staffRows, error: staffError } = await supabase
      .from("staff")
      .select("*")
      .eq("user_id", user.id);

    console.log("STAFF RESULT", staffRows, staffError);
'''
)

p.write_text(text)
print("staff debug added")
