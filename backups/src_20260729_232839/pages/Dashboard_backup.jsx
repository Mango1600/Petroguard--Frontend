import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import TankReadings from "./TankReadings";
import PumpReadings from "./PumpReadings";
import FuelSales from "./FuelSales";
import DailyReconciliation from "./DailyReconciliation";
function Dashboard() {
  const [stations, setStations] = useState([]);
  const [showTankReadings, setShowTankReadings] = useState(false);
  const [showPumpReadings, setShowPumpReadings] = useState(false);
const [showFuelSales, setShowFuelSales] = useState(false);
const [showDailyReconciliation, setShowDailyReconciliation] = useState(false);
  useEffect(() => {
    loadStations();
  }, []);

  async function loadStations() {
    const { data, error } = await supabase
      .from("stations")
      .select("*")
      .order("id");

    if (error) {
      alert(error.message);
      console.error(error);
      return;
    }

    setStations(data || []);
  }

  return (
    <div>
      <h1>PetroGuard Dashboard</h1>

      <div style={{ marginBottom: "20px" }}>
        <button onClick={() => setShowTankReadings(!showTankReadings)}>
          {showTankReadings ? "Hide Tank Readings" : "Open Tank Readings"}
        </button>

        <button
          onClick={() => setShowPumpReadings(!showPumpReadings)}
          style={{ marginLeft: "10px" }}
        >
          {showPumpReadings ? "Hide Pump Readings" : "Open Pump Readings"}
        </button><button
  onClick={() => setShowDailyReconciliation(!showDailyReconciliation)}
  style={{ marginLeft: "10px" }}
>
  {showDailyReconciliation
    ? "Hide Daily Reconciliation"
    : "Open Daily Reconciliation"}
</button>
      </div>

      {showTankReadings && <TankReadings />}

      {showPumpReadings && <PumpReadings />}
{showDailyReconciliation && <DailyReconciliation />}
      <h2>Total Stations</h2>
      <h3>{stations.length}</h3>

      <h2>Stations</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Location</th>
          </tr>
        </thead>

        <tbody>
          {stations.map((station) => (
            <tr key={station.id}>
              <td>{station.id}</td>
              <td>{station.name}</td>
              <td>{station.location || "-"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
