from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

old = 'const [showBusinessDayManagement, setShowBusinessDayManagement] = useState(false);'

new = old + '\nconst [showPaymentSummary, setShowPaymentSummary] = useState(false);'

if 'showPaymentSummary' not in s:
    s = s.replace(old, new)

p.write_text(s)

print("Payment state added")
