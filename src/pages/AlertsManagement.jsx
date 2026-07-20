import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function AlertsManagement() {

  const [alerts, setAlerts] = useState([]);
  const [activities, setActivities] = useState([]);
  const [audits, setAudits] = useState([]);
  const [incidents, setIncidents] = useState([]);



  useEffect(() => {
    loadAlerts();
    loadActivities();
    loadAudits();
    loadIncidents();
  }, []);



  async function loadAlerts() {

    const { data, error } = await supabase
      .from("alerts")
      .select(`
        id,
        message,
        severity,
        created_at,
        stations(name)
      `)
      .order("created_at", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setAlerts(data || []);

  }



  async function loadActivities() {

    const { data, error } = await supabase
      .from("activity_log")
      .select("*")
      .order("created_at", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setActivities(data || []);

  }  async function loadAudits() {

    const { data, error } = await supabase
      .from("audit_logs")
      .select("*")
      .order("created_at", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setAudits(data || []);

  }



  async function loadIncidents() {

    const { data, error } = await supabase
      .from("incident_reports")
      .select(`
        id,
        incident_type,
        severity,
        description,
        resolved,
        incident_date,
        stations(name)
      `)
      .order("created_at", {
        ascending: false,
      });


    if (error) {
      console.error(error);
      return;
    }


    setIncidents(data || []);

  }



  return (
    <div>

      <h2>
        Alerts & Fraud Monitoring
      </h2>


      <button onClick={loadAlerts}>
        Refresh Alerts
      </button>


      <hr />


      <h3>
        Active Alerts
      </h3>


      {alerts.length === 0 ? (

        <p>
          No alerts found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>
              <th>Station</th>
              <th>Severity</th>
              <th>Message</th>
              <th>Date</th>
            </tr>

          </thead>


          <tbody>

            {alerts.map((alert) => (

              <tr key={alert.id}>

                <td>
                  {alert.stations?.name}
                </td>

                <td>
                  {alert.severity}
                </td>

                <td>
                  {alert.message}
                </td>

                <td>
                  {alert.created_at}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}


      <hr />


      <h3>
        Staff Activity Log
      </h3>


      {activities.length === 0 ? (

        <p>
          No activities found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>
              <th>Module</th>
              <th>Activity</th>
              <th>Status</th>
              <th>Date</th>
            </tr>

          </thead>


          <tbody>

            {activities.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.module_name}
                </td>

                <td>
                  {item.activity_type}
                </td>

                <td>
                  {item.status}
                </td>

                <td>
                  {item.created_at}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}      <hr />


      <h3>
        Audit Trail
      </h3>


      {audits.length === 0 ? (

        <p>
          No audit records found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>
              <th>Module</th>
              <th>Action</th>
              <th>Description</th>
              <th>Date</th>
            </tr>

          </thead>


          <tbody>

            {audits.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.module_name}
                </td>

                <td>
                  {item.action_type}
                </td>

                <td>
                  {item.description}
                </td>

                <td>
                  {item.created_at}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}



      <hr />


      <h3>
        Incident Reports
      </h3>


      {incidents.length === 0 ? (

        <p>
          No incidents found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>
              <th>Station</th>
              <th>Type</th>
              <th>Severity</th>
              <th>Status</th>
            </tr>

          </thead>


          <tbody>

            {incidents.map((item) => (

              <tr key={item.id}>

                <td>
                  {item.stations?.name}
                </td>

                <td>
                  {item.incident_type}
                </td>

                <td>
                  {item.severity}
                </td>

                <td>
                  {item.resolved
                    ? "Resolved"
                    : "Open"}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      )}


    </div>
  );

}
