from pathlib import Path
import re

text = Path(".env").read_text()

for line in text.splitlines():
    if line.startswith("VITE_SUPABASE_URL"):
        print(line)

    if line.startswith("VITE_SUPABASE_ANON_KEY"):
        key=line.split("=",1)[1]
        print("KEY LENGTH:", len(key))
