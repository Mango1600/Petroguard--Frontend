import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

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
      .select("*")
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
