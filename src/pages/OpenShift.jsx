import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import AttendantPumpReading from "./AttendantPumpReading";
import VideoCapture from "../components/VideoCapture";
import { getOpenBusinessDay } from "../lib/businessDay";
import { createPumpShift } from "../lib/pumpShift";
import { createAssignment, nextAssignmentNumber } from "../lib/pumpShiftAssignment";

export default function OpenShift({ staff, onShiftOpened }) {
  const [activeShift, setActiveShift] = useState(null);
  const [pumps, setPumps] = useState([]);
  const [pumpId, setPumpId] = useState("");
  const [openingMeter, setOpeningMeter] = useState("");
  const [showVideo, setShowVideo] = useState(false);
  const [showPumpReading, setShowPumpReading] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    if (staff?.id) {
      loadActiveShift();
      loadPumps();
    }
  }, [staff?.id]);

  async function loadActiveShift() {
    const { data } = await supabase
      .from("staff_shifts")
      .select("*")
      .eq("staff_id", staff.id)
      .eq("status", "open")
      .order("id", { ascending: false })
      .limit(1)
      .maybeSingle();

    setActiveShift(data);
  }

  async function loadPumps() {
    const { data } = await supabase
      .from("pumps")
      .select("id,pump_name,product_type")
      .eq("station_id", staff.station_id);

    setPumps(data || []);
  }

  async function createShift() {
    console.log("CREATE SHIFT STARTED", {
      staff: staff?.id,
      pumpId,
      openingMeter
    });


    try {

      const { data: businessDay, error: bdError } =
        await getOpenBusinessDay(staff.station_id);


      if (bdError) {
        throw bdError;
      }


      if (!businessDay) {
        throw new Error("No OPEN Business Day found.");
      }


      const pumpShift = await createPumpShift({

        businessDayId: businessDay.id,

        pumpId: Number(pumpId),

        openingMeter: Number(openingMeter),

        openingEvidence: null,

        staffId: staff.id

      });


      console.log('Creating assignment', pumpShift);

      console.log("BEFORE CREATE ASSIGNMENT", {
  pumpShiftId: pumpShift.id,
  staffId: staff.id
});

console.log("BEFORE CREATE ASSIGNMENT", {
  pumpShiftId: pumpShift.id,
  staffId: staff.id
});

await createAssignment({

        pumpShiftId: pumpShift.id,

        staffId: staff.id,

        assignmentNo: await nextAssignmentNumber(pumpShift.id),

        openingMeter: Number(openingMeter),

        openingEvidence: null,

        assignedBy: staff.id

      });


      setActiveShift(pumpShift);

      setMessage("✅ Pump Shift opened");


      if (onShiftOpened) {
        onShiftOpened();
      }


    } catch(error) {

      console.log(error);

      setMessage(error.message);

    }

  }


  if (showVideo) {
    console.log("OpenShift state", {showVideo, activeShift, showPumpReading});

  return (
      <VideoCapture
        shiftId={activeShift?.id}
        stationId={staff.station_id}
        staffId={staff.id}
        evidenceType="opening_shift_video"
        onComplete={async () => {
          setShowVideo(false);
          await createShift();
        }}
      />
    );
  }

  if (showPumpReading) {
    return <AttendantPumpReading staff={staff} />;
  }

  return (
    <div style={{padding:20,maxWidth:500,margin:"auto"}}>
      <h2>🟢 OPEN SHIFT</h2>

      <p><b>Attendant:</b> {staff?.name}</p>
      <p><b>Station:</b> {staff?.station_id}</p>

      {activeShift ? (
        <>
          <p><b>Status:</b> 🟢 Shift Open</p>
          <p><b>Clock In:</b> {activeShift.clock_in}</p>

          <button
            style={{width:"100%",padding:15}}
            onClick={()=>setShowPumpReading(true)}
          >
            ▶ Continue Working
          </button>
        </>
      ) : (
        <>
          <p><b>Pump</b></p>

          <select
            value={pumpId}
            onChange={(e)=>setPumpId(e.target.value)}
            style={{width:"100%",padding:10}}
          >
            <option value="">Select Pump</option>
            {pumps.map((pump)=>(
              <option key={pump.id} value={pump.id}>
                {pump.pump_name} ({pump.product_type})
              </option>
            ))}
          </select>

          <br/><br/>

          <input
            type="number"
            placeholder="Opening Meter"
            value={openingMeter}
            onChange={(e)=>setOpeningMeter(e.target.value)}
            style={{width:"100%",padding:10}}
          />

          <br/><br/>

          <button
            style={{width:"100%",padding:15}}
            onClick={()=>{
              if (!pumpId) {
                setMessage("Select pump");
                return;
              }

              if (!openingMeter) {
                setMessage("Enter opening meter");
                return;
              }

              setShowVideo(true);
            }}
          >
            START SHIFT
          </button>
        </>
      )}

      <p>{message}</p>
    </div>
  );
}