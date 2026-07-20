import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

import TankReadings from "./TankReadings";
import PumpReadings from "./PumpReadings";
import FuelSales from "./FuelSales";
import DailyReconciliation from "./DailyReconciliation";
import ManagerDashboard from "./ManagerDashboard";
import StaffManagement from "./StaffManagement";

export default function Dashboard({ staff }) {
  const [station, setStation] = useState(null);

  const [showTankReadings, setShowTankReadings] = useState(false);
  const [showPumpReadings, setShowPumpReadings] = useState(false);
  const [showFuelSales, setShowFuelSales] = useState(false);
  const [showDailyReconciliation, setShowDailyReconciliation] = useState(false);
  const [showManagerDashboard, setShowManagerDashboard] = useState(false);
  const [showStaffManagement, setShowStaffManagement] = useState(false);

  useEffect(() => {
    loadStation();
  }, []);

  async function loadStation() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("stations")
      .select("*")
      .eq("id", staff.station_id)
      .single();

    if (error) {
      console.error(error);
      return;
    }

    setStation(data);
  }

  return (
    <div>
      <h1>PetroGuard Command Centre</h1>

      <h2>Welcome, {staff?.name}</h2>

      <p>
        Role: <b>{staff?.role}</b>
      </p>

      <p>
        Email: <b>{staff?.email}</b>
      </p>

      <hr />

      <h3>Station</h3>

      <p>
        {station?.name || "Loading..."}
      </p>

      <p>
        {station?.location || "-"}
      </p>

      <hr />

      <button onClick={() => setShowTankReadings(!showTankReadings)}>
        {showTankReadings ? "Hide Tank Readings" : "Open Tank Readings"}
      </button>

      <button onClick={() => setShowPumpReadings(!showPumpReadings)}>
        {showPumpReadings ? "Hide Pump Readings" : "Open Pump Readings"}
      </button>

      <button onClick={() => setShowFuelSales(!showFuelSales)}>
        {showFuelSales ? "Hide Fuel Sales" : "Open Fuel Sales"}
      </button>

      <button
        onClick={() =>
          setShowDailyReconciliation(!showDailyReconciliation)
        }
      >
        {showDailyReconciliation
          ? "Hide Daily Reconciliation"
          : "Open Daily Reconciliation"}
      </button>

      <button
        onClick={() =>
          setShowManagerDashboard(!showManagerDashboard)
        }
      >
        {showManagerDashboard
          ? "Hide Manager Dashboard"
          : "Open Manager Dashboard"}
      </button>

      <button
        onClick={() =>
          setShowStaffManagement(!showStaffManagement)
        }
      >
        {showStaffManagement
          ? "Hide Staff Management"
          : "Open Staff Management"}
      </button>

      <hr />

      {showTankReadings && <TankReadings />}

      {showPumpReadings && <PumpReadings />}

      {showFuelSales && <FuelSales />}

      {showDailyReconciliation && <DailyReconciliation />}

      {showManagerDashboard && <ManagerDashboard />}

      {showStaffManagement && <StaffManagement />}

    </div>
  );
}


