from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

if 'CameraCapture' not in text:
    text = text.replace(
        'import { supabase } from "../lib/supabase";',
        'import { supabase } from "../lib/supabase";\nimport CameraCapture from "../components/CameraCapture";'
    )

file.write_text(text)

print("CameraCapture import added")
