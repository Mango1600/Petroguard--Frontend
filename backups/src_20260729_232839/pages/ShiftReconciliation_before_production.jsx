import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function FuelSales() {
  const [receipts, setReceipts] = useState([]);
  const [stationId, setStationId] = useState("");
  const [cash, setCash] = useState("");
  const [pos, setPos] = useState("");
  const [transfer, setTransfer] = useState("");
  const [credit, setCredit] = useState("");
  const [expenses, setExpenses] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    loadReceipts();
  }, []);

  async function loadReceipts() {
    const { data } = await supabase
      .from("daily_receipts")
      .select("*")
      .order("created_at", { ascending: false });

    setReceipts(data || []);
  }

  async function saveReceipt() {
    if (!stationId) {
      alert("Select station");
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
      alert(error.message);
      return;
    }

    alert("Daily receipt saved");

    setCash("");
    setPos("");
    setTransfer("");
    setCredit("");
    setExpenses("");

    loadReceipts();
  }

  return (
    <div style={{ padding:20 }}>
      <h2>💰 Daily Receipts / Cash Declaration</h2>

      <input
        placeholder="Station ID"
        value={stationId}
        onChange={(e)=>setStationId(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Cash at Hand"
        value={cash}
        onChange={(e)=>setCash(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="POS Sales"
        value={pos}
        onChange={(e)=>setPos(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Bank Transfer"
        value={transfer}
        onChange={(e)=>setTransfer(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Credit Sales"
        value={credit}
        onChange={(e)=>setCredit(e.target.value)}
      />

      <br />

      <input
        type="number"
        placeholder="Expenses"
        value={expenses}
        onChange={(e)=>setExpenses(e.target.value)}
      />

      <br /><br />

      <button onClick={saveReceipt}>
        Save Declaration
      </button>

      <h3>Previous Declarations</h3>

      {receipts.map((r)=>(
        <div key={r.id}>
          Cash: {r.cash} | POS: {r.pos} | Transfer: {r.bank_transfer}
        </div>
      ))}
    </div>
  );
}
