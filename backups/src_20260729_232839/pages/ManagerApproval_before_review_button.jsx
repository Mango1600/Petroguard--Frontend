import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ManagerApproval({ staff }) {
  const [records, setRecords] = useState([]);

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

            <button onClick={() => approve(r.id)}>
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