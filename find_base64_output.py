from pathlib import Path

for path in Path("src").rglob("*.jsx"):
    try:
        text = path.read_text(errors="ignore")
    except Exception:
        continue

    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        if any(x in line for x in [
            "openingEvidence",
            "closingEvidence",
            "evidence",
            "imageData",
            "photo",
            "{photo}",
            "{evidence}",
            "{imageData}"
        ]):
            print(f"\n{path}:{i}")
            print(line.strip())
