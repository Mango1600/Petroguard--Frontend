from pathlib import Path

p = Path("src/pages/ManagerDashboard.jsx")
text = p.read_text()

text = text.replace(
'''    const { data, error } = await supabase
      .from("staff")
      .select(`
        id,
        name,
        role,
        email,
        status,
        staff_pumps (
          pump_id,
          pumps (
            pump_name,
            product_type
          )
        )
      `)
      .eq("role", "Attendant")
      .order("id");''',
'''    const { data, error } = await supabase
      .from("staff")
      .select("id,name,role,email,status")
      .eq("role","Attendant")
      .order("id");'''
)

p.write_text(text)
print("Manager query simplified")
