import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function EvidenceUploader({
  reconciliationId,
  stationId,
  onUploaded,
}) {
  const [uploading, setUploading] = useState(false);

  async function upload(file) {
    if (!file) return;

    setUploading(true);

    const filePath = `${reconciliationId}/${Date.now()}-${file.name}`;

    const { error: uploadError } = await supabase.storage
      .from("petroguard-evidence")
      .upload(filePath, file);

    if (uploadError) {
      alert(uploadError.message);
      setUploading(false);
      return;
    }

    const { error: dbError } = await supabase
      .from("evidence")
      .insert([
        {
          reconciliation_id: reconciliationId,
          station_id: stationId,
          evidence_type: file.type.startsWith("video")
            ? "video"
            : "photo",
          file_name: file.name,
          file_path: filePath,
          mime_type: file.type,
          file_size: file.size,
          capture_time: new Date().toISOString(),
          status: "Pending",
        },
      ]);

    setUploading(false);

    if (dbError) {
      alert(dbError.message);
      return;
    }

    alert("Evidence uploaded successfully");

    if (onUploaded) {
      onUploaded();
    }
  }

  return (
    <div>
      <input
        type="file"
        accept="image/*,video/*"
        capture="environment"
        disabled={uploading}
        onChange={(e) => upload(e.target.files[0])}
      />

      {uploading && <p>Uploading...</p>}
    </div>
  );
}

