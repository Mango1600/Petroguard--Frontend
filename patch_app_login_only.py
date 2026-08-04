from pathlib import Path

path = Path("src/App.jsx")

code = """import Login from "./pages/Login";

export default function App() {
  return <Login onLogin={()=>{}} />;
}
"""

path.write_text(code)

print("Login-only test applied.")
