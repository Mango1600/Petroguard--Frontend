from pathlib import Path

file = Path("src/pages/AttendantDashboard.jsx")

text = file.read_text()

index = text.find("if (loading)")

if index == -1:
    print("❌ No 'if (loading)' found")
else:
    print("✅ Found loading block around:")
    print("-" * 40)
    print(text[index:index+300])
    print("-" * 40)
