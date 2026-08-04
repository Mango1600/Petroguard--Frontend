from pathlib import Path

p = Path("src/main.jsx")
text = p.read_text(encoding="utf-8")

text = text.replace('import eruda from "eruda";\n', "")
text = text.replace("eruda.init();\n", "")

p.write_text(text, encoding="utf-8")

print("✅ eruda removed from main.jsx")
