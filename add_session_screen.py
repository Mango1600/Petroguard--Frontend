




from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

old = 'const { data } = await supabase.auth.getSession();'

new = '''const { data } = await supabase.auth.getSession();

      console.log("APP SESSION:", data.session);
      alert(JSON.stringify(data.session, null, 2));'''

if old in text:
    text = text.replace(old, new, 1)
    file.write_text(text)
    print("✅ Session alert added")
else:
    print("❌ getSession line not found")
