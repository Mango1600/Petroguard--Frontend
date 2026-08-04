import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function FuelSales({ salesContext }) {
  const [sales, setSales] = useState([]);
  const [stations, setStations] = useState([]);
  const [pumps, setPumps] = useState([]);
  const [loading, setLoading] = useState(true);

  const [stationId, setStationId] = useState("");
  const [pumpId, setPumpId] = useState("");
  const [openingMeter, setOpeningMeter] = useState("");
  const [closingMeter, setClosingMeter] = useState("");
  const [unitPrice, setUnitPrice] = useState("");
  const [paymentMethod, setPaymentMethod] = useState("Cash");
  const [activeShift, setActiveShift] = useState(null);
  const [activeAssignment, setActiveAssignment] = useState(null);

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    setLoading(true);

    const { data: salesData, error: salesError } = await supabase
      .from("fuel_sales")
      .select("*")
      .order("sale_date", { ascending: false });

    if (salesError) {
      console.error(salesError);
      setLoading(false);
      return;
    }

    const { data: stationData } = await supabase
      .from("stations")
      .select("*");

    const { data: pumpData } = await supabase
      .from("pumps")
      .select("*");

    setSales(salesData || []);
    setStations(stationData || []);
    setPumps(pumpData || []);
    setLoading(false);
  }

  function getStationName(id) {
    const station = stations.find((s) => s.id === id);
    return station ? station.name : "-";
  }

  function getPumpName(id) {
    const pump = pumps.find((p) => p.id === id);
    return pump ? pump.pump_name : "-";
  }
  async function saveSale() {
    if (!stationId || !pumpId || !openingMeter || !closingMeter || !unitPrice) {
      return;
    }

    const { data: shift } = await supabase
      .from("pump_shifts")
      .select("*")
      .eq("pump_id", Number(pumpId))
      .eq("status", "OPEN")
      .single();

    if (!shift) {
      alert("No active Pump Shift found for this pump");
      return;
    }

    const { data: assignment } = await supabase
      .from("attendant_assignments")
      .select("*")
      .eq("pump_shift_id", shift.id)
      .eq("status", "ACTIVE")
      .single();

    if (!assignment) {
      alert("No active attendant assignment found");
      return;
    }

    const quantity = Number(closingMeter) - Number(openingMeter);

    if (quantity <= 0) {
      return;
    }

    const totalAmount = quantity * Number(unitPrice);

    const { error } = await supabase
      .from("fuel_sales")
      .insert([
        {
          station_id: salesContext?.business_day_id ? stationId : Number(stationId),
          pump_id: salesContext?.pump_id || Number(pumpId),
          pump_shift_id: shift.id,
          staff_id: assignment.staff_id,
          quantity: quantity,
          unit_price: Number(unitPrice),
          total_amount: totalAmount,
          payment_method: paymentMethod,

          sale_date: new Date().toISOString(),
        },
      ]);

    if (error) {
      console.error(error);
      return;
    }


    setStationId("");
    setPumpId("");
    setOpeningMeter("");
    setClosingMeter("");
    setUnitPrice("");
    setPaymentMethod("Cash");

    loadData();
  }

  return (
    <div>
      <h2>Fuel Sales</h2>

      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <h3>New Fuel Sale Entry</h3>          <select
            value={stationId}
            onChange={(e) => setStationId(e.target.value)}
          >
            <option value="">Select Station</option>
            {stations.map((station) => (
              <option key={station.id} value={station.id}>
                {station.name}
              </option>
            ))}
          </select>

          <select
            value={pumpId}
            onChange={(e) => setPumpId(e.target.value)}
          >
            <option value="">Select Pump</option>
            {pumps
              .filter((pump) => String(pump.station_id) === String(stationId))
              .map((pump) => (
                <option key={pump.id} value={pump.id}>
                  {pump.pump_name}
                </option>
              ))}
          </select>

          <input
            type="number"
            placeholder="Opening Meter"
            value={openingMeter}
            onChange={(e) => setOpeningMeter(e.target.value)}
          />

          <input
            type="number"
            placeholder="Closing Meter"
            value={closingMeter}
            onChange={(e) => setClosingMeter(e.target.value)}
          />

          <input
            type="number"
            placeholder="Unit Price"
            value={unitPrice}
            onChange={(e) => setUnitPrice(e.target.value)}
          />

          <select
            value={paymentMethod}
            onChange={(e) => setPaymentMethod(e.target.value)}
          >
            <option>Cash</option>
            <option>POS</option>
            <option>Transfer</option>
            <option>Credit</option>
          </select>

          <button onClick={saveSale}>Save Fuel Sale</button>

          <h3>Today's Summary</h3>
          <p>Total Sales: {sales.length}</p>

          <table border="1" cellPadding="5">
            <thead>
              <tr>
                <th>ID</th>
                <th>Date</th>
                <th>Station</th>
                <th>Pump</th>
                <th>Quantity</th>
                <th>Unit Price</th>
                <th>Total Amount</th>
              </tr>
            </thead>

            <tbody>
              {sales.map((sale) => (
                <tr key={sale.id}>
                  <td>{sale.id}</td>
                  <td>{sale.sale_date}</td>
                  <td>{getStationName(sale.station_id)}</td>
                  <td>{getPumpName(sale.pump_id)}</td>
                  <td>{sale.quantity}</td>
                  <td>{sale.unit_price}</td>
                  <td>{sale.total_amount}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}

export default FuelSales;













 