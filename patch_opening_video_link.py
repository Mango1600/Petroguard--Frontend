from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
text = p.read_text()

text = text.replace(
'''<VideoCapture
        stationId={staff.station_id}
        staffId={staff.id}
        recordId={activeShift?.id}
        onComplete={async () => {
          setShowVideo(false);
        }}
      />''',
'''<VideoCapture
        shiftId={activeShift?.id}
        stationId={staff.station_id}
        staffId={staff.id}
        evidenceType="opening_shift_video"
        onComplete={async () => {
          setShowVideo(false);
        }}
      />'''
)

p.write_text(text)

print("✅ Opening video evidence linked to shift")
