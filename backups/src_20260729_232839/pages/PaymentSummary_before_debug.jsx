import { useState } from "react";
import { supabase } from "../lib/supabase";

export default function PaymentSummary({ staff }) {

  const [form, setForm] = useState({
    cash_sales: "",
    pos_sales: "",
    transfer_sales: "",
    credit_sales: "",
    other_income: "",
    other_expenses: ""
  });

  const [message, setMessage] = useState("");

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  }

  async function savePayment(status) {

    const totalCollected =
      Number(form.cash_sales || 0) +
      Number(form.pos_sales || 0) +
      Number(form.transfer_sales || 0) +
      Number(form.credit_sales || 0) +
      Number(form.other_income || 0) -
      Number(form.other_expenses || 0);

    const { error } = await supabase
      .from("pump_readings")
      .insert({
        station_id: staff.station_id,
        cash_sales: form.cash_sales,
        pos_sales: form.pos_sales,
        transfer_sales: form.transfer_sales,
        credit_sales: form.credit_sales,
        other_income: form.other_income,
        other_expenses: form.other_expenses,
        total_collected: totalCollected,
        status: status
      });

    if (error) {
      setMessage(error.message);
    } else {
      setMessage("Payment saved successfully");
    }
  }


  return (
    <div>
      <h2>💰 Payment Summary</h2>

      <p>Station ID: {staff?.station_id}</p>

      <label>Cash Sales</label><br />
      <input name="cash_sales" value={form.cash_sales} onChange={handleChange}/><br /><br />

      <label>POS Sales</label><br />
      <input name="pos_sales" value={form.pos_sales} onChange={handleChange}/><br /><br />

      <label>Bank Transfer</label><br />
      <input name="transfer_sales" value={form.transfer_sales} onChange={handleChange}/><br /><br />

      <label>Credit Sales</label><br />
      <input name="credit_sales" value={form.credit_sales} onChange={handleChange}/><br /><br />

      <label>Other Income</label><br />
      <input name="other_income" value={form.other_income} onChange={handleChange}/><br /><br />

      <label>Other Expenses</label><br />
      <input name="other_expenses" value={form.other_expenses} onChange={handleChange}/><br /><br />

      <button onClick={() => savePayment("draft")}>
        Save Draft
      </button>

      <button
        style={{ marginLeft:"10px" }}
        onClick={() => savePayment("submitted")}
      >
        Submit
      </button>

      <p>{message}</p>

    </div>
  );
}