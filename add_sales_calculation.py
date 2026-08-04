from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add calculation before return
if "totalCollected" not in text:
    text = text.replace(
        "return (",
        """
  const totalCollected =
    Number(form.cash_sales || 0) +
    Number(form.pos_sales || 0) +
    Number(form.transfer_sales || 0) +
    Number(form.credit_sales || 0) +
    Number(form.other_income || 0) -
    Number(form.other_expenses || 0);

  const variance =
    Number(form.expected_revenue || 0) - totalCollected;

  return (
"""
    )

path.write_text(text)

print("Sales calculation logic added successfully.")
