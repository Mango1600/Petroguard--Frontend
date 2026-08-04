from pathlib import Path

f = Path("src/pages/CashDeclaration.jsx")

t = f.read_text()

t = t.replace(
'import { supabase } from "../lib/supabase";',
'import { supabase } from "../lib/supabase";'
)

old = '''    alert("Daily receipt saved");'''

new = '''    const litres = Number(
      litresSold || 
      ((Number(closingMeter || 0) - Number(openingMeter || 0)))
    );

    const { data: pump } = await supabase
      .from("pump_readings")
      .select("product_type")
      .eq("pump_id", shift?.pump_id)
      .order("created_at", { ascending: false })
      .limit(1)
      .single();

    const { data: price } = await supabase
      .from("fuel_prices")
      .select("unit_price")
      .eq("product_type", pump?.product_type)
      .order("effective_date", { ascending: false })
      .limit(1)
      .single();

    const expectedRevenue =
      litres * Number(price?.unit_price || 0);

    const collected =
      Number(cash || 0) +
      Number(pos || 0) +
      Number(transfer || 0) +
      Number(credit || 0) -
      Number(expenses || 0);

    await supabase
      .from("daily_reconciliation")
      .insert([
        {
          station_id: Number(stationId),
          staff_id: shift?.staff_id,
          shift_id: shift?.id,
          fuel_sales: litres,
          cash_sales: Number(cash || 0),
          pos_sales: Number(pos || 0),
          transfer_sales: Number(transfer || 0),
          credit_sales_amount: Number(credit || 0),
          expected_revenue: expectedRevenue,
          revenue_variance: collected - expectedRevenue,
          status: "Pending Manager Approval"
        }
      ]);

    alert("Daily receipt saved and reconciliation created");'''

if old in t:
    t = t.replace(old,new)
else:
    print("Target line not found")

f.write_text(t)

print("✅ CashDeclaration reconciliation patch applied")
