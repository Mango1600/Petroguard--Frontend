from pathlib import Path

Path("src/components/VideoCapture.jsx").write_text("""
import { uploadVideoEvidence } from "../services/evidenceService";

export default function VideoCapture() {
  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      EVIDENCE SERVICE IMPORT OK
    </div>
  );
}
""")

print("VideoCapture import test created")
