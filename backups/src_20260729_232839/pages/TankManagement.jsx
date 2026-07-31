import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function TankManagement() {
  const [stations, setStations] = useState([]);
  const [tanks, setTanks] = useState([]);

  const [stationId, setStationId] = useState("");
  const [tankName, setTankName] = useState("");
  const [productType, setProductType] = useState("PMS");
  const [capacity, setCapacity] = useState("");
  const [status, setStatus] = useState("Active");

  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  useEffect(() => {
    loadStations();
    loadTanks();
  }, []);

  async function loadStations() {
    const { data, error } = await supabase
      .from("stations")
      .select("id, name")
      .order("name");

    if (error) {
      console.error(error);
      return;
    }

    setStations(data || []);
  }

  async function loadTanks() {
    const { data, error } = await supabase
      .from("tanks")
      .select(`
        id,
        tank_name,
        product_type,
        capacity,
        status,
        station_id,
        stations(name)
      `)
      .order("id", { ascending: false });

    if (error) {
      console.error(error);
      return;
    }

    setTanks(data || []);
  }

  async function saveTank(e) {
    e.preventDefault();

    if (!stationId || !tankName || !capacity) {
      setMessage("Please fill all required fields");
      return;
    }

    setLoading(true);
    setMessage("");

    const { error } = await supabase
      .from("tanks")
      .insert([
        {
          station_id: stationId,
          tank_name: tankName,
          product_type: productType,
          capacity: Number(capacity),
          status: status,
        },
      ]);

    if (error) {
      console.error(error);
      setMessage(error.message);
      setLoading(false);
      return;
    }

    setMessage("Tank added successfully");

    setTankName("");
    setCapacity("");
    setProductType("PMS");
    setStatus("Active");

    await loadTanks();

    setLoading(false);
  }  return (
    <div>
      <h2>Tank Management</h2>

      {message && (
        <p>{message}</p>
      )}

      <hr />

      <h3>Add New Tank</h3>

      <form onSubmit={saveTank}>

        <div>
          <label>Station</label>
          <br />

          <select
            value={stationId}
            onChange={(e) => setStationId(e.target.value)}
          >
            <option value="">
              Select Station
            </option>

            {stations.map((station) => (
              <option
                key={station.id}
                value={station.id}
              >
                {station.name}
              </option>
            ))}

          </select>
        </div>


        <br />

        <div>
          <label>Tank Name</label>
          <br />

          <input
            type="text"
            value={tankName}
            onChange={(e) => setTankName(e.target.value)}
            placeholder="Example: PMS Tank 1"
          />

        </div>


        <br />

        <div>
          <label>Product Type</label>
          <br />

          <select
            value={productType}
            onChange={(e) => setProductType(e.target.value)}
          >

            <option value="PMS">
              PMS
            </option>

            <option value="AGO">
              AGO
            </option>

            <option value="DPK">
              DPK
            </option>

            <option value="LPG">
              LPG
            </option>

            <option value="CNG">
              CNG
            </option>

          </select>

        </div>


        <br />


        <div>
          <label>
            Capacity
          </label>

          <br />

          <input
            type="number"
            value={capacity}
            onChange={(e) => setCapacity(e.target.value)}
            placeholder="Tank capacity"
          />

        </div>


        <br />


        <div>
          <label>
            Status
          </label>

          <br />

          <select
            value={status}
            onChange={(e) => setStatus(e.target.value)}
          >

            <option value="Active">
              Active
            </option>

            <option value="Maintenance">
              Maintenance
            </option>

            <option value="Disabled">
              Disabled
            </option>

          </select>

        </div>


        <br />


        <button type="submit" disabled={loading}>

          {loading
            ? "Saving..."
            : "Save Tank"}

        </button>


      </form>


      <hr />


      <h3>
        Tank List
      </h3>


      {tanks.length === 0 ? (

        <p>
          No tanks found
        </p>

      ) : (

        <table border="1">

          <thead>

            <tr>

              <th>
                ID
              </th>

              <th>
                Station
              </th>

              <th>
                Tank Name
              </th>

              <th>
                Product
              </th>

              <th>
                Capacity
              </th>

              <th>
                Status
              </th>

            </tr>

          </thead>


          <tbody>

            {tanks.map((tank) => (

              <tr key={tank.id}>

                <td>
                  {tank.id}
                </td>

                <td>
                  {tank.stations?.name || "-"}
                </td>

                <td>
                  {tank.tank_name}
                </td>

                <td>
                  {tank.product_type}
                </td>

                <td>
                  {tank.capacity}
                </td>

                <td>
                  {tank.status}
                </td>

              </tr>

            ))}

          </tbody>


        </table>

      )}

    </div>
  );
}
