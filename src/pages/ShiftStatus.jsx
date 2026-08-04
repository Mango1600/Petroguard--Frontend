import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ShiftStatus({
  staff,
  onOpenShift,
  onContinueShift,
  onHandover
}) {
  const [shift, setShift] = useState(null);
  const [openedBy, setOpenedBy] = useState(null);

  if (!staff) {
    return (
      <div style={{padding:20}}>
        <h2>Loading...</h2>
        <p>Waiting for staff information...</p>
      </div>
    );
  }

  useEffect(() => {
    loadShift();
  }, []);

  async function loadShift() {
    const { data } = await supabase
      .from("staff_shifts")
      .select("*")
      .eq("station_id", staff.station_id)
      .eq("status", "open")
      .maybeSingle();

    if (!data) {
      setShift(null);
      return;
    }

    setShift(data);

    const { data: staffData } = await supabase
      .from("staff")
      .select("name")
      .eq("id", data.staff_id)
      .maybeSingle();

    setOpenedBy(staffData);
  }

  if (!shift) {
    return (
      <div style={{padding:20}}>
        <h2>⛽ SHIFT STATUS</h2>

        <p><b>Station:</b> {staff.station_id}</p>

        <p>🟢 No Active Shift</p>

        <button onClick={onOpenShift}>
          Open New Shift
        </button>
      </div>
    );
  }

  const mine = shift.staff_id === staff.id;

  return (
    <div style={{padding:20}}>
      <h2>⛽ SHIFT STATUS</h2>

      <p><b>Station:</b> {staff.station_id}</p>
      <p><b>Shift No:</b> {shift.id}</p>
      <p><b>Opened By:</b> {openedBy?.name}</p>
      <p><b>Current Attendant:</b> {staff.name}</p>

      {mine ? (
        <button onClick={onContinueShift}>
          ▶ Continue Shift
        </button>
      ) : (
        <button onClick={onHandover}>
          🔄 Handover & Continue
        </button>
      )}
    </div>
  );
}