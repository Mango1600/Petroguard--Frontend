from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

target = '{showFuelSales && <FuelSales staff={staff} />}'

insert = target + '\n\n      {showPaymentSummary && <PaymentSummary staff={staff} />}'

if "showPaymentSummary && <PaymentSummary" not in s:
    s = s.replace(target, insert)

p.write_text(s)

print("Payment Summary render added")
