from pathlib import Path

p = Path("src/pages/Dashboard.jsx")

s = p.read_text()

target = '''      <button onClick={() => setShowDailyReconciliation(!showDailyReconciliation)}>'''

button = '''      <button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>
        {showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>

'''

if "Open Payment Summary" not in s:
    s = s.replace(target, button + target)

p.write_text(s)

print("Payment button added safely")
