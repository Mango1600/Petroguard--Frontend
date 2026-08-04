from pathlib import Path

p = Path("src/pages/PaymentSummary.jsx")

s = p.read_text()

old = '''if (error) {
      setMessage(error.message);
    } else {
      setMessage("Payment saved successfully");
    }'''

new = '''if (error) {
      console.log(error);
      setMessage("SAVE ERROR: " + error.message);
    } else {
      setMessage("Payment saved successfully");
    }'''

if old in s:
    s = s.replace(old, new)
    p.write_text(s)
    print("Debug message added")
else:
    print("Target section not found")
