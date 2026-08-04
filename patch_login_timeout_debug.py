from pathlib import Path

path = Path("src/pages/Login.jsx")

text = path.read_text()

old = '''const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });'''

new = '''console.log("LOGIN START");

    const loginPromise = supabase.auth.signInWithPassword({
      email,
      password,
    });

    const timeoutPromise = new Promise((resolve) =>
      setTimeout(() => resolve({
        data: null,
        error: { message: "Login timeout after 10 seconds" }
      }), 10000)
    );

    const { data, error } = await Promise.race([
      loginPromise,
      timeoutPromise
    ]);

    console.log("LOGIN RESULT", data, error);'''

if old not in text:
    print("Target not found")
    raise SystemExit

text = text.replace(old, new)

path.write_text(text)

print("Login timeout debug added")
