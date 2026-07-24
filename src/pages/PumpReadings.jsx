import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

function PumpReadings() {
  const [readings, setReadings] = useState([]);
  const [stations, setStations] = useState([]);
  const [staff, setStaff] = useState([]);
  const [shifts, setShifts] = useState([]);
  const [fuelPrices, setFuelPrices] = useState([]);
  const [loading, setLoading] = useState(true);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    loadData();
  }, []);

  async function loadData() {
    setLoading(true);

    const {
      data: { session },
    } = await supabase.auth.getSession();

    console.log("Session:", session);

    const [pumpResult, stationResult, staffResult, shiftResult] = await Promise.all([
      supabase
        .from("pump_readings")
        .select(`
          *,
          pumps(
            pump_name,
            product_type
          )
        `)
        .order("id"),

      supabase
        .from("stations")
        .select("*")
        .order("id"),

      supabase
        .from("staff")
        .select("*")
        .order("id"),

      supabase
        .from("staff_shifts")
        .select("*")
        .order("id"),

      supabase
        .from("fuel_prices")
        .select("*")
        .order("effective_date", { ascending: false }),
    ]);

    console.log("Pump data:", pumpResult.data);
    console.log("Pump error:", pumpResult.error);

    if (pumpResult.error) {
      setErrorMessage(pumpResult.error.message);
      setLoading(false);
      return;
    }

    if (stationResult.error) {
      setErrorMessage(stationResult.error.message);
      setLoading(false);
      return;
    }

    setReadings(pumpResult.data || []);
    setStations(stationResult.data || []);
    setStaff(staffResult.data || []);
    setShifts(shiftResult.data || []);
    setFuelPrices(shiftResult.data || []);
    setLoading(false);
  }




  async function submitReading(id) {
    const { error } = await supabase
      .from("pump_readings")
      .update({
        status: "submitted",
        submitted_at: new Date().toISOString()
      })
      .eq("id", id);

    if (error) {
      alert(error.message);
      console.log(error);
      return;
    }

    alert("Submitted successfully");
    loadData();
  }

  async function verifyReading(id) {
    const { error } = await supabase
      .from("pump_readings")
      .update({
        status: "verified",
        verified_at: new Date().toISOString()
      })
      .eq("id", id);

    if (error) {
      alert(error.message);
      return;
    }

    alert("Verified successfully");
    loadData();
  }

  async function approveReading(id) {
    const { data, error } = await supabase
      .from("pump_readings")
      .update({
        status: "approved",
        approved_at: new Date().toISOString()
      })
      .eq("id", id)
      .select();

    console.log("Approve result:", data, error);

    if (error) {
      alert(error.message);
      return;
    }

    if (!data || data.length === 0) {
      alert("No row was updated.");
      return;
    }

    alert("Approved successfully");
    loadData();
  }

  function getStationName(stationId) {
    const station = stations.find((s) => s.id === stationId);
    return station ? station.name : `Station ${stationId}`;
  }

  function getStaffName(staffId) {
    const person = staff.find((s) => s.id === staffId);
    return person ? person.name : `Staff ${staffId}`;
  }

  function getShift(shiftId) {
    return shifts.find((s) => s.id === shiftId);
  }

  function getFuelPrice(productType) {
    const price = fuelPrices.find(
      (p) => p.product_type === productType
    );

    return price ? price.unit_price : 0;
  }

  if (loading) {
    return <p>Loading pump readings...</p>;
  }

  if (errorMessage) {
    return <p>Error: {errorMessage}</p>;
  }

  return (
    <div>
      <h2>Pump Readings</h2>

      {readings.length === 0 ? (
        <p>No pump readings found.</p>
      ) : (
        readings.map((reading) => (
          <div key={reading.id}>
            <h3>Pump Transaction #{reading.id}</h3>

            <p>Station: {getStationName(reading.station_id)}</p>

            <p>
              Attendant: {getStaffName(reading.staff_id)}
            </p>

            <p>
              Shift ID: {reading.staff_shift_id || "Not assigned"}
            </p>

            <p>
              Pump: {reading.pumps?.pump_name || `Pump ${reading.pump_id}`}
            </p>

            <p>
              Product: {reading.pumps?.product_type || "Not set"}
            </p>

            <p>Opening Meter: {reading.opening_meter} L</p>

            <p>Closing Meter: {reading.closing_meter} L</p>

            <p>
              Litres Sold: {Number(reading.closing_meter) - Number(reading.opening_meter)} L
            </p>

            <hr />

            <h4>Sales Calculation</h4>

            <p>
              Unit Price:
              ₦{Number(
                getFuelPrice(reading.pumps?.product_type)
              ).toLocaleString()}
            </p>

            <p>
              Expected Sales:
              ₦{(
                (Number(reading.closing_meter) -
                Number(reading.opening_meter)) *
                Number(getFuelPrice(reading.pumps?.product_type))
              ).toLocaleString()}
            </p>

            <hr />

            <h4>Payment Summary</h4>

            <p>Cash: ₦{Number(reading.cash_sales).toLocaleString()}</p>
            <p>POS: ₦{Number(reading.pos_sales).toLocaleString()}</p>
            <p>Transfer: ₦{Number(reading.transfer_sales).toLocaleString()}</p>
            <p>Credit: ₦{Number(reading.credit_sales).toLocaleString()}</p>

            <p>
              Total Collected: ₦{Number(reading.total_collected).toLocaleString()}
            </p>

            <p>
              Sales Variance: ₦{Number(reading.sales_variance).toLocaleString()}
            </p>

            <p>Status: {reading.status}</p>

            {reading.status === "draft" && (
              <button onClick={() => submitReading(reading.id)}>
                Submit
              </button>
            )}

            {reading.status === "submitted" && (
              <button onClick={() => verifyReading(reading.id)}>
                Verify
              </button>
            )}

            {reading.status === "verified" && (
              <button onClick={() => approveReading(reading.id)}>
                Approve
              </button>
            )}

            <hr />
          </div>
        ))
      )}
    </div>
  );
}

export default PumpReadings;
