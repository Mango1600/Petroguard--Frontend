import { useState } from "react";

export default function ShiftSubmission() {
  const [form, setForm] = useState({
    cash: "",
    pos: "",
    transfer: "",
    credit: "",
    expenses: "",
    remarks: ""
  });

  const expectedRevenue = 0; // Load automatically from Pump Readings

  const totalDeclared =
    (Number(form.cash) || 0) +
    (Number(form.pos) || 0) +
    (Number(form.transfer) || 0) +
    (Number(form.credit) || 0);

  const variance =
    expectedRevenue - totalDeclared + (Number(form.expenses) || 0);

  return (
    <div style={{ padding: 20 }}>
      <h2>💰 Shift Submission</h2>

      <h3>Cash Declaration</h3>

      <input
        type="number"
        placeholder="Cash Received"
        value={form.cash}
        onChange={(e) =>
          setForm({ ...form, cash: e.target.value })
        }
      />

      <input
        type="number"
        placeholder="POS Sales"
        value={form.pos}
        onChange={(e) =>
          setForm({ ...form, pos: e.target.value })
        }
      />

      <input
        type="number"
        placeholder="Bank Transfers"
        value={form.transfer}
        onChange={(e) =>
          setForm({ ...form, transfer: e.target.value })
        }
      />

      <input
        type="number"
        placeholder="Credit Sales"
        value={form.credit}
        onChange={(e) =>
          setForm({ ...form, credit: e.target.value })
        }
      />

      <input
        type="number"
        placeholder="Expenses"
        value={form.expenses}
        onChange={(e) =>
          setForm({ ...form, expenses: e.target.value })
        }
      />

      <textarea
        placeholder="Remarks"
        value={form.remarks}
        onChange={(e) =>
          setForm({ ...form, remarks: e.target.value })
        }
      />

      <hr />

      <h3>Automatic Summary</h3>

      <p>Expected Revenue: ₦{expectedRevenue.toLocaleString()}</p>
      <p>Total Declared: ₦{totalDeclared.toLocaleString()}</p>
      <p>Expenses: ₦{(Number(form.expenses) || 0).toLocaleString()}</p>
      <p>
        <strong>
          Variance: ₦{variance.toLocaleString()}
        </strong>
      </p>

      <button>📷 Capture Evidence</button>

      <br /><br />

      <button>✅ Submit Shift</button>
    </div>
  );
}