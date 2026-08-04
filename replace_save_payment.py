from pathlib import Path
import re

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

new_function = r'''
  async function savePayment(status) {
    try {
      const today = new Date().toISOString().split("T")[0];

      const totalCollected =
        cleanNumber(form.cash_sales) +
        cleanNumber(form.pos_sales) +
        cleanNumber(form.transfer_sales) +
        cleanNumber(form.credit_sales) +
        cleanNumber(form.other_income) -
        cleanNumber(form.other_expenses);

      const payload = {
        station_id: staff.station_id,
        staff_id: staff?.id ?? null,
        reconciliation_date: today,

        cash_sales: cleanNumber(form.cash_sales),
        pos_sales: cleanNumber(form.pos_sales),
        transfer_sales: cleanNumber(form.transfer_sales),
        credit_sales_amount: cleanNumber(form.credit_sales),

        expected_revenue: totalCollected,
        revenue_variance: 0,
        status: status === "draft" ? "Draft" : "Submitted"
      };

      const { data: existing, error: findError } = await supabase
        .from("daily_reconciliation")
        .select("id")
        .eq("station_id", staff.station_id)
        .eq("reconciliation_date", today)
        .maybeSingle();

      if (findError) throw findError;

      let result;

      if (existing) {
        result = await supabase
          .from("daily_reconciliation")
          .update(payload)
          .eq("id", existing.id);
      } else {
        result = await supabase
          .from("daily_reconciliation")
          .insert(payload);
      }

      if (result.error) throw result.error;

      setMessage("Payment saved successfully");
    } catch (err) {
      console.error(err);
      setMessage("SAVE ERROR: " + err.message);
    }
  }
'''

pattern = r'async function savePayment\(status\)\s*\{.*?\n\s*\}\n\s*\n\s*return \('

match = re.search(pattern, text, flags=re.S)

if not match:
    print("savePayment() not found.")
    raise SystemExit

replacement = new_function + "\n\n  return ("

text = re.sub(pattern, replacement, text, flags=re.S)

path.write_text(text)

print("savePayment() replaced successfully.")
