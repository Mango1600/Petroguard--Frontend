from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

s = s.replace(
    "{showPaymentSummary && <PaymentSummary />}",
    "{showPaymentSummary && <PaymentSummary staff={staff} />}"
)

p.write_text(s)

print("PaymentSummary staff prop fixed")
