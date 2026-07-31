import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import ManagerActivity from "../components/ManagerActivity";

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
        email,
        status,
        staff_pumps (
          pump_id,
          pumps (
            pump_name,
            product_type
          )
        )
      `)
      .eq("role", "Attendant")
      .order("id");

    if (error) {
      console.error("Manager Dashboard Error:", error);
      alert(error.message);
      return;
    }

    setAttendants(data || []);
  }

  return (
    <div>
      <h1>Manager Dashboard</h1>

      <ManagerActivity />

      <hr />

      <h2>Attendant Pump Assignment</h2>

      {attendants.length === 0 ? (
        <p>No attendants found.</p>
      ) : (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>Attendant</th>
              <th>Role</th>
              <th>Assigned Pump</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {attendants.map((person) => (
              <tr key={person.id}>
                <td>{person.name}</td>

                <td>{person.role}</td>

                <td>
                  {person.staff_pumps?.length > 0 ? (
                    person.staff_pumps.map((item) => (
                      <div key={item.pump_id}>
                        {item.pumps?.pump_name || "Pump"}{" "}
                        ({item.pumps?.product_type || "-"})
                      </div>
                    ))
                  ) : (
                    "-"
                  )}
                </td>

                <td>
                  {person.status || "Active"}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
