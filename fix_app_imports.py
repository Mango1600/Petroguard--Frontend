from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text(encoding="utf-8")

if 'import ActivateAccount from "./pages/ActivateAccount";' not in text:
    text = text.replace(
        'import Login from "./pages/Login";',
        '''import Login from "./pages/Login";
import ActivateAccount from "./pages/ActivateAccount";
import Welcome from "./pages/Welcome";'''
    )

file.write_text(text, encoding="utf-8")

print("✅ App.jsx imports repaired.")
