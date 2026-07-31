import { useState } from "react";

export default function BusinessDayClose({ staff }) {
  const [message, setMessage] = useState("");

  function handleCloseDay() {
    setMessage("Business Day Close validation will be implemented in the next step.");
  }

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
