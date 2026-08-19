import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function ShiftReconciliation({ onBack }) {
  const [receipts, setReceipts] = useState([]);
  const [stations, setStations] = useState([]);
  const [stationId, setStationId] = useState("");
  const [cash, setCash] = useState("");
  const [pos, setPos] = useState("");
  const [transfer, setTransfer] = useState("");
  const [credit, setCredit] = useState("");
  const [expenses, setExpenses] = useState("");
  const [loading, setLoading] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  useEffect(() => {
    loadReceipts();
    loadStations();
  }, []);

  async function loadStations() {
    const { data } = await supabase
      .from("stations")
      .select("id, name")
      .order("name");

    setStations(data || []);
  }

  
  async function submitShift() {
    if (!stationId) {
      return;
    }

    setLoading(true);

    const { error } = await supabase
      .from("staff_shifts")
      .update({
        status: "submitted",
        submitted_at: new Date().toISOString()
      })
      .eq("station_id", Number(stationId))
      .eq("status", "open");

    setLoading(false);

    if (error) {
      return;
    }

    setSubmitted(true);
  }

async function loadReceipts() {
    const { data } = await supabase
      .from("daily_receipts")
      .select("*")
      .order("created_at", { ascending: false });

    setReceipts(data || []);
  }

  async function saveReceipt() {
    if (!stationId) {
      return;
    }

    setLoading(true);
console.log({
  cash,
  pos,
  transfer,
  credit,
  expenses
});

    console.log({
      stationId,
      cash,
      pos,
      transfer,
      credit,
      expenses
    });

    const { error } = await supabase
      .from("daily_receipts")
      .insert([
        {
          station_id: Number(stationId),
          cash: Number(cash || 0),
          pos: Number(pos || 0),
          bank_transfer: Number(transfer || 0),
          credit: Number(credit || 0),
          expenses: Number(expenses || 0),
          created_at: new Date().toISOString()
        }
      ]);

    setLoading(false);

    if (error) {
      return;
    }


    setCash("");
    setPos("");
    setTransfer("");
    setCredit("");
    setExpenses("");

    loadReceipts();
  }

  return (
    <div style={{ padding:20 }}>
      <h2>💰 Shift Reconciliation</h2>

      {onBack && (
        <button onClick={onBack}>
          ⬅ Back to Dashboard
        </button>
      )}

      <h4>Attendant Shift Submission</h4>

      <select
        value={stationId}
        onChange={(e)=>setStationId(e.target.value)}
      >
        <option value="">Select Station</option>
        {stations.map((station) => (
          <option key={station.id} value={station.id}>
            {station.name}
          </option>
        ))}
      </select>

      <br />

      <input
        type="number"
        placeholder="Cash at Hand (₦)"
        value={cash}
        onChange={(e)=>setCash(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="POS Sales (₦)"
        value={pos}
        onChange={(e)=>setPos(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Bank Transfer (₦)"
        value={transfer}
        onChange={(e)=>setTransfer(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Credit Sales (₦)"
        value={credit}
        onChange={(e)=>setCredit(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Expenses (₦)"
        value={expenses}
        onChange={(e)=>setExpenses(e.target.value)}
      />

      <br /><br />

      <button onClick={saveReceipt}>
        ✅ Submit Shift
      </button>

      <h3>📋 Shift History</h3>

      {receipts.map((r)=>(
        <div key={r.id}>
          Cash: {r.cash} | POS: {r.pos} | Transfer: {r.bank_transfer} | Credit: {r.credit} | Expenses: {r.expenses}
        </div>
      ))}
    
      <br /><br />

      <button
        onClick={submitShift}
        disabled={loading || submitted}
        style={{width:"100%",padding:15}}
      >
        {submitted ? "✅ SHIFT SUBMITTED" : "📤 SUBMIT SHIFT"}
      </button>

</div>
  );
}