from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

old = 'setMessage("Payment saved successfully");'

new = '''if (status === "submitted") {
      setMessage("Payment submitted successfully.");
    } else {
      setMessage("Payment saved successfully.");
    }'''

if old in text:
    text = text.replace(old, new)
    path.write_text(text)
    print("Submit message updated successfully.")
else:
    print("Target text not found.")
