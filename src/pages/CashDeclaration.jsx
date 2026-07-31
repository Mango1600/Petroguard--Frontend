import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function CashDeclaration({
  onBack,
  shift,
  openingMeter,
  closingMeter,
  litresSold,
  closingVideo
}) {
  const [receipts, setReceipts] = useState([]);
  const [stations, setStations] = useState([]);
  const [stationId, setStationId] = useState("");
  const [cash, setCash] = useState("");
  const [pos, setPos] = useState("");
  const [transfer, setTransfer] = useState("");
  const [credit, setCredit] = useState("");
  const [expenses, setExpenses] = useState("");
  const [loading, setLoading] = useState(false);

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

    const litres = Number(
      litresSold || 
      ((Number(closingMeter || 0) - Number(openingMeter || 0)))
    );

    const { data: pump } = await supabase
      .from("pump_readings")
      .select("product_type")
      .eq("pump_id", shift?.pump_id)
      .order("created_at", { ascending: false })
      .limit(1)
      .single();

    const { data: price } = await supabase
      .from("fuel_prices")
      .select("unit_price")
      .eq("product_type", pump?.product_type)
      .order("effective_date", { ascending: false })
      .limit(1)
      .single();

    const expectedRevenue =
      litres * Number(price?.unit_price || 0);

    const collected =
      Number(cash || 0) +
      Number(pos || 0) +
      Number(transfer || 0) +
      Number(credit || 0) -
      Number(expenses || 0);

    await supabase
      .from("daily_reconciliation")
      .insert([
        {
          station_id: Number(stationId),
          staff_id:
shift?.staff_id,
          shift_id:
shift?.staff_shift_id ??
shift?.shift_id ??
shift?.id,
          fuel_sales: litres,
          cash_sales: Number(cash || 0),
          pos_sales: Number(pos || 0),
          transfer_sales: Number(transfer || 0),
          credit_sales_amount: Number(credit || 0),
          expected_revenue: expectedRevenue,
          revenue_variance: collected - expectedRevenue,
          status: "Pending Manager Approval"
        }
      ]);

    alert("Daily receipt saved and reconciliation created");

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
    </div>
  );
}
