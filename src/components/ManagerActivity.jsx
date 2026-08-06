import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ManagerActivity() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    loadActivities();
  }, []);

  async function loadActivities() {

    const { data, error } = await supabase
      .from("pump_shifts")
      .select(`
        id,
        opening_meter,
        closing_meter,
        status,
        pump_id,
        opened_by_staff_id,
        pumps (
          pump_name,
          product_type
        )
      `)
      .order("id", { ascending: false });

    if (error) {
      console.error("ManagerActivity Error:", error);
      return;
    }

    const rows = await Promise.all(
      (data || []).map(async (shift) => {

        const { data: staff } = await supabase
          .from("staff")
          .select("name,role")
          .eq("id", shift.opened_by_staff_id)
          .single();

        return {
          ...shift,
          staff
        };
      })
    );

    setActivities(rows);
  }

  return (
    <div>
      <h2>Today's Activities</h2>

      {activities.length === 0 ? (
        <p>No activities found.</p>
      ) : (
        <table border="1" cellPadding="8">
          <thead>
            <tr>
              <th>Attendant</th>
              <th>Pump</th>
              <th>Opening</th>
              <th>Closing</th>
              <th>Variance</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {activities.map((item) => (
              <tr key={item.id}>
                <td>
                  {item.staff?.name || "Unknown"}
                </td>

                <td>
                  {item.pumps
                    ? `${item.pumps.pump_name} (${item.pumps.product_type})`
                    : "-"}
                </td>

                <td>{item.opening_meter}</td>

                <td>{item.closing_meter}</td>

                <td>{item.variance}</td>

                <td>{item.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}