from pathlib import Path

path = Path("src/pages/TankDipEntry.jsx")
text = path.read_text()

old = """if (evidenceImage) {
  await uploadEvidence({
    imageData: evidenceImage,
    fileName: "tank-dip-photo.jpg",
    stationId: staff.station_id,
    recordId: reading.id,
    moduleName: "tank_readings",
    evidenceType: "TANK_DIP_PHOTO",
    uploadedBy: staff.id,
  });
}"""

new = """if (evidenceImage) {
  await supabase
    .from("evidence_links")
    .update({
      module_name: "tank_readings",
      record_id: String(reading.id),
    })
    .eq("evidence_id", evidenceImage);
}"""

if old in text:
    text = text.replace(old, new)
    path.write_text(text)
    print("✅ TankDipEntry repaired.")
else:
    print("❌ Pattern not found.")
