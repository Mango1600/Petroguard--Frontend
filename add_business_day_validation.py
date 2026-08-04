from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

# Add imports
text = text.replace(
    'import { useState } from "react";',
    'import { useState, useEffect } from "react";\nimport { supabase } from "../lib/supabase";'
)

# Add states
text = text.replace(
    'const [message, setMessage] = useState("");',
    '''const [message, setMessage] = useState("");
  const [checks, setChecks] = useState({});
  const [settings, setSettings] = useState(null);'''
)

# Replace close function
old = '''function handleCloseDay() {
    setMessage("Business Day Close validation will be implemented in the next step.");
  }'''

new = '''async function loadSettings() {

    const { data, error } = await supabase
      .from("company_settings")
      .select("*")
      .limit(1)
      .single();

    if (!error && data) {
      setSettings(data);
    }
  }


  async function handleCloseDay() {

    const result = {

      attendance: true,

      pump_readings: true,

      tank_dip:
        settings?.tank_dip_required ? false : true,

      payment_summary: true,

      manager_approval:
        settings?.manager_approval_required ? false : true
    };


    setChecks(result);


    const failed = Object.values(result)
      .some(item => item === false);


    if (failed) {

      setMessage(
        "Cannot close Business Day. Pending requirements detected."
      );

    } else {

      setMessage(
        "Business Day Closed Successfully."
      );
    }
  }


  useEffect(() => {
    loadSettings();
  }, []);'''

text = text.replace(old, new)

path.write_text(text)

print("Business Day validation engine added successfully.")
