import { supabase } from "../lib/supabase";
import { APP_CONFIG } from "../config/appConfig";
import { createAuditLog } from "./auditService";

function dataURLtoBlob(dataURL) {
  const arr = dataURL.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);

  let n = bstr.length;
  const u8arr = new Uint8Array(n);

  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }

  return new Blob([u8arr], { type: mime });
}


export async function uploadEvidence({
  imageData,
  fileName,
  stationId,
  recordId,
  moduleName,
  evidenceType,
  uploadedBy = null,
  companyId = null,
  description = null,
  latitude = null,
  longitude = null,
}) {

  try {

    const blob = dataURLtoBlob(imageData);

    const filePath =
      `${moduleName}/${Date.now()}-${fileName}`;


    const { error: storageError } =
      await supabase.storage
        .from(APP_CONFIG.STORAGE.EVIDENCE_BUCKET)
        .upload(filePath, blob, {
          contentType: "image/jpeg",
          upsert: false,
        });


    if (storageError) throw storageError;


    const { data: evidence, error: evidenceError } =
      await supabase
        .from("evidence")
        .insert({
          company_id: companyId,
          station_id: stationId,
          uploaded_by: uploadedBy,
          evidence_type: evidenceType,
          file_name: fileName,
          file_path: filePath,
          mime_type: "image/jpeg",
          capture_time: new Date(),
          latitude,
          longitude,
          description,
        })
        .select()
        .single();


    if (evidenceError) throw evidenceError;


    const { error: linkError } =
      await supabase
        .from("evidence_links")
        .insert({
          evidence_id: evidence.id,
          module_name: moduleName,
          record_id: String(recordId),
        });


    if (linkError) throw linkError;


    await createAuditLog({
      companyId,
      stationId,
      moduleName,
      recordId,
      action: "EVIDENCE_UPLOADED",
      performedBy: uploadedBy,
      newData: evidence,
    });


    return {
      success: true,
      evidence,
    };


  } catch (error) {

    console.error("Evidence Upload Error:", error);

    return {
      success: false,
      error,
    };

  }
}
