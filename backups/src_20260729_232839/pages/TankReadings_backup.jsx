import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function TankReadings() {
  const [readings, setReadings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    loadTankReadings();
  }, []);

  async function loadTankReadings() {
    setLoading(true);

    const { data, error } = await supabase
      .from("tank_readings")
      .select(`
        id,
        product_type,
        opening_volume,
        closing_volume,
        deliveries,
        expected_volume,
        variance,
        status,
        reading_date,
        stations (
          name
        ),
        tanks (
          tank_name
        )
      `)
      .order("id", { ascending: false });

    if (error) {
      setErrorMessage(error.message);
      setLoading(false);
      return;
    }

    setReadings(data || []);
    setLoading(false);
  }

  function formatNumber(value) {
    return Number(value || 0).toLocaleString();
  }

  function varianceStatus(value) {
    if (value < 0) {
      return {
        text: `Loss: ${formatNumber(Math.abs(value))} L`,
        color: "#DC2626",
      };
    }

    if (value > 0) {
      return {
        text: `Gain: ${formatNumber(value)} L`,
        color: "#16A34A",
      };
    }

    return {
      text: "Balanced",
      color: "#64748B",
    };
  }

  if (loading) {
    return <p>Loading tank readings...</p>;
  }

  if (errorMessage) {
    return <p>Error: {errorMessage}</p>;
  }

  return (
    <div style={{ padding: "16px" }}>
      <h2>⛽ Tank Readings</h2>

      {readings.length === 0 ? (
        <p>No tank readings found.</p>
      ) : (
        readings.map((reading) => {
          const variance = varianceStatus(reading.variance);

          return (
            <div
              key={reading.id}
              style={{
                background: "#ffffff",
                borderRadius: "12px",
                padding: "16px",
                marginBottom: "16px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
              }}
            >
              <h3>
                ⛽ {reading.stations?.name || "Unknown Station"}
              </h3>

              <h4>
                {reading.tanks?.tank_name || "Unknown Tank"}
              </h4>

              <p>
                <strong>Product:</strong>{" "}
                {reading.product_type}
              </p>

              <p>
                <strong>Date:</strong>{" "}
                {reading.reading_date}
              </p>

              <hr />

              <p>
                Opening: {formatNumber(reading.opening_volume)} L
              </p>

              <p>
                Deliveries: {formatNumber(reading.deliveries)} L
              </p>

              <p>
                Expected: {formatNumber(reading.expected_volume)} L
              </p>

              <p>
                Closing: {formatNumber(reading.closing_volume)} L
              </p>

              <h3 style={{ color: variance.color }}>
                {variance.text}
              </h3>

              <p>
                Status: <strong>{reading.status}</strong>
              </p>

              <div
                style={{
                  marginTop: "12px",
                  padding: "10px",
                  borderRadius: "8px",
                  background: "#F1F5F9",
                }}
              >
                📷 Evidence Center (Coming Soon)
              </div>
            </div>
          );
        })
      )}
    </div>
  );
}

export default TankReadings;
