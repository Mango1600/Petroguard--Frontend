import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

import EvidenceViewer from "../components/EvidenceViewer";
import VerificationCard from "../components/VerificationCard";
import GPSLocation from "../components/GPSLocation";
import ReconciliationSummary from "../components/ReconciliationSummary";

function DailyReconciliation() {
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadReconciliation();
  }, []);

  async function loadReconciliation() {
    setLoading(true);

    const { data, error } = await supabase
      .from("daily_reconciliation")
      .select(`
        *,
        evidence(*)
      `)
      .order("reconciliation_date", { ascending: false });

    if (error) {
      alert(error.message);
      console.error(error);
      setLoading(false);
      return;
    }

    setRecords(data || []);
    setLoading(false);
  }

  if (loading) {
    return <p>Loading Daily Reconciliation...</p>;
  }

  return (
    <div>
      <h2>Daily Reconciliation</h2>

      <ReconciliationSummary records={records} />

      <h3>Evidence & Verification</h3>

      {records.map((row) => (
        <div
          key={row.id}
          style={{
            border: "1px solid #ccc",
            padding: "10px",
            marginBottom: "15px",
            borderRadius: "8px"
          }}
        >
          <h4>Record ID: {row.id}</h4>

          <EvidenceViewer reconciliationId={row.id} />

          <GPSLocation />

          <VerificationCard
            status={row.status || "Pending"}
            risk={row.risk_level || "Low"}
            manager={row.verified_by}
            owner={row.approved_by}
            comment={row.comment}
          />

          <hr />

          <p>
            Opening Meter Photo:{" "}
            {row.opening_meter_photo ? "Captured" : "Missing"}
          </p>

          <p>
            Closing Meter Photo:{" "}
            {row.closing_meter_photo ? "Captured" : "Missing"}
          </p>

          <p>
            Video Evidence:{" "}
            {row.video_evidence ? "Captured" : "Missing"}
          </p>
        </div>
      ))}

      {records.length === 0 ? (
        <p>No reconciliation records found.</p>
      ) : (
        <table border="1" cellPadding="6">
          <thead>
            <tr>
              <th>ID</th>
              <th>Date</th>
              <th>Fuel Sales</th>
              <th>Cash</th>
              <th>POS</th>
              <th>Credit</th>
              <th>Variance</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {records.map((row) => (
              <tr key={row.id}>
                <td>{row.id}</td>
                <td>{row.reconciliation_date}</td>
                <td>{row.fuel_sales}</td>
                <td>{row.cash_sales}</td>
                <td>{row.pos_sales}</td>
                <td>{row.credit_sales_amount}</td>
                <td>{row.variance}</td>
                <td>{row.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default DailyReconciliation;




















