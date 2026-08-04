import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function BusinessDay() {
  const [businessDay, setBusinessDay] = useState(null);
  const [stationId, setStationId] = useState("");
  const [loading, setLoading] = useState(false);
  const today = new Date().toISOString().slice(0, 10);

  async function loadBusinessDay() {
    if (!stationId) return;

    const { data } = await supabase
      .from("business_days")
      .select("*")
      .eq("station_id", stationId)
      .eq("status", "OPEN")
      .maybeSingle();

    setBusinessDay(data);
  }

  async function openBusinessDay() {
    if (!stationId) {
      alert("Select Station");
      return;
    }

    setLoading(true);

    const { error } = await supabase.from("business_days").insert({
      station_id: stationId,
      business_date: today,
      status: "OPEN",
    });

    setLoading(false);

    if (error) {
      alert(error.message);
      return;
    }

    loadBusinessDay();
  }

  async function closeBusinessDay() {
    if (!businessDay) return;

    setLoading(true);

    const { error } = await supabase
      .from("business_days")
      .update({
        status: "CLOSED",
        closed_at: new Date().toISOString(),
      })
      .eq("id", businessDay.id);

    setLoading(false);

    if (error) {
      alert(error.message);
      return;
    }

    setBusinessDay(null);
  }

  useEffect(() => {
    loadBusinessDay();
  }, [stationId]);

  return (
    <div className="page">
      <h2>Business Day</h2>

      <input
        type="number"
        placeholder="Station ID"
        value={stationId}
        onChange={(e) => setStationId(e.target.value)}
      />

      <p>Date: {today}</p>

      <p>
        Status: {businessDay ? "🟢 OPEN" : "🔴 CLOSED"}
      </p>

      {!businessDay ? (
        <button onClick={openBusinessDay} disabled={loading}>
          Open Business Day
        </button>
      ) : (
        <button onClick={closeBusinessDay} disabled={loading}>
          Close Business Day
        </button>
      )}
    </div>
  );
}
