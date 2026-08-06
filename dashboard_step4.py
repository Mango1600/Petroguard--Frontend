from pathlib import Path

Path("src/pages/Dashboard.jsx").write_text("""
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
import BusinessDayManagement from "./BusinessDayManagement";
import PaymentSummary from "./PaymentSummary";
import OperationsAnalysis from "./OperationsAnalysis";
import AttendantDashboard from "./AttendantDashboard";

export default function Dashboard({staff}) {

  return (
    <div style={{padding:"30px",color:"black",background:"white"}}>
      DASHBOARD STEP 4 IMPORTS + RENDER OK<br/>
      User: {staff?.name}
    </div>
  );
}
""")

print("Dashboard step 4 created")
