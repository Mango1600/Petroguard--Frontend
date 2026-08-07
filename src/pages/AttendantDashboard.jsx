import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import { handoverAssignment } from "../lib/pumpShiftAssignment";
import ResumeAssignment from "./ResumeAssignment";
import ShiftClose from "./ShiftClose";
import CashDeclaration from "./CashDeclaration";

export default function AttendantDashboard({ staff }) {
  const [assignment, setAssignment] = useState(null);
  const [closingMeter, setClosingMeter] = useState("");
  const [closingEvidence, setClosingEvidence] = useState("");
  const [evidenceVerified, setEvidenceVerified] = useState(false);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState("dashboard");

  useEffect(() => {
    loadPumpShift();
  }, []);

  async function loadPumpShift() {
    const { data: sessionData } = await supabase.auth.getSession();
    console.log("SUPABASE SESSION:", sessionData);

    console.log("Dashboard staff FULL:", JSON.stringify(staff, null, 2));

    if (!staff?.id) return;

    const { data, error } = await supabase
      .from("attendant_assignments")
      .select(`
        *,
        pump_shifts (
          *,
          pumps (
            station_id,
            pump_name,
            product_type
          ),
          business_days (
            business_date
          )
        )
      `)
      .eq("staff_id", staff.id)
      .eq("status", "ACTIVE")
      .maybeSingle();

    console.log("Dashboard staff FULL:", JSON.stringify(staff, null, 2));
    console.log("Active assignment query result:", data);
    console.log("Active assignment query error:", error);

    if (error) {
      console.log(error);
    }

    setAssignment(data);
    setLoading(false);
  }

  if (loading)
    return <div style={{padding:20}}>Loading Pump Shift...</div>;

  if (!assignment) {
    return (
      <ResumeAssignment
        loggedInStaff={staff}
        
        onResumeSuccess={loadPumpShift}
      />
    );
  }

  const shift = assignment.pump_shifts;






  async function handleHandover() {

    if (!evidenceVerified) {
      alert("Capture and verify closing evidence first.");
      return;
    }

    if (!closingMeter) {
      alert("Closing meter required.");
      return;
    }


    try {

      await handoverAssignment({

        assignmentId: assignment.id,

        pumpShiftId: assignment.pump_shift_id,

        currentClosingMeter: Number(closingMeter),

        closingEvidence,

        nextStaffId: assignment.staff_id

      });


      loadPumpShift();


    } catch(error) {

      console.log(error);

      alert(error.message);

    }

  }


  

if (page === "cash-declaration") {
  return (
    <CashDeclaration
      loggedInStaff={staff}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />
  );
}

if (page === "shift-close") {
  return (
    <ShiftClose
      loggedInStaff={staff}
      assignment={assignment}
      shift={shift}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />
  );
}

return (
    <div style={{padding:20}}>
      <h1>⛽ Pump Shift Dashboard</h1>

      <p>Attendant: {staff?.name}</p>

      <h2>
        Pump: {shift?.pumps?.pump_name}
      </h2>

      <p>
        Product: {shift?.pumps?.product_type}
      </p>

      <p>
        Business Day: {shift?.business_days?.business_date}
      </p>

      <p>
        Shift No: {shift?.shift_no}</p>

      <p>Status: {shift?.status}</p>

      <p>Opening Meter: {shift?.opening_meter}</p>

      <p>Assignment No: {assignment.assignment_no}</p>

      <CameraCapture
        title="Closing Evidence"
        stationId={staff?.station_id}
        uploadedBy={staff?.user_id}
        recordId={assignment?.pump_shift_id}
        moduleName="pump_shift"
        onCapture={(evidenceId) => {
          setClosingEvidence(evidenceId);
          setEvidenceVerified(true);
        }}
      />
      
<input
type="number"
placeholder="Closing Meter"
value={closingMeter}
onChange={(e)=>setClosingMeter(e.target.value)}
/>



<button onClick={handleHandover}>
Handover Pump
</button>

      <button
onClick={() => setPage("shift-close")}
>
Close Pump Shift
</button>
    </div>
  );
}