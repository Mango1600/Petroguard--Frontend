from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

old = 'const { data } = await supabase.auth.getSession();'

new = '''const { data } = await supabase.auth.getSession();

      console.log("APP SESSION:", data.session);'''

if old in text:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ APP SESSION debug added")
else:
    print("❌ getSession line not found")
