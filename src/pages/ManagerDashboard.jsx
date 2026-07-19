import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ManagerDashboard() {
  const [attendants, setAttendants] = useState([]);

  useEffect(() => {
    loadAttendants();
  }, []);

  async function loadAttendants() {
    const { data, error } = await supabase
      .from("staff")
      .select(`
        id,
        name,
        role,
        station_id,
        staff_pumps (
  pump_id,
  pumps!staff_pumps_pump_id_fkey (
    pump_name,
    product_type
  )
)

      `)
      .eq("role", "Attendant");

    if (error) {
      alert(error.message);
      return;
    }

    setAttendants(data || []);
  }

  return (
    <div>
      <h1>Manager Dashboard</h1>

      <h2>Attendant Pump Assignment</h2>

      {attendants.length === 0 ? (
        <p>No attendants found</p>
      ) : (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>Attendant</th>
              <th>Pump</th>
              <th>Product</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {attendants.map((person) => (
              <tr key={person.id}>
                <td>{person.name}</td>

                <td>
                  {person.staff_pumps?.[0]?.pumps?.pump_name || person.staff_pumps?.[0]?.pump_name || "-"}
                </td>

                <td>
                  {person.staff_pumps?.[0]?.pumps?.product_type || person.staff_pumps?.[0]?.product_type || "-"}
                </td>

                <td>Active</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
