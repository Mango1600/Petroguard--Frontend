import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ManagerActivity() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    loadActivities();
  }, []);

  async function loadActivities() {
    const { data, error } = await supabase
      .from("pump_readings")
      .select(`
        id,
        opening_meter,
        closing_meter,
        variance,
        status,
        reading_date,
        staff (
          name,
          role
        ),
        pumps (
          pump_name,
          product_type
        )
      `)
      .order("reading_date", { ascending: false });

    if (error) {
      console.error("ManagerActivity Error:", error);
      alert(error.message);
      return;
    }

    setActivities(data || []);
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
