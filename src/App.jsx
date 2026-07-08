import { useEffect, useState } from "react";

function App() {
  const [stations, setStations] = useState([]);

  useEffect(() => {
    fetch("https://petroguard-api.onrender.com/stations")
      .then((res) => res.json())
      .then((data) => {
        setStations(data.stations || []);
      })
      .catch((err) => console.log(err));
  }, []);

  return (
    <div>
      <h1>PetroGuard Dashboard</h1>
      <h2>Stations</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Location</th>
            <th>Owner ID</th>
          </tr>
        </thead>

        <tbody>
          {stations.map((station) => (
            <tr key={station.id}>
              <td>{station.id}</td>
              <td>{station.name}</td>
              <td>{station.location || "-"}</td>
              <td>{station.owner_id || "-"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
