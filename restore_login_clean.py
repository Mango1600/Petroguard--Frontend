from pathlib import Path

path = Path("src/pages/Login.jsx")

text = path.read_text()

start = text.find('    console.log("LOGIN START");')
end = text.find('    console.log("AUTH RESULT:", data.user);')

if start != -1 and end != -1:
    clean = '''    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

'''
    text = text[:start] + clean + text[end:]

path.write_text(text)

print("Login restored to clean auth flow.")
