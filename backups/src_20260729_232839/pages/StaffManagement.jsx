import { useEffect, useState } from "react";
import { supabase } from "../lib/supabase";

export default function StaffManagement() {
  const [staff, setStaff] = useState([]);
  const [form, setForm] = useState({
    name: "",
    email: "",
    phone: "",
    role: "Attendant",
    station_id: 1,
    status: "active",
  });

  useEffect(() => {
    loadStaff();
  }, []);

  async function loadStaff() {
    const { data } = await supabase
      .from("staff")
      .select("*")
      .order("name");

    setStaff(data || []);
  }

  async function saveStaff() {
    const { error } = await supabase
      .from("staff")
      .insert([form]);

    if (error) {
      return;
    }


    setForm({
      name: "",
      email: "",
      phone: "",
      role: "Attendant",
      station_id: 1,
      status: "active",
    });

    loadStaff();
  }

  return (
    <div style={{ padding: 20 }}>
      <h2>👥 Staff Management</h2>

      <input
        placeholder="Full Name"
        value={form.name}
        onChange={(e)=>setForm({...form,name:e.target.value})}
      /><br /><br />

      <input
        placeholder="Email"
        value={form.email}
        onChange={(e)=>setForm({...form,email:e.target.value})}
      /><br /><br />

      <input
        placeholder="Phone"
        value={form.phone}
        onChange={(e)=>setForm({...form,phone:e.target.value})}
      /><br /><br />

      <select
        value={form.role}
        onChange={(e)=>setForm({...form,role:e.target.value})}
      >
        <option>Manager</option>
        <option>Attendant</option>
        <option>Cashier</option>
        <option>Developer</option>
      </select>

      <br /><br />

      <button onClick={saveStaff}>
        Save Staff
      </button>

      <hr />

      <table border="1" cellPadding="8">
        <thead>
          <tr>
            <th>Name</th>
            <th>Role</th>
            <th>Email</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {staff.map((s)=>(
            <tr key={s.id}>
              <td>{s.name}</td>
              <td>{s.role}</td>
              <td>{s.email}</td>
              <td>{s.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}