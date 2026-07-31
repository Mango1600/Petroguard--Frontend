import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function AttendantDashboard({ staff }) {
  const [assignment, setAssignment] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadPumpShift();
  }, []);

  async function loadPumpShift() {
    if (!staff?.id) return;

    const { data, error } = await supabase
      .from("attendant_assignments")
      .select(`
        id,
        assignment_no,
        status,
        pump_shift_id,
        assigned_at,
        handed_over_at,
        pump_shifts (
          id,
          shift_no,
          status,
          opening_meter,
          closing_meter,
          pumps (
            id,
            pump_name,
            product_type
          ),
          business_days (
            business_date,
            status
          )
        )
      `)
      .eq("staff_id", staff.id)
      .eq("status", "ACTIVE")
      .maybeSingle();

    if (error) {
      console.log(error);
    }

    setAssignment(data);
    setLoading(false);
  }

  if (loading)
    return <div style={{padding:20}}>Loading Pump Shift...</div>;

  if (!assignment)
    return (
      <div style={{padding:20}}>
        <h2>No Active Pump Assignment</h2>
      </div>
    );

  const shift = assignment.pump_shifts;

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

      <button>Record Sales</button>
      <button>Handover Pump</button>
      <button>Close Pump Shift</button>
    </div>
  );
}
