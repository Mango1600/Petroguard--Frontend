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

  const cleanNumber = (value) =>
    Number(String(value).replace(/₦|,/g, "").trim()) || 0;

  async function savePayment(status) {
    try {

    const totalCollected =
      cleanNumber(form.cash_sales) +
      cleanNumber(form.pos_sales) +
      cleanNumber(form.transfer_sales) +
      cleanNumber(form.credit_sales) +
      cleanNumber(form.other_income) -
      cleanNumber(form.other_expenses);

    const { error } = await supabase
      .from("pump_readings")
      .insert({
        station_id: staff.station_id,
        cash_sales: cleanNumber(form.cash_sales),
        pos_sales: cleanNumber(form.pos_sales),
        transfer_sales: cleanNumber(form.transfer_sales),
        credit_sales: cleanNumber(form.credit_sales),
        other_income: cleanNumber(form.other_income),
        other_expenses: cleanNumber(form.other_expenses),
        total_collected: totalCollected,
        status: status
      });

    if (error) {
      console.log(error);
      setMessage("SAVE ERROR: " + error.message);
    } else {
      setMessage("Payment saved successfully");
    }
    } catch (err) {
      console.log(err);
      setMessage("EXCEPTION: " + err.message);
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