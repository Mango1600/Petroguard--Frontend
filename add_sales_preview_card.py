from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

if "Sales Reconciliation Preview" not in text:

    marker = """
      <h2>💰 Payment Summary</h2>
"""

    preview = """
      <h2>💰 Payment Summary</h2>

      <div>
        <h3>📊 Sales Reconciliation Preview</h3>

        <p>
          Total Submitted:
          ₦{totalCollected.toLocaleString()}
        </p>

        <p>
          Expected Revenue:
          ₦{totalCollected.toLocaleString()}
        </p>

        <p>
          Variance:
          ₦0
        </p>

        <p>
          Status:
          🟢 Balanced
        </p>
      </div>
"""

    text = text.replace(marker, preview)

    # Add calculation before return
    text = text.replace(
        "return (",
        """
  const totalCollected =
    cleanNumber(form.cash_sales) +
    cleanNumber(form.pos_sales) +
    cleanNumber(form.transfer_sales) +
    cleanNumber(form.credit_sales) +
    cleanNumber(form.other_income) -
    cleanNumber(form.other_expenses);

  return (
"""
    )

path.write_text(text)

print("Sales preview card added successfully.")
