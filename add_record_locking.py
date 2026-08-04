from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add paymentStatus state if it doesn't exist
if 'const [paymentStatus' not in text:
    text = text.replace(
        'const [message, setMessage] = useState("");',
        '''const [message, setMessage] = useState("");
  const [paymentStatus, setPaymentStatus] = useState("Draft");'''
    )

# Add lock flag if it doesn't exist
if 'const isLocked' not in text:
    text = text.replace(
        'async function savePayment(status) {',
        '''const isLocked =
    paymentStatus === "Submitted" ||
    paymentStatus === "Approved";

  async function savePayment(status) {'''
    )

# Update success message to keep local status in sync
text = text.replace(
    'setMessage("Payment submitted successfully.");',
    '''setPaymentStatus("Submitted");
      setMessage("Payment submitted successfully.");'''
)

text = text.replace(
    'setMessage("Payment saved successfully.");',
    '''setPaymentStatus("Draft");
      setMessage("Payment saved successfully.");'''
)

path.write_text(text)
print("Record locking state added successfully.")
