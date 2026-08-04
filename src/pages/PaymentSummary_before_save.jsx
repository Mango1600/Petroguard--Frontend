import { useState } from "react";

export default function PaymentSummary({ staff }) {
  const [form, setForm] = useState({
    cash_sales: "",
    pos_sales: "",
    transfer_sales: "",
    credit_sales: "",
    other_income: "",
    other_expenses: ""
  });

  return (
    <div>
      <h2>💰 Payment Summary</h2>

      <p>Station ID: {staff?.station_id}</p>

      <label>Cash Sales</label><br />
      <input type="number" /><br /><br />

      <label>POS Sales</label><br />
      <input type="number" /><br /><br />

      <label>Bank Transfer</label><br />
      <input type="number" /><br /><br />

      <label>Credit Sales</label><br />
      <input type="number" /><br /><br />

      <label>Other Income</label><br />
      <input type="number" /><br /><br />

      <label>Other Expenses</label><br />
      <input type="number" /><br /><br />

      <button>Save Draft</button>
      <button style={{ marginLeft: "10px" }}>Submit</button>
    </div>
  );
}