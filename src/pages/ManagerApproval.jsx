import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ManagerApproval({ staff }) {
  const [records, setRecords] = useState([]);
  const [selectedRecord, setSelectedRecord] = useState(null);

  async function loadSubmitted() {
    const { data, error } = await supabase
      .from("daily_reconciliation")
      .select("*")
      .eq("status", "Submitted")
      .order("reconciliation_date", { ascending: false });

    if (error) {
      console.error(error);
      return;
    }

    setRecords(data || []);
  }

  async function approve(id) {
    const { error } = await supabase
      .from("daily_reconciliation")
      .update({
        status: "Approved",
        approved_by: staff.id,
        approved_at: new Date().toISOString(),
      })
      .eq("id", id);

    if (error) {
      alert(error.message);
      return;
    }

    loadSubmitted();
  }

  async function reject(id) {
    const reason = prompt("Reason for rejection:");

    if (!reason) return;

    const { error } = await supabase
      .from("daily_reconciliation")
      .update({
        status: "Rejected",
        rejected_by: staff.id,
        rejected_at: new Date().toISOString(),
        rejection_reason: reason,
      })
      .eq("id", id);

    if (error) {
      alert(error.message);
      return;
    }

    loadSubmitted();
  }

  useEffect(() => {
    loadSubmitted();
  }, []);

  return (
    <div>
      <h2>📋 Manager Approval Dashboard</h2>

      {selectedRecord && (
        <div
          style={{
            border: "2px solid #0a7",
            padding: "15px",
            marginBottom: "20px",
            borderRadius: "8px",
          }}
        >
          <h3>📋 Manager Review</h3>

          <p><b>Business Date:</b> {selectedRecord.reconciliation_date}</p>
          <p><b>Station ID:</b> {selectedRecord.station_id}</p>
          <p><b>Status:</b> {selectedRecord.status}</p>

          <hr />

          <p><b>Expected Revenue:</b> ₦{Number(selectedRecord.expected_revenue || 0).toLocaleString()}</p>

          <p><b>Actual Collection:</b> ₦{(
            Number(selectedRecord.cash_sales || 0) +
            Number(selectedRecord.pos_sales || 0) +
            Number(selectedRecord.transfer_sales || 0) +
            Number(selectedRecord.credit_sales_amount || 0)
          ).toLocaleString()}</p>

          <p><b>Variance:</b> ₦{Number(selectedRecord.revenue_variance || 0).toLocaleString()}</p>

          <button onClick={() => approve(selectedRecord.id)}>
            ✅ Approve
          </button>

          <button
            style={{marginLeft:"10px"}}
            onClick={() => reject(selectedRecord.id)}
          >
            ❌ Reject
          </button>

          <button
            style={{marginLeft:"10px"}}
            onClick={() => setSelectedRecord(null)}
          >
            Close
          </button>
        </div>
      )}


      {records.length === 0 ? (
        <p>✅ No submitted reconciliations.</p>
      ) : (
        records.map((r) => (
          <div
            key={r.id}
            style={{
              border: "1px solid #ccc",
              padding: "12px",
              marginBottom: "12px",
            }}
          >
            <p><b>Date:</b> {r.reconciliation_date}</p>
            <p><b>Station:</b> {r.station_id}</p>
            <p><b>Expected Revenue:</b> ₦{Number(r.expected_revenue || 0).toLocaleString()}</p>
            <p><b>Variance:</b> ₦{Number(r.revenue_variance || 0).toLocaleString()}</p>
            <p><b>Status:</b> {r.status}</p>

            <button onClick={() => setSelectedRecord(r)}>
              👁 Review
            </button>

            <button
              style={{ marginLeft: "10px" }}
              onClick={() => approve(r.id)}
            >
              ✅ Approve
            </button>

            <button
              style={{ marginLeft: "10px" }}
              onClick={() => reject(r.id)}
            >
              ❌ Reject
            </button>
          </div>
        ))
      )}
    </div>
  );
}
