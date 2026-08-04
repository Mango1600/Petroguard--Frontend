from pathlib import Path

path = Path("src/pages/Dashboard.jsx")
text = path.read_text()

# Import
old = 'import ManagerApproval from "./ManagerApproval";'
new = '''import ManagerApproval from "./ManagerApproval";
import BusinessDayClose from "./BusinessDayClose";'''

if old in text and "BusinessDayClose" not in text:
    text = text.replace(old, new)

# State
old = 'const [showManagerApproval, setShowManagerApproval] = useState(false);'
new = '''const [showManagerApproval, setShowManagerApproval] = useState(false);
const [showBusinessDayClose, setShowBusinessDayClose] = useState(false);'''

if old in text and "showBusinessDayClose" not in text:
    text = text.replace(old, new)

# Button
old = '''{showManagerApproval
          ? "Hide Manager Approval"
          : "Open Manager Approval"}
      </button>'''

new = '''{showManagerApproval
          ? "Hide Manager Approval"
          : "Open Manager Approval"}
      </button>

      <button onClick={() => setShowBusinessDayClose(!showBusinessDayClose)}>
        {showBusinessDayClose
          ? "Hide Business Day Close"
          : "Open Business Day Close"}
      </button>'''

if old in text and "Open Business Day Close" not in text:
    text = text.replace(old, new)

# Component
old = '''{showManagerApproval && (
        <ManagerApproval staff={staff} />
      )}'''

new = '''{showManagerApproval && (
        <ManagerApproval staff={staff} />
      )}

      {showBusinessDayClose && (
        <BusinessDayClose staff={staff} />
      )}'''

if old in text and "<BusinessDayClose" not in text:
    text = text.replace(old, new)

path.write_text(text)

print("Business Day Close added to Dashboard successfully.")
