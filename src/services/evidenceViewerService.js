import { supabase } from "../lib/supabase";

export async function getEvidenceByRecord({
  moduleName,
  recordId,
}) {
  try {
    const { data, error } = await supabase
      .from("evidence_links")
      .select(`
        id,
        module_name,
        record_id,
        evidence (
          id,
          evidence_type,
          file_name,
          file_path,
          mime_type,
          capture_time,
          latitude,
          longitude,
          status,
          created_at
        )
      `)
      .eq("module_name", moduleName)
      .eq("record_id", String(recordId));

    if (error) throw error;

    return {
      success: true,
      data,
    };

  } catch (error) {
    console.error("Evidence Viewer Error:", error);

    return {
      success: false,
      error,
    };
  }
}
