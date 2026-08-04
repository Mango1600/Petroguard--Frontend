from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add state after paymentStatus
old = 'const [paymentStatus, setPaymentStatus] = useState("Draft");'

new = '''const [paymentStatus, setPaymentStatus] = useState("Draft");
  const [expectedRevenue, setExpectedRevenue] = useState(0);'''

if old in text and "expectedRevenue" not in text:
    text = text.replace(old, new)

path.write_text(text)

print("Expected Revenue state added successfully.")
