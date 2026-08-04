from pathlib import Path

path = Path("src/pages/CompanySettings.jsx")
text = path.read_text()

# Add imports
text = text.replace(
    'import { useState } from "react";',
    'import { useState, useEffect } from "react";\nimport { supabase } from "../lib/supabase";'
)

# Add loadSettings before saveSettings
old = '''  function saveSettings() {
    alert("Company Settings saved successfully.");
  }'''

new = '''  async function loadSettings() {
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
  }'''

text = text.replace(old, new)

# Add useEffect before return
text = text.replace(
    '  return (',
    '''  useEffect(() => {
    loadSettings();
  }, []);

  return ('''
)

path.write_text(text)

print("Company Settings connected to Supabase successfully.")
