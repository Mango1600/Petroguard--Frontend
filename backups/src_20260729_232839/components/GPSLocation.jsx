import { useState } from "react";

export default function GPSLocation({ onLocation }) {
  const [loading, setLoading] = useState(false);
  const [location, setLocation] = useState(null);

  function getLocation() {
    if (!navigator.geolocation) {
      alert("Geolocation is not supported on this device.");
      return;
    }

    setLoading(true);

    navigator.geolocation.getCurrentPosition(
      (position) => {
        const gps = {
          latitude: position.coords.latitude,
          longitude: position.coords.longitude,
        };

        setLocation(gps);

        if (onLocation) {
          onLocation(gps);
        }

        setLoading(false);
      },
      (error) => {
        alert(error.message);
        setLoading(false);
      },
      {
        enableHighAccuracy: true,
        timeout: 10000,
      }
    );
  }

  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "10px",
        borderRadius: "8px",
        marginTop: "10px",
      }}
    >
      <h4>GPS Location</h4>

      <button onClick={getLocation} disabled={loading}>
        {loading ? "Getting Location..." : "Capture GPS"}
      </button>

      {location && (
        <div style={{ marginTop: "10px" }}>
          <p>
            <strong>Latitude:</strong> {location.latitude}
          </p>

          <p>
            <strong>Longitude:</strong> {location.longitude}
          </p>
        </div>
      )}
    </div>
  );
}

