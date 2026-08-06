from pathlib import Path

p = Path("src/services/evidenceService.js")

text = p.read_text()

if "export async function uploadVideoEvidence" not in text:

    text += '''

export async function uploadVideoEvidence({
  videoBlob,
  fileName,
  stationId,
  recordId,
  moduleName,
  uploadedBy = null,
  description = null
}) {

  return await uploadEvidence({
    videoBlob,
    fileName,
    stationId,
    recordId,
    moduleName,
    evidenceType: "VIDEO",
    uploadedBy,
    description
  });

}
'''

p.write_text(text)

print("✅ Added uploadVideoEvidence export")
