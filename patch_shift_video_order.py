from pathlib import Path

p = Path("src/pages/OpenShift.jsx")
text = p.read_text()

old = """if (showVideo) {
    return (
      <VideoCapture
        stationId={staff.station_id}
        staffId={staff.id}
        recordId={staff.id}
        onComplete={async () => {
          setShowVideo(false);
          await createShift();
        }}
      />
    );
  }"""

new = """if (showVideo) {
    return (
      <VideoCapture
        stationId={staff.station_id}
        staffId={staff.id}
        recordId={activeShift?.id}
        onComplete={async () => {
          setShowVideo(false);
        }}
      />
    );
  }"""

if old in text:
    text = text.replace(old, new)
else:
    print("⚠️ Video block not found")

p.write_text(text)

print("✅ Video now waits for existing shift")
