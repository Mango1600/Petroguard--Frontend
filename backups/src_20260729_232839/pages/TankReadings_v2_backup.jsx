import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function TankReadings() {
  const [readings, setReadings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    loadReadings();
  }, []);

  async function loadReadings() {
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
        stations(name),
        tanks(tank_name)
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

  function litres(value) {
    return Number(value || 0).toLocaleString();
  }

  function getVariance(variance) {
    if (variance < 0) {
      return {
        label: `🔴 Loss ${litres(Math.abs(variance))} L`,
        note: "Review required",
      };
    }

    if (variance > 0) {
      return {
        label: `🟢 Gain ${litres(variance)} L`,
        note: "Above expected",
      };
    }

    return {
      label: "⚪ Balanced",
      note: "No variance",
    };
  }

  function statusBadge(status) {
    const value = status?.toUpperCase();

    if (value === "APPROVED") return "🟢 APPROVED";
    if (value === "VERIFIED") return "🔵 VERIFIED";
    if (value === "SUBMITTED") return "🟡 SUBMITTED";

    return "⚪ DRAFT";
  }

  if (loading) {
    return <p>Loading Tank Readings...</p>;
  }

  if (errorMessage) {
    return <p>Error: {errorMessage}</p>;
  }

  return (
    <div style={{ padding: "16px" }}>
      <h2>⛽ Tank Operations</h2>

      {readings.length === 0 ? (
        <p>No tank readings found.</p>
      ) : (
        readings.map((reading) => {
          const variance = getVariance(reading.variance);

          return (
            <div
              key={reading.id}
              style={{
                background: "#fff",
                borderRadius: "12px",
                padding: "16px",
                marginBottom: "16px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
              }}
            >
              <h3>
                ⛽ {reading.stations?.name || "Unknown Station"}
              </h3>

              <h4>
                {reading.tanks?.tank_name || "Unknown Tank"}
              </h4>

              <p>
                <strong>Product:</strong> {reading.product_type}
              </p>

              <p>
                <strong>Date:</strong> {reading.reading_date}
              </p>

              <hr />

              <p>
                Opening: {litres(reading.opening_volume)} L
              </p>

              <p>
                Deliveries: {litres(reading.deliveries)} L
              </p>

              <p>
                Expected: {litres(reading.expected_volume)} L
              </p>

              <p>
                Closing: {litres(reading.closing_volume)} L
              </p>

              <h3>{variance.label}</h3>
              <p>{variance.note}</p>

              <p>
                <strong>Status:</strong>{" "}
                {statusBadge(reading.status)}
              </p>

              <div
                style={{
                  background: "#F1F5F9",
                  padding: "12px",
                  borderRadius: "8px",
                  marginTop: "12px",
                }}
              >
                📷 Evidence Center
                <br />
                Photo • Video • Verification
              </div>
            </div>
          );
        })
      )}
    </div>
  );
}

export default TankReadings;
