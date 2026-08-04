from pathlib import Path

path = Path("src/pages/Dashboard.jsx")

text = path.read_text()

# Add button after Payment Summary button
old = '''      <button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>
        {showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>'''

new = old + '''

      <br /><br />

      <button onClick={() => setShowOperationsAnalysis(!showOperationsAnalysis)}>
        {showOperationsAnalysis ? "Hide Operations Analysis" : "Open Operations Analysis"}
      </button>'''

if old in text and "Open Operations Analysis" not in text:
    text = text.replace(old, new)

# Add render after PaymentSummary
old2 = '''      {showPaymentSummary && <PaymentSummary staff={staff} />}'''

new2 = old2 + '''

      {showOperationsAnalysis && <OperationsAnalysis staff={staff} />}'''

if old2 in text and "OperationsAnalysis staff" not in text:
    text = text.replace(old2, new2)

path.write_text(text)

print("Operations Analysis UI connected.")
