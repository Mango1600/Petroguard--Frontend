from pathlib import Path

f = Path("src/services/evidenceService.js")
text = f.read_text(encoding="utf-8")

if "export async function uploadVideoEvidence" not in text:
    text += """

export async function uploadVideoEvidence({
  videoBlob,
  fileName,
  stationId,
  recordId,
  moduleName,
  uploadedBy = null,
  description = null,
}) {
  try {
    const filePath = `${moduleName}/${Date.now()}-${fileName}`;

    const { error } = await supabase.storage
      .from(APP_CONFIG.STORAGE.EVIDENCE_BUCKET)
      .upload(filePath, videoBlob, {
        contentType: "video/webm",
        upsert: false,
      });

    if (error) throw error;

    return {
      success: true,
      filePath,
    };
  } catch (error) {
    console.error("Video Upload Error:", error);
    return {
      success: false,
      error,
    };
  }
}
"""
    f.write_text(text, encoding="utf-8")
    print("✅ uploadVideoEvidence() added.")
else:
    print("Already exists.")
