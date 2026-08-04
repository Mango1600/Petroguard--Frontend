from pathlib import Path

root = Path(".")

extensions = {".js", ".jsx", ".ts", ".tsx"}

removed = 0

for file in root.rglob("*"):
    if file.suffix not in extensions:
        continue

    try:
        text = file.read_text(encoding="utf-8")
    except Exception:
        continue

    original = text

    lines = []
    for line in text.splitlines():
        s = line.strip()

        if s.startswith("alert("):
            removed += 1
            continue

        if "LOGIN SUCCESS" in line:
            removed += 1
            continue

        if "console.log(" in line and (
            "LOGIN" in line.upper()
            or "staff" in line.lower()
            or "json.stringify" in line.lower()
        ):
            removed += 1
            continue

        lines.append(line)

    text = "\n".join(lines)

    if text != original:
        file.write_text(text, encoding="utf-8")
        print("Cleaned:", file)

print(f"\nRemoved {removed} debug statements.")
