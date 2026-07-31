import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function EvidenceViewer({ reconciliationId }) {
  const [evidence, setEvidence] = useState([]);

  useEffect(() => {
    loadEvidence();
  }, [reconciliationId]);

  async function loadEvidence() {
    const { data, error } = await supabase
      .from("evidence")
      .select("*")
      .eq("reconciliation_id", reconciliationId)
      .order("created_at", { ascending: false });

    if (error) {
      console.error(error);
      return;
    }

    setEvidence(data || []);
  }

  if (evidence.length === 0) {
    return <p>No evidence uploaded.</p>;
  }

  return (
    <div>
      <h4>Uploaded Evidence</h4>

      {evidence.map((item) => (
        <div
          key={item.id}
          style={{
            border: "1px solid #ccc",
            padding: "10px",
            marginBottom: "10px",
            borderRadius: "8px",
          }}
        >
          <p><strong>Type:</strong> {item.evidence_type}</p>
          <p><strong>File:</strong> {item.file_name}</p>
          <p><strong>Status:</strong> {item.status}</p>
          <p><strong>Captured:</strong> {item.capture_time}</p>
        </div>
      ))}
    </div>
  );
}
