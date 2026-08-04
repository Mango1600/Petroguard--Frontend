from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

old = """
      payment_summary: true,
"""

new = """
      const { data: payment } = await supabase
        .from("daily_reconciliation")
        .select("*")
        .eq("station_id", staff.station_id)
        .eq("reconciliation_date", today)
        .maybeSingle();


      payment_summary:
        !!payment &&
        (
          Number(payment.cash_sales || 0) +
          Number(payment.pos_sales || 0) +
          Number(payment.transfer_sales || 0) +
          Number(payment.credit_sales_amount || 0)
        ) > 0,
"""

if old in text:
    text = text.replace(old, new)

path.write_text(text)

print("Payment Summary validation added successfully.")
