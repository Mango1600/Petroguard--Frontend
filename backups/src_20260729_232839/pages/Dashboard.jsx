import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import OCCPanel from "./OCCPanel";
import { getOCC } from "../lib/occApi";
import TankReadings from "./TankReadings";
import PumpReadings from "./PumpReadings";
import ShiftReconciliation from "./ShiftReconciliation";
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
import BusinessDayManagement from "./BusinessDayManagement";
import PaymentSummary from "./PaymentSummary";
import ManagerApproval from "./ManagerApproval";
import BusinessDayClose from "./BusinessDayClose";
import CompanySettings from "./CompanySettings";
export default function Dashboard({ staff }) {
  const [station, setStation] = useState(null);
  const [policy, setPolicy] = useState(null);
  const [modulePermissions, setModulePermissions] = useState([]);
  const [dashboardSummary, setDashboardSummary] = useState(null);
const [paymentSummary, setPaymentSummary] = useState(null);
const [operationStatus, setOperationStatus] = useState({
  pump: "Pending",
  tank: "Pending",
  payment: "Pending",
  reconciliation: "Pending"
});

  const [showTankReadings, setShowTankReadings] = useState(false);
  const [showPumpReadings, setShowPumpReadings] = useState(false);
  const [showShiftReconciliation, setShowShiftReconciliation] = useState(false);
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
const [showBusinessDayManagement, setShowBusinessDayManagement] = useState(false);
const [showPaymentSummary, setShowPaymentSummary] = useState(false);
const [showManagerApproval, setShowManagerApproval] = useState(false);
const [showBusinessDayClose, setShowBusinessDayClose] = useState(false);
const [showCompanySettings, setShowCompanySettings] = useState(false);




async function loadOperationStatus() {
  const pump = await supabase
    .from("pump_readings")
    .select("status")
    .limit(1);

  const tank = await supabase
    .from("tank_readings")
    .select("status")
    .limit(1);

  const recon = await supabase
    .from("daily_reconciliation")
    .select("status")
    .limit(1);

  setOperationStatus({
    pump: pump.data?.[0]?.status || "Pending",
    tank: tank.data?.[0]?.status || "Pending",
    payment: "Pending",
    reconciliation: recon.data?.[0]?.status || "Pending"
  });
}

async function loadDashboardSummary() {
  const { data, error } = await supabase
    .from("dashboard_summary")
    .select("*")
    .single();

  if (error) {
    console.log("Dashboard summary error:", error);
    return;
  }

  setDashboardSummary(data);
}

useEffect(() => {
  loadStation();
  loadStationPolicy();
  loadDashboardSummary();
  loadModulePermissions();
  loadOperationStatus();
}, []);


  async function loadStationPolicy() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("station_policies")
      .select("*")
      .eq("station_id", staff.station_id)
      .single();

    if (error) {
      console.error("Policy error:", error);
      return;
    }

    setPolicy(data);
  }

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


  async function loadModulePermissions() {
    if (!staff?.station_id) return;

    const { data, error } = await supabase
      .from("module_permissions")
      .select("*")
      .eq("station_id", staff.station_id);

    if (error) {
      console.error("Module permission error:", error);
      return;
    }

    setModulePermissions(data || []);
  }



  function canAccess(moduleName) {
    if (!staff) return false;

    if (staff.role.toLowerCase() == "developer") return true;

    const permission = modulePermissions.find(
      (m) => m.module_name === moduleName
    );

    if (!permission) return false;

    return permission.allowed_roles.includes(staff.role.toLowerCase());
  }

  return (
    <div>
      <h1>⛽ PetroGuard Enterprise</h1>

<h2>Operations Control Center (OCC)</h2>

<p>Enterprise Fuel Station Operating System</p>

<hr />

<h3>🟢 Business Day: OPEN</h3>

<p>📅 Monday, 27 July 2026</p>

<p>🏢 Company: ABC Petroleum Ltd.</p>


<h3>Enterprise Fuel Station Operating System</h3>

<hr />

<h3>📈 Business Day Progress</h3>

<table border="1" cellPadding="6">
<tr><td>🟢 Login</td><td>Completed</td></tr>
<tr><td>⛽ Pump Reading</td><td>{operationStatus.pump}</td></tr>
<tr><td>🛢 Tank Dip</td><td>{operationStatus.tank}</td></tr>
<tr><td>💰 Fuel Sales</td><td>Pending</td></tr>
<tr><td>📊 Reconciliation</td><td>{operationStatus.reconciliation}</td></tr>
</table>

<hr />


<hr />

<h3>📈 Today's KPIs</h3>

<p>
⛽ Litres Sold: {dashboardSummary?.total_liters_sold || 0} L
</p>

<p>
💰 Expected Revenue: ₦{Number(dashboardSummary?.total_revenue || 0).toLocaleString()}
</p>

<p>
📊 Transactions: {dashboardSummary?.total_transactions || 0}
</p>


<p>💵 Cash Received: ₦{Number(dashboardSummary?.cash_received || 0).toLocaleString()}</p>

<p>💳 POS Sales: ₦{Number(dashboardSummary?.pos_sales || 0).toLocaleString()}</p>

<p>🏦 Bank Transfers: ₦0.00</p>

<p>📒 Credit Sales: ₦{Number(dashboardSummary?.credit_sales || 0).toLocaleString()}</p>
<p>⚠ Variance: ₦0.00</p>

<h3>📋 Today's Operations</h3>

<p>🟢 Station Status: Open</p>
<p>👥 Staff on Duty: {staff?.name}</p>
<p>📅 Business Date: {new Date().toLocaleDateString()}</p>

<hr />

<h2>Welcome, {staff?.name} 👋</h2>

<p><strong>Role:</strong> {staff?.role}</p>

<p><strong>Station:</strong> {station?.name || "-"}</p>

<p><strong>Status:</strong> 🟢 Station Open</p>


      {canAccess("tank_dip") && (
      <button onClick={() => setShowTankReadings(!showTankReadings)}>
        {showTankReadings ? "Hide Tank Readings" : "Open Tank Readings"}
      </button>
      )}

      {canAccess("pump_reading") && (
      <button onClick={() => setShowPumpReadings(!showPumpReadings)}>
        {showPumpReadings ? "Hide Pump Readings" : "Open Pump Readings"}
      </button>
      )}

      <button onClick={() => setShowShiftReconciliation(!showShiftReconciliation)}>
        {showShiftReconciliation ? "Hide Shift Reconciliation" : "Open Shift Reconciliation"}
      </button>

      <button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>
        {showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>

      <button onClick={() => setShowManagerApproval(!showManagerApproval)}>
        {showManagerApproval
          ? "Hide Manager Approval"
          : "Open Manager Approval"}
      </button>

      <button onClick={() => setShowBusinessDayClose(!showBusinessDayClose)}>
        {showBusinessDayClose
          ? "Hide Business Day Close"
          : "Open Business Day Close"}
      </button>

      <button onClick={() => setShowCompanySettings(!showCompanySettings)}>
        {showCompanySettings
          ? "Hide Company Settings"
          : "Open Company Settings"}
      </button>

      {canAccess("reconciliation") && (
      <button onClick={() => setShowDailyReconciliation(!showDailyReconciliation)}>
        {showDailyReconciliation
          ? "Hide Daily Reconciliation"
          : "Open Daily Reconciliation"}
      </button>
      )}

      {canAccess("business_close") && (
        <button onClick={() => setShowBusinessDayManagement(!showBusinessDayManagement)}>
          {showBusinessDayManagement
            ? "Hide Business Day Management"
            : "Open Business Day Management"}
        </button>
      )}

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
      {showShiftReconciliation && (
        <ShiftReconciliation
          onBack={() => setShowShiftReconciliation(false)}
        />
      )}
      {showPaymentSummary && <PaymentSummary staff={staff} />}

      {showManagerApproval && (
        <ManagerApproval staff={staff} />
      )}

      {showBusinessDayClose && (
        <BusinessDayClose staff={staff} />
      )}

      {showCompanySettings && (
        <CompanySettings />
      )}
      {showPumpReadings && <PumpReadings />}
      {showTankReadings && <TankReadings />}

      {showBusinessDayManagement && (
        <BusinessDayManagement staff={staff} />
      )}










    

<hr />

<h3>🚨 Alerts</h3>

<p>✅ No Active Alerts</p>

<hr />

<h3>🖥 System Status</h3>

<p>🟢 Database Connected</p>
<p>🟢 User Authenticated</p>
<p>🟢 Station Operational</p>


</div>
  );
}