from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
t = p.read_text()

old = """onComplete={async () => {
          setShowVideo(false);
        }}"""

new = """onComplete={async () => {
          setShowVideo(false);
          await createShift();
        }}"""

if old in t:
    t = t.replace(old, new)
    p.write_text(t)
    print("✅ OpenShift video completion fixed")
else:
    print("❌ Pattern not found")
