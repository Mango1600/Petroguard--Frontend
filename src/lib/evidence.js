export async function collectEnterpriseEvidence(photo, video = null) {

  const timestamp = new Date().toISOString();

  let latitude = null;
  let longitude = null;

  if (navigator.geolocation) {
    try {
      const pos = await new Promise((resolve, reject) =>
        navigator.geolocation.getCurrentPosition(resolve, reject)
      );

      latitude = pos.coords.latitude;
      longitude = pos.coords.longitude;

    } catch (_) {}
  }

  const deviceId = navigator.userAgent;

  const network =
    navigator.connection?.effectiveType ?? null;

  let battery = null;

  if (navigator.getBattery) {
    try {
      const b = await navigator.getBattery();
      battery = Math.round(b.level * 100);
    } catch (_) {}
  }

  return {
    photo,
    video,

    latitude,
    longitude,

    timestamp,

    device_id: deviceId,

    network,

    battery,

    sha256_hash: null,

    ai_verified: false,

    evidence_locked: false
  };

}
