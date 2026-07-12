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
    console.log("Uploading evidence...");

    return {
      success: true,
      imageData,
      fileName,
    };
  } catch (error) {
    console.error(error);

    return {
      success: false,
      error,
    };
  }
}
