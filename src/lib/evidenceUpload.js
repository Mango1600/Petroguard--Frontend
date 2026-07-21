import { supabase } from "./supabase";

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

export async function uploadEvidence(imageData, fileName) {
  try {
    const blob = dataURLtoBlob(imageData);

    const filePath = `evidence/${Date.now()}-${fileName}`;

    const { error } = await supabase.storage
      .from("petroguard-evidence")
      .upload(filePath, blob, {
        contentType: "image/jpeg",
      });

    if (error) {
      throw error;
    }

    const { data } = supabase.storage
      .from("petroguard-evidence")
      .getPublicUrl(filePath);

    return {
      success: true,
      url: data.publicUrl,
      path: filePath,
    };

  } catch (error) {
    console.error("Evidence upload failed:", error);

    return {
      success: false,
      error: error.message,
    };
  }
}
