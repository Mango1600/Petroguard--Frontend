import { useState, useEffect } from "react";
import { supabase } from "../lib/supabase";

export default function CompanySettings() {
  const [settings, setSettings] = useState({
    company_name: "ABC Petroleum Ltd.",
    opening_time: "07:00",
    closing_time: "18:30",
    currency: "NGN",
    tank_dip_required: true,
    manager_approval_required: true,
    business_day_close_required: true,
    max_cash_variance: 5000,
    max_tank_variance: 50
  });

  function handleChange(e) {
    const { name, value, type, checked } = e.target;

    setSettings({
      ...settings,
      [name]: type === "checkbox" ? checked : value
    });
  }

  async function loadSettings() {
    const { data, error } = await supabase
      .from("company_settings")
      .select("*")
      .limit(1)
      .single();

    if (!error && data) {
      setSettings(data);
    }
  }

  async function saveSettings() {
    const { error } = await supabase
      .from("company_settings")
      .update(settings)
      .eq("id", settings.id);

    if (error) {
      alert(error.message);
      return;
    }

    alert("Company Settings saved successfully.");
  }

  useEffect(() => {
    loadSettings();
  }, []);

  return (
    <div>
      <h2>🏢 Company Settings</h2>

      <label>Company Name</label><br />
      <input
        name="company_name"
        value={settings.company_name}
        onChange={handleChange}
      />

      <br /><br />

      <label>Business Day Opening Time</label><br />
      <input
        type="time"
        name="opening_time"
        value={settings.opening_time}
        onChange={handleChange}
      />

      <br /><br />

      <label>Business Day Closing Time</label><br />
      <input
        type="time"
        name="closing_time"
        value={settings.closing_time}
        onChange={handleChange}
      />

      <br /><br />

      <label>Currency</label><br />
      <input
        name="currency"
        value={settings.currency}
        onChange={handleChange}
      />

      <br /><br />

      <label>
        <input
          type="checkbox"
          name="tank_dip_required"
          checked={settings.tank_dip_required}
          onChange={handleChange}
        />
        Tank Dip Required
      </label>

      <br />

      <label>
        <input
          type="checkbox"
          name="manager_approval_required"
          checked={settings.manager_approval_required}
          onChange={handleChange}
        />
        Manager Approval Required
      </label>

      <br />

      <label>
        <input
          type="checkbox"
          name="business_day_close_required"
          checked={settings.business_day_close_required}
          onChange={handleChange}
        />
        Business Day Close Required
      </label>

      <br /><br />

      <label>Maximum Cash Variance (₦)</label><br />
      <input
        type="number"
        name="max_cash_variance"
        value={settings.max_cash_variance}
        onChange={handleChange}
      />

      <br /><br />

      <label>Maximum Tank Variance (Litres)</label><br />
      <input
        type="number"
        name="max_tank_variance"
        value={settings.max_tank_variance}
        onChange={handleChange}
      />

      <br /><br />

      <button onClick={saveSettings}>
        💾 Save Company Settings
      </button>
    </div>
  );
}
