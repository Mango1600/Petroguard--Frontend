import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function FuelSales() {
  const [sales, setSales] = useState([]);
  const [stations, setStations] = useState([]);
  const [pumps, setPumps] = useState([]);
  const [loading, setLoading] = useState(true);

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
      alert(salesError.message);
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
  if (loading) {
    return <p>Loading Fuel Sales...</p>;
  }

  return (
    <div>
      <h2>Fuel Sales</h2>

      <h3>Today's Summary</h3>

      <p><strong>Total Sales:</strong> {sales.length}</p>

      <table border="1" cellPadding="6">
        <thead>
          <tr>
            <th>ID</th>
            <th>Date</th>
            <th>Station</th>
            <th>Pump</th>
            <th>Product</th>
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
              <td>{sale.product_type}</td>
              <td>{sale.quantity}</td>
              <td>{sale.unit_price}</td>
              <td>{sale.total_amount}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default FuelSales;
