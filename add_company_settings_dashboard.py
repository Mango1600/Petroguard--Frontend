from pathlib import Path

path = Path("src/pages/Dashboard.jsx")
text = path.read_text()

# Import
old = 'import BusinessDayClose from "./BusinessDayClose";'
new = '''import BusinessDayClose from "./BusinessDayClose";
import CompanySettings from "./CompanySettings";'''

if old in text and "CompanySettings" not in text:
    text = text.replace(old, new)

# State
old = 'const [showBusinessDayClose, setShowBusinessDayClose] = useState(false);'
new = '''const [showBusinessDayClose, setShowBusinessDayClose] = useState(false);
const [showCompanySettings, setShowCompanySettings] = useState(false);'''

if old in text and "showCompanySettings" not in text:
    text = text.replace(old, new)

# Button
old = '''{showBusinessDayClose
          ? "Hide Business Day Close"
          : "Open Business Day Close"}
      </button>'''

new = '''{showBusinessDayClose
          ? "Hide Business Day Close"
          : "Open Business Day Close"}
      </button>

      <button onClick={() => setShowCompanySettings(!showCompanySettings)}>
        {showCompanySettings
          ? "Hide Company Settings"
          : "Open Company Settings"}
      </button>'''

if old in text and "Open Company Settings" not in text:
    text = text.replace(old, new)

# Component
old = '''{showBusinessDayClose && (
        <BusinessDayClose staff={staff} />
      )}'''

new = '''{showBusinessDayClose && (
        <BusinessDayClose staff={staff} />
      )}

      {showCompanySettings && (
        <CompanySettings />
      )}'''

if old in text and "<CompanySettings" not in text:
    text = text.replace(old, new)

path.write_text(text)

print("Company Settings added to Dashboard successfully.")
