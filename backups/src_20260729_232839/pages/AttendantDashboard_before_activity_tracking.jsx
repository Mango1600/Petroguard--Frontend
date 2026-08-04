import { useEffect, useState } from "react";
import PumpReadings from "./PumpReadings";
import { supabase } from "../lib/supabase";
import OpenShift from "./OpenShift";
import ShiftReconciliation from "./ShiftReconciliation";
import ShiftClose from "./ShiftClose";
import AttendantPumpReading from "./AttendantPumpReading";

export default function AttendantDashboard({ staff }) {
  const [page, setPage] = useState("home");

  useEffect(() => {
    checkActiveShift();
  }, []);

  async function checkActiveShift() {
    const { data } = await supabase
      .from("staff_shifts")
      .select("id,station_id,status")
      .eq("station_id", staff.station_id)
      .eq("status", "open")
      .maybeSingle();

    if (data) {
      setPage("attendantPump");
    } else {
      setPage("open");
    }
  }

  console.log("Current page:", page);

  if (page === "open")
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={() => setPage("attendantPump")}
      />
    );
  if (page === "pump") return <PumpReadings staff={staff} />;
  if (page === "attendantPump") return <AttendantPumpReading staff={staff} />;
  if (page === "reconciliation") return <ShiftReconciliation staff={staff} />;
  if (page === "close") return <ShiftClose staff={staff} />;

  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h2>⛽ PetroGuard</h2>
      <h3>Attendant Operations</h3>

      <p><b>Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_name || "Main Station"}</p>
      <p><b>Business Day:</b> 🟢 OPEN</p>

      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => { console.log("BUTTON CLICK");
          console.log("OPEN SHIFT clicked");
          setPage("open");
        }}
      >
        🟢 OPEN SHIFT
      </button>

      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => setPage("reconciliation")}
      >
        💰 SHIFT RECONCILIATION
      </button>

      <button
        style={{width:"100%",padding:15,marginTop:10}}
        onClick={() => setPage("close")}
      >
        🔴 CLOSE SHIFT
      </button>

    </div>
  );
}