import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function PumpManagement() {
  const [pumps, setPumps] = useState([]);
  const [stations, setStations] = useState([]);

  const [form, setForm] = useState({
    station_id: "",
    pump_name: "",
    product_type: "PMS",
    status: "Active",
  });

  useEffect(() => {
    loadPumps();
    loadStations();
  }, []);

  async function loadPumps() {
    const { data, error } = await supabase
      .from("pumps")
      .select(`
        id,
        pump_name,
        product_type,
        status,
        stations (
          name
        )
      `)
      .order("id");

    if (error) {
      alert(error.message);
      return;
    }

    setPumps(data || []);
  }

  async function loadStations() {
    const { data, error } = await supabase
      .from("stations")
      .select("id, name")
      .order("name");

    if (error) {
      alert(error.message);
      return;
    }

    setStations(data || []);
  }

  async function addPump(e) {
    e.preventDefault();

    const { error } = await supabase
      .from("pumps")
      .insert([form]);

    if (error) {
      alert(error.message);
      return;
    }

    loadPumps();
  }

  return (
    <div>
      <h1>Pump Management</h1>

      <h2>Add New Pump</h2>

      <form onSubmit={addPump}>

        <select
          value={form.station_id}
          onChange={(e)=>
            setForm({
              ...form,
              station_id:e.target.value
            })
          }
        >
          <option value="">
            Select Station
          </option>

          {stations.map((station)=>(
            <option key={station.id} value={station.id}>
              {station.name}
            </option>
          ))}

        </select>

        <br />

        <input
          placeholder="Pump Name"
          value={form.pump_name}
          onChange={(e)=>
            setForm({
              ...form,
              pump_name:e.target.value
            })
          }
        />

        <br />

        <select
          value={form.product_type}
          onChange={(e)=>
            setForm({
              ...form,
              product_type:e.target.value
            })
          }
        >
          <option>PMS</option>
          <option>AGO</option>
          <option>DPK</option>
        </select>

        <br />

        <select
          value={form.status}
          onChange={(e)=>
            setForm({
              ...form,
              status:e.target.value
            })
          }
        >
          <option>Active</option>
          <option>Maintenance</option>
          <option>Disabled</option>
        </select>

        <br />

        <button>
          Add Pump
        </button>

      </form>

      <hr />

      <h2>Pumps</h2>

      <table border="1" cellPadding="8">

        <thead>
          <tr>
            <th>Pump</th>
            <th>Station</th>
            <th>Product</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>

        {pumps.map((pump)=>(
          <tr key={pump.id}>
            <td>{pump.pump_name}</td>
            <td>{pump.stations?.name || "-"}</td>
            <td>{pump.product_type}</td>
            <td>{pump.status}</td>
          </tr>
        ))}

        </tbody>

      </table>

    </div>
  );
}
