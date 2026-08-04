from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

old = 'import BusinessDayManagement from "./BusinessDayManagement";'

new = old + '\nimport PaymentSummary from "./PaymentSummary";'

if 'import PaymentSummary from "./PaymentSummary";' not in s:
    s = s.replace(old, new)

p.write_text(s)

print("Payment import added")
