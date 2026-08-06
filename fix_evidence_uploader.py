from pathlib import Path
import re

path = Path("src/components/EvidenceUploader.jsx")
text = path.read_text()

# Change the callback parameter
text = text.replace(
    "async function handleCapture(imageBase64) {",
    "async function handleCapture(evidenceId) {"
)

# Replace the old Base64 upload logic
pattern = re.compile(
    r"""try\s*\{
.*?if\s*\(onUploaded\)\s*\{
\s*onUploaded\(\);
\s*\}
""",
    re.S,
)

replacement = """try {
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
"""

text = pattern.sub(replacement, text)

path.write_text(text)

print("✅ EvidenceUploader repaired.")
