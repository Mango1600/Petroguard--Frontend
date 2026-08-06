from pathlib import Path

p = Path("src/components/ManagerActivity.jsx")

text = p.read_text()

start = text.index("  async function loadActivities() {")
end = text.index("\n  return (", start)

new_function = r'''  async function loadActivities() {

    const { data, error } = await supabase
      .from("pump_shifts")
      .select(`
        id,
        opening_meter,
        closing_meter,
        status,
        pump_id,
        opened_by_staff_id,
        pumps (
          pump_name,
          product_type
        )
      `)
      .order("id", { ascending: false });

    if (error) {
      console.error("ManagerActivity Error:", error);
      return;
    }

    const rows = await Promise.all(
      (data || []).map(async (shift) => {

        const { data: staff } = await supabase
          .from("staff")
          .select("name,role")
          .eq("id", shift.opened_by_staff_id)
          .single();

        return {
          ...shift,
          staff
        };
      })
    );

    setActivities(rows);
  }
'''

text = text[:start] + new_function + text[end:]

p.write_text(text)

print("✅ ManagerActivity patched")
