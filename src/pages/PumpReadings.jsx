import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function PumpReadings() {
  const [readings, setReadings] = useState([]);
  const [stations, setStations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    setLoading(true);

    const {
      data: { session },
    } = await supabase.auth.getSession();

    console.log("Session:", session);

    const [pumpResult, stationResult] = await Promise.all([
      supabase
        .from("pump_readings")
        .select("*")
        .order("id"),

      supabase
        .from("stations")
        .select("*")
        .order("id"),
    ]);

    console.log("Pump data:", pumpResult.data);
    console.log("Pump error:", pumpResult.error);

    if (pumpResult.error) {
      setErrorMessage(pumpResult.error.message);
      setLoading(false);
      return;
    }

    if (stationResult.error) {
      setErrorMessage(stationResult.error.message);
      setLoading(false);
      return;
    }

    setReadings(pumpResult.data || []);
    setStations(stationResult.data || []);
    setLoading(false);
  }

  function getStationName(stationId) {
    const station = stations.find((s) => s.id === stationId);
    return station ? station.name : `Station ${stationId}`;
  }

  if (loading) {
    return <p>Loading pump readings...</p>;
  }

  if (errorMessage) {
    return <p>Error: {errorMessage}</p>;
  }

  return (
    <div>
      <h2>Pump Readings</h2>

      {readings.length === 0 ? (
        <p>No pump readings found.</p>
      ) : (
        readings.map((reading) => (
          <div key={reading.id}>
            <p>ID: {reading.id}</p>
            <p>Station: {getStationName(reading.station_id)}</p>
            <p>Opening Meter: {reading.opening_meter}</p>
            <p>Closing Meter: {reading.closing_meter}</p>
            <p>Variance: {reading.variance}</p>
            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default PumpReadings;
