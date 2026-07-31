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
import AlertsManagement from "./AlertsManagement";
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
const [showAlertsManagement, setShowAlertsManagement] = useState(false);

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
      <h1>⛽ PetroGuard Enterprise</h1>

<h3>Enterprise Fuel Station Operating System</h3>

<hr />

<h3>📈 Business Day Progress</h3>

<table border="1" cellPadding="6">
<tr><td>🟢 Login</td><td>Completed</td></tr>
<tr><td>⛽ Pump Reading</td><td>In Progress</td></tr>
<tr><td>🛢 Tank Dip</td><td>Pending</td></tr>
<tr><td>💰 Fuel Sales</td><td>Pending</td></tr>
<tr><td>📊 Reconciliation</td><td>Pending</td></tr>
</table>

<hr />

<h3>📋 Today's Operations</h3>

<p>🟢 Station Status: Open</p>
<p>👥 Staff on Duty: {staff?.name}</p>
<p>📅 Business Date: {new Date().toLocaleDateString()}</p>

<hr />

<h2>Welcome, {staff?.name} 👋</h2>

<p><strong>Role:</strong> {staff?.role}</p>

<p><strong>Station:</strong> {station?.name || "-"}</p>

<p><strong>Status:</strong> 🟢 Station Open</p>


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
<button onClick={() => setShowAlertsManagement(!showAlertsManagement)}>
  {showAlertsManagement
    ? "Hide Alerts & Fraud Monitoring"
    : "Open Alerts & Fraud Monitoring"}
</button>

      <hr />
      {showAlertsManagement && <AlertsManagement />}
      {showInventoryManagement && <InventoryManagement />}
      {showFuelDeliveryManagement && <FuelDeliveryManagement />}
      {showFuelPriceManagement && <FuelPriceManagement />}
      {showTankManagement && <TankManagement />}
      {showPumpManagement && <PumpManagement />}
      {showStationManagement && <StationManagement />}
      {showStaffManagement && <StaffManagement />}
      {showManagerDashboard && <ManagerDashboard />}
      {showDailyReconciliation && <DailyReconciliation />}
      {showFuelSales && <FuelSales />}
      {showPumpReadings && <PumpReadings />}
      {showTankReadings && <TankReadings />}









    </div>
  );
}
