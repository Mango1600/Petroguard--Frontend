from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

target = '''      <button onClick={() => setShowFuelSales(!showFuelSales)}>
        {showFuelSales ? "Hide Fuel Sales" : "Open Fuel Sales"}
      </button>
'''

insert = target + '''
      <button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>
        {showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>
'''

if "Open Payment Summary" not in s:
    s = s.replace(target, insert)

p.write_text(s)

print("Payment button inserted after Fuel Sales")
