from pathlib import Path

Path("src/App.jsx").write_text("""
import Login from "./pages/Login";

export default function App() {
  return (
    <div>
      <Login />
    </div>
  );
}
""")

print("Login import test created")
