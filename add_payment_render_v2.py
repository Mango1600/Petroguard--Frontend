from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

target = '{showFuelSales && <FuelSales />}'

new = target + '\n      {showPaymentSummary && <PaymentSummary />}'

if "{showPaymentSummary && <PaymentSummary />}" not in s:
    s = s.replace(target, new)

p.write_text(s)

print("Payment render added")
