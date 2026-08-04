from pathlib import Path

p = Path("src/pages/ShiftClose.jsx")
text = p.read_text()

# Import VideoCapture
text = text.replace(
    'import { supabase } from "../lib/supabase";',
    'import { supabase } from "../lib/supabase";\nimport VideoCapture from "../components/VideoCapture";'
)

# Add showVideo state
text = text.replace(
    'const [message, setMessage] = useState("");',
    'const [message, setMessage] = useState("");\n  const [showVideo, setShowVideo] = useState(false);'
)

# Open video after closing meter is saved
text = text.replace(
    'setMessage(\n      `✅ Closing saved. PetroGuard calculated ${litres} litres`\n    );',
    'setMessage(`✅ Closing saved. PetroGuard calculated ${litres} litres`);\n    setShowVideo(true);'
)

# Show VideoCapture before the normal page
marker = '''  if (!shift) {
    return <div style={{padding:20}}>No active shift found</div>;
  }'''

insert = '''  if (showVideo) {
    return (
      <VideoCapture
        shiftId={shift.id}
        stationId={staff.station_id}
        staffId={staff.id}
        evidenceType="closing_shift_video"
        onComplete={async () => {
          setShowVideo(false);
        }}
      />
    );
  }

''' + marker

text = text.replace(marker, insert)

p.write_text(text)

print("✅ ShiftClose closing video connected")
