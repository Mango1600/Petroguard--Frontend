import { useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "./CameraCapture";

export default function EvidenceUploader({
  reconciliationId,
  stationId,
  onUploaded,
}) {
  const [uploading, setUploading] = useState(false);

  async function handleCapture(evidenceId) {
    setUploading(true);

    try {
      const { error: dbError } = await supabase
        .from("evidence")
        .update({
          reconciliation_id: reconciliationId,
          station_id: stationId,
          status: "Pending"
        })
        .eq("id", evidenceId);

      if (dbError) {
        setUploading(false);
        return;
      }

      if (onUploaded) {
        onUploaded(evidenceId);
      }

    } catch (err) {
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





