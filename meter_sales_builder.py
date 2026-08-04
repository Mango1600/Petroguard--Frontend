from pathlib import Path

files = {}

files["supabase/meter_sales.sql"] = '''
create extension if not exists pgcrypto;

create table if not exists meter_sales (

    id uuid primary key default gen_random_uuid(),

    business_day_id uuid not null references business_days(id),

    pump_shift_id uuid not null references pump_shifts(id),

    assignment_id uuid not null references pump_shift_assignments(id),

    pump_id uuid not null references pumps(id),

    opening_meter numeric not null,

    closing_meter numeric not null,

    litres_sold numeric not null,

    unit_price numeric not null,

    total_amount numeric not null,

    calculated_at timestamptz default now()
);
'''

files["src/lib/meterSales.js"] = '''
export function calculateSales(openingMeter, closingMeter, unitPrice) {
  const litresSold = closingMeter - openingMeter;
  const totalAmount = litresSold * unitPrice;

  return {
    litresSold,
    totalAmount,
  };
}
'''
files["src/pages/MeterSales.jsx"] = '''
export default function MeterSales() {
  return (
    <div>
      <h2>Automatic Meter Sales</h2>
      <p>Sales are calculated from meter readings.</p>
    </div>
  );
}
'''

files["src/components/MeterSalesCard.jsx"] = '''
export default function MeterSalesCard({opening, closing, litres, amount}) {
  return (
    <div>
      <h3>Meter Sales</h3>
      <p>Opening: {opening}</p>
      <p>Closing: {closing}</p>
      <p>Litres Sold: {litres}</p>
      <p>Total Amount: ₦{amount}</p>
    </div>
  );
}
'''

files["src/components/MeterSalesSummary.jsx"] = '''
export default function MeterSalesSummary({litres, amount}) {
  return (
    <div>
      <h3>Sales Summary</h3>
      <p>Total Litres: {litres}</p>
      <p>Total Sales: ₦{amount}</p>
    </div>
  );
}
'''

files["src/components/MeterReadingForm.jsx"] = '''
export default function MeterReadingForm() {
  return (
    <div>
      <h3>Closing Meter Reading</h3>
      <p>Opening meter comes from the active assignment.</p>
    </div>
  );
}
'''

for filename, content in files.items():
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")

print("MODULE 4 CREATED")
print("FILES:", len(files))
for f in files:
    print("✓", f)


# ==========================================
# MODULE 5 - PAYMENT ALLOCATION VALIDATION
# Production Rules
# ==========================================

def validate_payment_allocation(
    total_sales_amount,
    cash,
    pos,
    bank_transfer,
    credit
):
    allocated_amount = (
        cash +
        pos +
        bank_transfer +
        credit
    )

    if allocated_amount != total_sales_amount:
        raise ValueError(
            "Payment allocation does not match calculated sales amount"
        )

    return {
        "total_sales_amount": total_sales_amount,
        "cash": cash,
        "pos": pos,
        "bank_transfer": bank_transfer,
        "credit": credit,
        "status": "BALANCED"
    }


