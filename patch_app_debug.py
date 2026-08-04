from pathlib import Path

file = Path("src/App.jsx")

text = file.read_text()

old = """export default function App() {
"""

new = """export default function App() {
  console.log("APP STARTED");
"""

if "APP STARTED" not in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("App debug line added.")
else:
    print("App debug line already exists.")
