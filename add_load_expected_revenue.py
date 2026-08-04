from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

if "async function loadExpectedRevenue()" not in text:

    insert_after = """  async function loadPaymentStatus() {
"""

    function = """
  async function loadExpectedRevenue() {
    const today = new Date().toISOString().split("T")[0];

    const { data, error } = await supabase
      .from("fuel_sales")
      .select("total_amount")
      .eq("station_id", staff.station_id)
      .gte("sale_date", today + "T00:00:00")
      .lt("sale_date", today + "T23:59:59");

    if (error) {
      console.error(error);
      return;
    }

    const total = (data || []).reduce(
      (sum, row) => sum + Number(row.total_amount || 0),
      0
    );

    setExpectedRevenue(total);
  }

"""

    text = text.replace(insert_after, function + insert_after)

path.write_text(text)

print("loadExpectedRevenue() added successfully.")
