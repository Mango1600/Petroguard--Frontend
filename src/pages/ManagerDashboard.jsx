import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import ManagerActivity from "../components/ManagerActivity";
import StaffRoster from "./StaffRoster";
import BusinessDayManagement from "./BusinessDayManagement";
import BusinessDayClose from "./BusinessDayClose";

export default function ManagerDashboard({ staff }) {
  const [attendants, setAttendants] = useState([]);

  useEffect(() => {
    loadAttendants();
  }, []);

  async function loadAttendants() {
    const { data, error } = await supabase
      .from("staff")
      .select("id,name,role,email,status")
      .eq("role","Attendant")
      .order("id");

    if (error) {
      console.error("Manager Dashboard Error:", error);
      return;
    }

    setAttendants(data || []);
  }

  const [showRoster, setShowRoster] = useState(false);

  return (
    <div>
      <h1>Manager Dashboard</h1>

      <BusinessDayManagement staff={staff} />
        <BusinessDayClose staff={staff} />

      <button
        onClick={() => setShowRoster(!showRoster)}
        style={{ marginBottom: 15 }}
      >
        {showRoster ? "Hide Staff Roster" : "Open Staff Roster"}
      </button>

      {showRoster && <StaffRoster staff={staff} />}

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