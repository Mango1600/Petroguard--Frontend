import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function StationManagement() {
  const [stations, setStations] = useState([]);
  const [companies, setCompanies] = useState([]);

  const [form, setForm] = useState({
    name: "",
    location: "",
    company_id: "",
    latitude: "",
    longitude: "",
    gps_radius: 100,
  });

  useEffect(() => {
    loadStations();
    loadCompanies();
  }, []);

  async function loadStations() {
    const { data, error } = await supabase
      .from("stations")
      .select(`
        id,
        name,
        location,
        latitude,
        longitude,
        gps_radius,
        companies (
          company_name
        )
      `)
      .order("id");

    if (error) {
      alert(error.message);
      return;
    }

    setStations(data || []);
  }

  async function loadCompanies() {
    const { data, error } = await supabase
      .from("companies")
      .select("id, company_name")
      .order("company_name");

    if (error) {
      alert(error.message);
      return;
    }

    setCompanies(data || []);
  }

  async function addStation(e) {
    e.preventDefault();

    const { error } = await supabase
      .from("stations")
      .insert([
        {
          name: form.name,
          location: form.location,
          company_id: form.company_id,
          latitude: form.latitude,
          longitude: form.longitude,
          gps_radius: form.gps_radius,
        },
      ]);

    if (error) {
      alert(error.message);
      return;
    }

    loadStations();
  }

  return (
    <div>
      <h1>Station Management</h1>

      <h2>Add New Station</h2>

      <form onSubmit={addStation}>
        <input
          placeholder="Station name"
          onChange={(e) =>
            setForm({...form, name:e.target.value})
          }
        />

        <br />

        <input
          placeholder="Location"
          onChange={(e) =>
            setForm({...form, location:e.target.value})
          }
        />

        <br />

        <select
          onChange={(e) =>
            setForm({...form, company_id:e.target.value})
          }
        >
          <option>Select Company</option>

          {companies.map((company)=>(
            <option key={company.id} value={company.id}>
              {company.company_name}
            </option>
          ))}

        </select>

        <br />

        <input
          placeholder="Latitude"
          onChange={(e)=>
            setForm({...form, latitude:e.target.value})
          }
        />

        <br />

        <input
          placeholder="Longitude"
          onChange={(e)=>
            setForm({...form, longitude:e.target.value})
          }
        />

        <br />

        <button>
          Add Station
        </button>

      </form>

      <hr />

      <h2>Stations</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Name</th>
            <th>Company</th>
            <th>Location</th>
            <th>GPS</th>
          </tr>
        </thead>

        <tbody>

        {stations.map((station)=>(
          <tr key={station.id}>
            <td>{station.name}</td>
            <td>
              {station.companies?.company_name || "-"}
            </td>
            <td>{station.location}</td>
            <td>
              {station.latitude},
              {station.longitude}
            </td>
          </tr>
        ))}

        </tbody>
      </table>

    </div>
  );
}
