import { useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "./CameraCapture";

export default function EvidenceUploader({
  reconciliationId,
  stationId,
  onUploaded,
}) {
  const [uploading, setUploading] = useState(false);

  async function handleCapture(imageBase64) {
    setUploading(true);

    try {
      const response = await fetch(imageBase64);
      const blob = await response.blob();

      const file = new File(
        [blob],
        `evidence-${Date.now()}.jpg`,
        { type: "image/jpeg" }
      );

      const filePath = `${reconciliationId}/${file.name}`;

      const { error: uploadError } = await supabase.storage
        .from("petroguard-evidence")
        .upload(filePath, file);

      if (uploadError) {
        alert("Storage error: " + uploadError.message);
        setUploading(false);
        return;
      }

      const { error: dbError } = await supabase
        .from("evidence")
        .insert([
          {
            reconciliation_id: reconciliationId,
            station_id: stationId,
            evidence_type: "photo",
            file_name: file.name,
            file_path: filePath,
            mime_type: file.type,
            file_size: file.size,
            capture_time: new Date().toISOString(),
            status: "Pending",
          },
        ]);

      if (dbError) {
        alert("Database error: " + dbError.message);
        setUploading(false);
        return;
      }

      alert("Evidence uploaded successfully");

      if (onUploaded) {
        onUploaded();
      }

    } catch (err) {
      alert(err.message);
    }

    setUploading(false);
  }

  return (
    <div>
      <CameraCapture onCapture={handleCapture} />

      {uploading && <p>Uploading evidence...</p>}
    </div>
  );
}






