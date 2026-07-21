import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function StaffManagement() {
  const [staffList, setStaffList] = useState([]);

  const [form, setForm] = useState({
    name: "",
    role: "Attendant",
    phone: "",
    email: "",
    station_id: 1,
    status: "Active",
  });

  useEffect(() => {
    loadStaff();
  }, []);

  async function loadStaff() {
  const { data, error } = await supabase
    .from("staff")
    .select(`
      id,
      name,
      role,
      phone,
      email,
      status,
      stations!staff_station_id_fkey (
        name
      )
    `)
    .order("id");

  if (error) {
    console.error(error);
    alert(error.message);
    return;
  }

  setStaffList(data || []);
}

  async function addStaff(e) {
    e.preventDefault();

    const { error } = await supabase
      .from("staff")
      .insert([
        {
          name: form.name,
          role: form.role,
          phone: form.phone,
          email: form.email,
          station_id: form.station_id,
          status: form.status,
        },
      ]);

    if (error) {
      alert(error.message);
      return;
    }

    setForm({
      name: "",
      role: "Attendant",
      phone: "",
      email: "",
      station_id: 1,
      status: "Active",
    });

    loadStaff();
  }

  return (
    <div>
      <h1>Staff Management</h1>

      <h2>Add New Staff</h2>

      <form onSubmit={addStaff}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) =>
            setForm({ ...form, name: e.target.value })
          }
        />

        <br />

        <input
          placeholder="Phone"
          value={form.phone}
          onChange={(e) =>
            setForm({ ...form, phone: e.target.value })
          }
        />

        <br />

        <input
          placeholder="Email"
          value={form.email}
          onChange={(e) =>
            setForm({ ...form, email: e.target.value })
          }
        />

        <br />

        <select
          value={form.role}
          onChange={(e) =>
            setForm({ ...form, role: e.target.value })
          }
        >
          <option>Attendant</option>
          <option>Cashier</option>
          <option>Manager</option>
        </select>

        <br />

        <button type="submit">
          Add Staff
        </button>
      </form>

      <hr />

      <h2>Staff List</h2>

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Station</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {staffList.map((person) => (
            <tr key={person.id}>
              <td>{person.name}</td>
              <td>{person.role}</td>
              <td>{person.email}</td>
              <td>{person.phone}</td>
              <td>
                {person.stations?.name || "-"}
              </td>
              <td>{person.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
