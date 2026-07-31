import { uploadEvidence as saveEvidence } from "../services/evidenceService";import { useEffect, useState } from "react";

import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
function TankReadings() {  const [readings, setReadings] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");
const [evidenceImage, setEvidenceImage] = useState(null);
  useEffect(() => {
    loadReadings();
  }, []);
async function uploadEvidence(imageData, readingId) {
  console.log("Preparing evidence upload");

  setEvidenceImage(imageData);

  const result = await saveEvidence({
    imageData,
    fileName: `tank-dip-${Date.now()}.jpg`,
    stationId: 1,
    recordId: readingId,
    moduleName: "tank_readings",
    evidenceType: "TANK_DIP_PHOTO",
    description: "Tank dip reading photo",
  });

  console.log("Evidence result:", result);
}
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
<div
  style={{
    background: "#F8FAFC",
    padding: "12px",
    borderRadius: "10px",
    marginBottom: "16px",
  }}
>
  <h3>Today's Overview</h3>

  <p>
    Total Readings: <strong>{readings.length}</strong>
  </p>

  <p>
    Total Variance:{" "}
    <strong>
      {litres(
        readings.reduce(
          (total, item) => total + Number(item.variance || 0),
          0
        )
      )} L
    </strong>
  </p>

  <p>
    Pending Review:{" "}
    <strong>
      {
        readings.filter(
          (item) =>
            item.status?.toUpperCase() === "DRAFT"
        ).length
      }
    </strong>
  </p>
</div>
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
    marginTop: "16px",
    padding: "12px",
    background: "#F8FAFC",
    borderRadius: "10px",
  }}
>
  <h4>Workflow</h4>

  <p>
    {reading.status?.toUpperCase() === "DRAFT"
      ? "⚪ Draft"
      : "✅ Draft Completed"}
  </p>

  <p>
    Submitted:{" "}
    {reading.submitted_at
      ? new Date(reading.submitted_at).toLocaleString()
      : "Pending"}
  </p>

  <p>
    Verified:{" "}
    {reading.verified_at
      ? new Date(reading.verified_at).toLocaleString()
      : "Pending"}
  </p>

  <p>
    Approved:{" "}
    {reading.approved_at
      ? new Date(reading.approved_at).toLocaleString()
      : "Pending"}
  </p>
</div>
              <div
  style={{
    background: "#F1F5F9",
    padding: "12px",
    borderRadius: "8px",
    marginTop: "12px",
  }}
>
  <h4>📷 Evidence Center</h4>

  <CameraCapture
  onCapture={(image) => {
    uploadEvidence(image, reading.id);
  }}
/>

{evidenceImage && (
  <p>✅ Evidence photo attached</p>
)}

  <p>Photo • Video • Verification</p>
</div>
    



            </div>
          );
        })
      )}
    </div>
  );
}

export default TankReadings;
