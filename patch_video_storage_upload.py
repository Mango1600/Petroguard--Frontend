from pathlib import Path

p = Path("src/components/VideoCapture.jsx")
text = p.read_text()

old = """        console.log("🎥 Video captured:", blob.size, blob.type);

        if (onComplete) {
          onComplete(blob);
        }"""

new = """        console.log("🎥 Video captured:", blob.size, blob.type);

        try {
          setUploading(true);

          const file = new File(
            [blob],
            `video-${Date.now()}.webm`,
            { type: "video/webm" }
          );

          const filePath = `${shiftId}/${file.name}`;

          const { error: uploadError } =
            await supabase.storage
              .from("petroguard-evidence")
              .upload(filePath, file);

          if (uploadError) {
            console.log(uploadError);
            return;
          }

          const { error: dbError } =
            await supabase
              .from("evidence")
              .insert([{
                shift_id: shiftId,
                station_id: stationId,
                uploaded_by: staffId,
                evidence_type: evidenceType || "shift_video",
                file_name: file.name,
                file_path: filePath,
                mime_type: file.type,
                file_size: file.size,
                capture_time: new Date().toISOString(),
                status: "Pending"
              }]);

          if (dbError) {
            console.log(dbError);
            return;
          }

          console.log("✅ Video evidence saved");

        } finally {
          setUploading(false);
        }

        if (onComplete) {
          onComplete(blob);
        }"""

if old not in text:
    print("Target not found")
else:
    text = text.replace(old, new)
    p.write_text(text)
    print("✅ Video storage upload added")
