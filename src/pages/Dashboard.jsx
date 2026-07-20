import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

import TankReadings from "./TankReadings";
import PumpReadings from "./PumpReadings";
import FuelSales from "./FuelSales";
import DailyReconciliation from "./DailyReconciliation";
import ManagerDashboard from "./ManagerDashboard";
import StaffManagement from "./StaffManagement";
import StationManagement from "./StationManagement";
import PumpManagement from "./PumpManagement";
import TankManagement from "./TankManagement";
import FuelPriceManagement from "./FuelPriceManagement";
import FuelDeliveryManagement from "./FuelDeliveryManagement";
import InventoryManagement from "./InventoryManagement";
export default function Dashboard({ staff }) {
  const [station, setStation] = useState(null);

  const [showTankReadings, setShowTankReadings] = useState(false);
  const [showPumpReadings, setShowPumpReadings] = useState(false);
  const [showFuelSales, setShowFuelSales] = useState(false);
  const [showDailyReconciliation, setShowDailyReconciliation] = useState(false);
  const [showManagerDashboard, setShowManagerDashboard] = useState(false);
  const [showStaffManagement, setShowStaffManagement] = useState(false);
  const [showStationManagement, setShowStationManagement] = useState(false);
  const [showPumpManagement, setShowPumpManagement] = useState(false);
const [showTankManagement, setShowTankManagement] = useState(false);
const [showFuelPriceManagement, setShowFuelPriceManagement] = useState(false);
const [showFuelDeliveryManagement, setShowFuelDeliveryManagement] = useState(false);
const [showInventoryManagement, setShowInventoryManagement] = useState(false);
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
        Station: <b>{station?.name || "-"}</b>
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

      <button onClick={() => setShowDailyReconciliation(!showDailyReconciliation)}>
        {showDailyReconciliation
          ? "Hide Daily Reconciliation"
          : "Open Daily Reconciliation"}
      </button>

      <button onClick={() => setShowManagerDashboard(!showManagerDashboard)}>
        {showManagerDashboard
          ? "Hide Manager Dashboard"
          : "Open Manager Dashboard"}
      </button>

      <button onClick={() => setShowStaffManagement(!showStaffManagement)}>
        {showStaffManagement
          ? "Hide Staff Management"
          : "Open Staff Management"}
      </button>

      <button onClick={() => setShowStationManagement(!showStationManagement)}>
        {showStationManagement
          ? "Hide Station Management"
          : "Open Station Management"}
      </button>

      <button onClick={() => setShowPumpManagement(!showPumpManagement)}>
        {showPumpManagement
          ? "Hide Pump Management"
          : "Open Pump Management"}
      </button>
<button onClick={() => setShowTankManagement(!showTankManagement)}>
  {showTankManagement
    ? "Hide Tank Management"
    : "Open Tank Management"}
</button>
<button onClick={() => setShowFuelPriceManagement(!showFuelPriceManagement)}>
  {showFuelPriceManagement
    ? "Hide Fuel Price Management"
    : "Open Fuel Price Management"}
</button>
<button onClick={() => setShowFuelDeliveryManagement(!showFuelDeliveryManagement)}>
  {showFuelDeliveryManagement
    ? "Hide Fuel Delivery Management"
    : "Open Fuel Delivery Management"}
</button>
<button onClick={() => setShowInventoryManagement(!showInventoryManagement)}>
  {showInventoryManagement
    ? "Hide Inventory Management"
    : "Open Inventory Management"}
</button>

      <hr />

      {showTankReadings && <TankReadings />}

      {showPumpReadings && <PumpReadings />}
{showTankManagement && <TankManagement />}
{showFuelPriceManagement && <FuelPriceManagement />}
{showFuelDeliveryManagement && <FuelDeliveryManagement />}
{showInventoryManagement && <InventoryManagement />}

      {showFuelSales && <FuelSales />}

      {showDailyReconciliation && <DailyReconciliation />}

      {showManagerDashboard && <ManagerDashboard />}

      {showStaffManagement && <StaffManagement />}

      {showStationManagement && <StationManagement />}

      {showPumpManagement && <PumpManagement />}

    </div>
  );
}
