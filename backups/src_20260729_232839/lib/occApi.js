const OCC_URL = "http://10.125.11.166:5000/api/occ";

export async function getOCC() {
  const response = await fetch(OCC_URL);

  if (!response.ok) {
    throw new Error("OCC connection failed");
  }

  return await response.json();
}
