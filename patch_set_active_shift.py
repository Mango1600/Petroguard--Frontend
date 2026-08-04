from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
text = p.read_text()

old = """    await loadActiveShift();

    setMessage("✅ Shift opened");"""

new = """    setActiveShift(newShift);

    setMessage("✅ Shift opened");"""

if old in text:
    text = text.replace(old, new)
else:
    print("⚠️ Target text not found")

p.write_text(text)

print("✅ Active shift linked")
