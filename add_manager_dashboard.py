from pathlib import Path

path = Path("src/pages/Dashboard.jsx")
text = path.read_text()

# Add import
old = 'import PaymentSummary from "./PaymentSummary";'
new = '''import PaymentSummary from "./PaymentSummary";
import ManagerApproval from "./ManagerApproval";'''

if old in text and 'import ManagerApproval' not in text:
    text = text.replace(old, new)

# Add state
old = 'const [showPaymentSummary, setShowPaymentSummary] = useState(false);'
new = '''const [showPaymentSummary, setShowPaymentSummary] = useState(false);
const [showManagerApproval, setShowManagerApproval] = useState(false);'''

if old in text and "showManagerApproval" not in text:
    text = text.replace(old, new)

# Add button
old = '''{showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>'''

new = '''{showPaymentSummary ? "Hide Payment Summary" : "Open Payment Summary"}
      </button>

      <button onClick={() => setShowManagerApproval(!showManagerApproval)}>
        {showManagerApproval
          ? "Hide Manager Approval"
          : "Open Manager Approval"}
      </button>'''

if old in text and "Open Manager Approval" not in text:
    text = text.replace(old, new)

# Add component
old = '{showPaymentSummary && <PaymentSummary staff={staff} />}'

new = '''{showPaymentSummary && <PaymentSummary staff={staff} />}

      {showManagerApproval && (
        <ManagerApproval staff={staff} />
      )}'''

if old in text and "<ManagerApproval" not in text:
    text = text.replace(old, new)

path.write_text(text)

print("Manager Approval module added successfully.")
