from pathlib import Path

path = Path("src/pages/Dashboard.jsx")

text = path.read_text()

if 'OperationsAnalysis' not in text:
    text = text.replace(
        'import PaymentSummary from "./PaymentSummary";',
        'import PaymentSummary from "./PaymentSummary";\nimport OperationsAnalysis from "./OperationsAnalysis";'
    )

if 'showOperationsAnalysis' not in text:
    text = text.replace(
        'const [showPaymentSummary, setShowPaymentSummary] = useState(false);',
        'const [showPaymentSummary, setShowPaymentSummary] = useState(false);\nconst [showOperationsAnalysis, setShowOperationsAnalysis] = useState(false);'
    )

if 'OperationsAnalysis' not in text.split("return")[0]:
    pass

path.write_text(text)

print("Operations Analysis import/state added.")
