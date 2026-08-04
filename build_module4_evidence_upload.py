from pathlib import Path

path = Path("src/components/CameraCapture.jsx")
text = path.read_text()

# Add Supabase import
if 'import { supabase } from "../lib/supabase";' not in text:
    text = text.replace(
        'import { useRef, useState, useEffect } from "react";',
        'import { useRef, useState, useEffect } from "react";\nimport { supabase } from "../lib/supabase";'
    )

# Add upload function before usePhoto
marker = "  function usePhoto() {"

upload_code = r'''
  async function uploadEvidence() {

    if (!capturedPhoto) return null;

    const response = await fetch(capturedPhoto);
    const blob = await response.blob();

    const fileName =
      `opening/${Date.now()}.jpg`;

    const { data, error } =
      await supabase.storage
        .from("petroguard-evidence")
        .upload(fileName, blob, {
          contentType: "image/jpeg"
        });

    if (error) {
      console.error(error);
      setError("Evidence upload failed.");
      return null;
    }

    return data.path;
  }

'''

if upload_code not in text:
    text = text.replace(marker, upload_code + marker)

# Replace usePhoto function
old = r'''
  function usePhoto() {
    if (onCapture && capturedPhoto) {
      onCapture(capturedPhoto);
    }
  }
'''

new = r'''
  async function usePhoto() {

    const path = await uploadEvidence();

    if (onCapture && path) {
      onCapture(path);
    }
  }
'''

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Evidence upload connected.")
