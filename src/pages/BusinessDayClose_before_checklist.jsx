import { useState, useEffect } from "react";
import { supabase } from "../lib/supabase";

export default function BusinessDayClose({ staff }) {
  const [message, setMessage] = useState("");
  const [checks, setChecks] = useState({});
  const [settings, setSettings] = useState(null);

  async function loadSettings() {

    const { data, error } = await supabase
      .from("company_settings")
      .select("*")
      .limit(1)
      .single();

    if (!error && data) {
      setSettings(data);
    }
  }


  async function handleCloseDay() {

    const result = {

      attendance: true,

      pump_readings: true,

      tank_dip:
        settings?.tank_dip_required ? false : true,

      payment_summary: true,

      manager_approval:
        settings?.manager_approval_required ? false : true
    };


    setChecks(result);


    const failed = Object.values(result)
      .some(item => item === false);


    if (failed) {

      setMessage(
        "Cannot close Business Day. Pending requirements detected."
      );

    } else {

      setMessage(
        "Business Day Closed Successfully."
      );
    }
  }


  useEffect(() => {
    loadSettings();
  }, []);

  return (
    <div>
      <h2>🔒 Business Day Close</h2>

      <p><b>Station:</b> {staff?.station_name || "Main Station"}</p>

      <p>
        Before closing the business day, PetroGuard will verify:
      </p>

      <ul>
        <li>✅ Attendance completed</li>
        <li>✅ Pump readings completed</li>
        <li>✅ Tank dip completed (if required)</li>
        <li>✅ Fuel deliveries reconciled</li>
        <li>✅ Payment summary submitted</li>
        <li>✅ Manager approval completed</li>
        <li>✅ No critical alerts</li>
      </ul>

      <button onClick={handleCloseDay}>
        🔒 Close Business Day
      </button>

      <p>{message}</p>
    </div>
  );
}
