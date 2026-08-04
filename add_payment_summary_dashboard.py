from pathlib import Path

file = Path("src/pages/Dashboard.jsx")

content = file.read_text()

if 'import PaymentSummary from "./PaymentSummary";' not in content:
    content = content.replace(
        'import BusinessDayManagement from "./BusinessDayManagement";',
        'import BusinessDayManagement from "./BusinessDayManagement";\nimport PaymentSummary from "./PaymentSummary";'
    )

if 'showPaymentSummary' not in content:
    content = content.replace(
        'const [showBusinessDayManagement, setShowBusinessDayManagement] = useState(false);',
        'const [showBusinessDayManagement, setShowBusinessDayManagement] = useState(false);\nconst [showPaymentSummary, setShowPaymentSummary] = useState(false);'
    )

if 'Open Payment Summary' not in content:
    content = content.replace(
        'Open Business Day Management',
        'Open Business Day Management\n<button onClick={() => setShowPaymentSummary(!showPaymentSummary)}>\n{showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}\n</button>'
    )

if '<PaymentSummary' not in content:
    content += '\n\n{showPaymentSummary && <PaymentSummary staff={staff} />}\n'

file.write_text(content)

print("Payment Summary connected to Dashboard successfully")
