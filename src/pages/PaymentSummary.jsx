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
      const today = new Date().toISOString().split("T")[0];

      const totalCollected =
        cleanNumber(form.cash_sales) +
        cleanNumber(form.pos_sales) +
        cleanNumber(form.transfer_sales) +
        cleanNumber(form.credit_sales) +
        cleanNumber(form.other_income) -
        cleanNumber(form.other_expenses);

      console.log("STAFF:", staff);

      const payload = {
        station_id: staff.station_id,
        staff_id: staff?.id ?? null,
        reconciliation_date: today,

        cash_sales: cleanNumber(form.cash_sales),
        pos_sales: cleanNumber(form.pos_sales),
        transfer_sales: cleanNumber(form.transfer_sales),
        credit_sales_amount: cleanNumber(form.credit_sales),

        expected_revenue: totalCollected,
        revenue_variance: 0,
        status: status === "draft" ? "Draft" : "Submitted"
      };

      const { data: existing, error: findError } = await supabase
        .from("daily_reconciliation")
        .select("id")
        .eq("station_id", staff.station_id)
        .eq("reconciliation_date", today)
        .maybeSingle();

      if (findError) throw findError;

      let result;

      if (existing) {
        result = await supabase
          .from("daily_reconciliation")
          .update(payload)
          .eq("id", existing.id);
      } else {
        result = await supabase
          .from("daily_reconciliation")
          .insert(payload);
      }

      if (result.error) throw result.error;

      if (status === "submitted") {
      setMessage("Payment submitted successfully.");
    } else {
      setMessage("Payment saved successfully.");
    }
    } catch (err) {
      console.error(err);
      setMessage(
`SAVE ERROR:
${err.message}

CODE: ${err.code || ""}
DETAILS: ${err.details || ""}
HINT: ${err.hint || ""}`
);
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
