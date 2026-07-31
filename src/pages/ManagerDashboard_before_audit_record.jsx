import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";
import ManagerActivity from "../components/ManagerActivity";

export default function ManagerDashboard() {
  const [attendants, setAttendants] = useState([]);

  
async function loadPendingShifts() {
  const { data } = await supabase
    .from("staff_shifts")
    .select("*")
    .eq("status","submitted")
    .order("submitted_at",{ascending:false});

  setPendingShifts(data || []);
}

async function approveShift(id) {
  const { error } = await supabase
    .from("staff_shifts")
    .update({
      status:"approved",
      approved_at:new Date().toISOString(),
      locked:true,
      locked_at:new Date().toISOString()
    })
    .eq("id",id);

  if(error){
    alert(error.message);
    return;
  }

  alert("✅ Shift Approved and Locked 🔒");
  loadPendingShifts();
}

useEffect(() => {
  loadPendingShifts();
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
    
<hr/>

<h2>Pending Shift Approval</h2>

{pendingShifts.map(shift => (
  <div
    key={shift.id}
    style={{
      border:"1px solid #ccc",
      padding:12,
      marginBottom:12,
      borderRadius:8
    }}
  >
    <p><b>Shift ID:</b> {shift.id}</p>
    <p><b>Staff:</b> {shift.staff_id}</p>
    <p><b>Station:</b> {shift.station_id}</p>

    <button
      onClick={() => approveShift(shift.id)}
      style={{padding:10}}
    >
      ✅ APPROVE SHIFT
    </button>
  </div>
))}

</div>
  );
}
