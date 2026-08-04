
from pathlib import Path

path = Path("src/pages/Login.jsx")

text = path.read_text()

text = text.replace(
'const { data, error } = await supabase.auth.signInWithPassword({',
'console.log("LOGIN START");\n\n    const { data, error } = await supabase.auth.signInWithPassword({'
)

text = text.replace(
'const user = data.user;',
'console.log("AUTH RESULT:", data.user);\n\n    const user = data.user;'
)

text = text.replace(
'if (staffError) {',
'console.log("STAFF QUERY RESULT:", staffRows, staffError);\n\n    if (staffError) {'
)

path.write_text(text)

print("Login debug added")
