from pathlib import Path

root = Path("src")

for f in sorted(root.rglob("*")):
    if f.suffix not in [".jsx", ".js"]:
        continue

    try:
        text = f.read_text()
    except:
        continue

    if "ManagerDashboard" in text or "manager@petroguard.com" in text:
        print("\n" + "="*60)
        print(f)
        print("="*60)

        for i, line in enumerate(text.splitlines(), 1):
            if "ManagerDashboard" in line or "manager@petroguard.com" in line:
                print(f"{i}: {line}")
