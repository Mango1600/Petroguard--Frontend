import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import CameraCapture from "../components/CameraCapture";
import VideoCapture from "../components/VideoCapture";
import { handoverAssignment } from "../lib/pumpShiftAssignment";
import ResumeAssignment from "./ResumeAssignment";
import OpenShift from "./OpenShift";
import ShiftClose from "./ShiftClose";
import CashDeclaration from "./CashDeclaration";

export default function AttendantDashboard({ staff }) {
  const [assignment, setAssignment] = useState(null);
  const [closedShift, setClosedShift] = useState(null);
  const [cashResult, setCashResult] = useState(null);
  const [reconResult, setReconResult] = useState(null);
  const [closingMeter, setClosingMeter] = useState("");
  const [closingEvidence, setClosingEvidence] = useState("");
  const [evidenceVerified, setEvidenceVerified] = useState(false);
  const [loading, setLoading] = useState(true);
  const [page, setPage] = useState("dashboard");

  useEffect(() => {
    loadPumpShift();
  }, []);

  async function loadClosedShift() {
    if (!staff?.id) return null;

    const { data: closed, error } = await supabase
      .from("pump_shifts")
      .select(`
        *,
        pumps (
          pump_name,
          product_type
        ),
        business_days (
          id,
          business_date
        )
      `)
      .eq("closed_by_staff_id", staff.id)
      .eq("status", "CLOSED")
      .order("closed_at", { ascending: false })
      .limit(1)
      .maybeSingle();

    if (error) {
      console.log("CLOSED SHIFT LOAD ERROR:", error);
      throw error;
    }

    setClosedShift(closed);

    if (closed?.id) {
      const { data: cash } = await supabase
        .from("cash_declarations")
        .select("*")
        .eq("pump_shift_id", closed.id)
        .order("declared_at", { ascending: false })
        .limit(1)
        .maybeSingle();

      setCashResult(cash);

      const { data: recon } = await supabase
        .from("daily_reconciliation")
        .select("*")
        .eq("shift_id", closed.id)
        .order("created_at", { ascending: false })
        .limit(1)
        .maybeSingle();

      setReconResult(recon);
    }

    return closed;
  }

  async function loadPumpShift() {
    const { data: sessionData } = await supabase.auth.getSession();
    // DEBUG REMOVED

    // DEBUG REMOVED

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
      .eq("pump_shifts.business_days.status", "OPEN")
      .order("id", { ascending: false })
      .limit(1)
      .maybeSingle();

    // DEBUG REMOVED
    // DEBUG REMOVED
    // DEBUG REMOVED

    if (error) {
      console.log(error);
    }

    setAssignment(data);

    if (!data) {
      const closed = await loadClosedShift();

      if (closed?.id) {
        const { data: existingCash, error: cashError } =
          await supabase
            .from("cash_declarations")
            .select("id")
            .eq("pump_shift_id", closed.id)
            .order("declared_at", { ascending: false })
            .limit(1)
            .maybeSingle();

        if (cashError) {
          console.log("CASH RECOVERY CHECK ERROR:", cashError);
        }

        if (!existingCash) {
          setPage("cash-declaration");
        }
      }
    }

    setLoading(false);
  }

  if (loading)
    return <div style={{padding:20}}>Loading Pump Shift...</div>;

  if (page === "cash-declaration") {
  if (!closedShift?.id) {
    return (
      <div style={{padding:20}}>
        <h2>Loading Closed Shift...</h2>
      </div>
    );
  }

  return (
    <CashDeclaration
      shiftData={{
        business_day_id: closedShift?.business_days?.id,
        pump_shift_id: closedShift?.id,
        attendant_assignment_id: closedShift?.assignment_id || null,
        user_id: staff?.user_id,
        staff_id: staff?.id
      }}
      onComplete={() => {
        setPage("dashboard");
      }}
    />
  );
}

if (!assignment) {
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={loadPumpShift}
      />
    );
  }

  if (!assignment) {
    return (
      <OpenShift
        staff={staff}
        onShiftOpened={loadPumpShift}
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


  


if (page === "shift-close") {
  return (
    <ShiftClose
      loggedInStaff={staff}
      assignment={assignment}
      shift={shift}
      onComplete={async () => {
        try {
          setPage("cash-declaration");
          await loadClosedShift();
        } catch (error) {
          console.log("CLOSED SHIFT LOAD ERROR:", error);
          alert("Shift closed, but closed shift data could not be loaded: " + error.message);
        }
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

      <VideoCapture
        stationId={staff?.station_id}
        uploadedBy={staff?.user_id}
        recordId={assignment?.pump_shift_id}
        moduleName="SHIFT_CLOSE"
        evidenceType="closing_shift_video"
        onComplete={(result) => {
          console.log("CLOSING VIDEO CAPTURED:", result);
          setClosingEvidence(result);
          setEvidenceVerified(true);
        }}
      />
      
<input
type="number"
placeholder="Closing Meter"
value={closingMeter}
onChange={(e)=>setClosingMeter(e.target.value)}
/>

<div style={{
  border:"1px solid #999",
  padding:"12px",
  marginTop:"15px",
  borderRadius:"8px"
}}>
<h3>📊 Shift Result Preview</h3>

<p>
Opening Meter: {shift?.opening_meter}
</p>

<p>
Closing Meter: {shift?.closing_meter}
</p>

<p>
Litres Sold: {
  shift?.closing_meter && shift?.opening_meter
    ? (Number(shift.closing_meter) - Number(shift.opening_meter)).toFixed(2)
    : "0"
} L
</p>

<p>
Price: ₦1,300
</p>

<p>
Expected Sales: ₦{
  shift?.closing_meter && shift?.opening_meter
    ? (
      (Number(shift.closing_meter) - Number(shift.opening_meter))
      * 1300
    ).toLocaleString()
    : "0"
}
</p>

</div>



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