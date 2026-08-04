from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

old = ': "Open Business Day Management"}'

new = ''': "Open Business Day Management"}
      </button>

      <button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>
        {showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>'''

s = s.replace(old, new)

p.write_text(s)

print("Payment button added")
