from pathlib import Path

p = Path("src/pages/PaymentSummary.jsx")
s = p.read_text()

old = """  async function savePayment(status) {"""

new = """  async function savePayment(status) {
    try {"""

s = s.replace(old, new)

old2 = """    if (error) {
      console.log(error);
      setMessage("SAVE ERROR: " + error.message);
    } else {
      setMessage("Payment saved successfully");
    }
  }"""

new2 = """    if (error) {
      console.log(error);
      setMessage("SAVE ERROR: " + error.message);
    } else {
      setMessage("Payment saved successfully");
    }
    } catch (err) {
      console.log(err);
      setMessage("EXCEPTION: " + err.message);
    }
  }"""

if old in s and old2 in s:
    s = s.replace(old2, new2)
    p.write_text(s)
    print("Try/catch added")
else:
    print("Target section not found")
