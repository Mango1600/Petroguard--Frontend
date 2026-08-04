from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
text = p.read_text()

if 'import { supabase } from "../lib/supabase";' in text:
    print("✅ Supabase import already exists")

print("✅ Ready for storage upload patch")
