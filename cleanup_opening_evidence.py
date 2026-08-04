from pathlib import Path

p = Path("src/pages/AttendantPumpReading.jsx")
code = p.read_text()

old = """
        <p>
          ✅ Opening Evidence Saved
        </p>
      )}
"""

code = code.replace(old, "")

p.write_text(code)

print("✅ Removed orphan JSX block")
