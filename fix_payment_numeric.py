from pathlib import Path

p = Path("src/pages/PaymentSummary.jsx")
s = p.read_text()

# Add cleanNumber() once
if "const cleanNumber" not in s:
    s = s.replace(
        "async function savePayment(status) {",
        """const cleanNumber = (value) =>
    Number(String(value).replace(/₦|,/g, "").trim()) || 0;

  async function savePayment(status) {"""
    )

replacements = {
    "Number(form.cash_sales || 0)": "cleanNumber(form.cash_sales)",
    "Number(form.pos_sales || 0)": "cleanNumber(form.pos_sales)",
    "Number(form.transfer_sales || 0)": "cleanNumber(form.transfer_sales)",
    "Number(form.credit_sales || 0)": "cleanNumber(form.credit_sales)",
    "Number(form.other_income || 0)": "cleanNumber(form.other_income)",
    "Number(form.other_expenses || 0)": "cleanNumber(form.other_expenses)",

    "cash_sales: form.cash_sales": "cash_sales: cleanNumber(form.cash_sales)",
    "pos_sales: form.pos_sales": "pos_sales: cleanNumber(form.pos_sales)",
    "transfer_sales: form.transfer_sales": "transfer_sales: cleanNumber(form.transfer_sales)",
    "credit_sales: form.credit_sales": "credit_sales: cleanNumber(form.credit_sales)",
    "other_income: form.other_income": "other_income: cleanNumber(form.other_income)",
    "other_expenses: form.other_expenses": "other_expenses: cleanNumber(form.other_expenses)"
}

for old, new in replacements.items():
    s = s.replace(old, new)

p.write_text(s)

print("Numeric fix applied successfully.")
