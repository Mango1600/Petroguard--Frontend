import { useState, useEffect } from "react";
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
  const [paymentStatus, setPaymentStatus] = useState("Draft");

  function handleChange(e) {
    setForm({
      ...form,
      [e.target.name]: e.target.value
    });
  }

  const cleanNumber = (value) =>
    Number(String(value).replace(/₦|,/g, "").trim()) || 0;

  
  const isLocked =
    paymentStatus === "Submitted" ||
    paymentStatus === "Approved";

  
  async function loadPaymentStatus() {
    const today = new Date().toISOString().split("T")[0];

    const { data, error } = await supabase
      .from("daily_reconciliation")
      .select("status")
      .eq("station_id", staff.station_id)
      .eq("reconciliation_date", today)
      .maybeSingle();

    if (!error && data) {
      setPaymentStatus(data.status || "Draft");
    }
  }

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
      setPaymentStatus("Submitted");
      setMessage("Payment submitted successfully.");
    } else {
      setPaymentStatus("Draft");
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


  useEffect(() => {
    loadPaymentStatus();
  }, []);

  
  const totalCollected =
    cleanNumber(form.cash_sales) +
    cleanNumber(form.pos_sales) +
    cleanNumber(form.transfer_sales) +
    cleanNumber(form.credit_sales) +
    cleanNumber(form.other_income) -
    cleanNumber(form.other_expenses);

  return (

    <div>
      <h2>💰 Payment Summary</h2>

      <div>
        <h3>📊 Sales Reconciliation Preview</h3>

        <p>
          Total Submitted:
          ₦{totalCollected.toLocaleString()}
        </p>

        <p>
          Expected Revenue:
          ₦{totalCollected.toLocaleString()}
        </p>

        <p>
          Variance:
          ₦0
        </p>

        <p>
          Status:
          🟢 Balanced
        </p>
      </div>

      <p>Station ID: {staff?.station_id}</p>

      <label>Cash Sales</label><br />
      <input name="cash_sales" value={form.cash_sales} onChange={handleChange} disabled={isLocked}/><br /><br />

      <label>POS Sales</label><br />
      <input name="pos_sales" value={form.pos_sales} onChange={handleChange} disabled={isLocked}/><br /><br />

      <label>Bank Transfer</label><br />
      <input name="transfer_sales" value={form.transfer_sales} onChange={handleChange} disabled={isLocked}/><br /><br />

      <label>Credit Sales</label><br />
      <input name="credit_sales" value={form.credit_sales} onChange={handleChange} disabled={isLocked}/><br /><br />

      <label>Other Income</label><br />
      <input name="other_income" value={form.other_income} onChange={handleChange} disabled={isLocked}/><br /><br />

      <label>Other Expenses</label><br />
      <input name="other_expenses" value={form.other_expenses} onChange={handleChange} disabled={isLocked}/><br /><br />

      {isLocked && (
        <p style={{color:"red",fontWeight:"bold"}}>
          🔒 This Payment Summary has been submitted.<br/>
          Awaiting Manager approval.
        </p>
      )}

      <button onClick={() => savePayment("draft")} disabled={isLocked}>
        Save Draft
      </button>

      <button
        style={{ marginLeft:"10px" }}
        onClick={() => savePayment("submitted")}
        disabled={isLocked}
      >
        Submit
      </button>

      <p>{message}</p>

    </div>
  );
}
