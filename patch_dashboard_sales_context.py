from pathlib import Path

file = Path("src/pages/Dashboard.jsx")

text = file.read_text()

text = text.replace(
'''const [showPaymentSummary, setShowPaymentSummary] = useState(false);''',
'''const [showPaymentSummary, setShowPaymentSummary] = useState(false);
  const [salesContext, setSalesContext] = useState(null);'''
)

text = text.replace(
'''<AttendantDashboard staff={staff} />''',
'''<AttendantDashboard
        staff={staff}
        openSales={(context) => {
          setSalesContext(context);
          setShowFuelSales(true);
        }}
      />'''
)

text = text.replace(
'''{showFuelSales && <FuelSales />}''',
'''{showFuelSales && (
        <FuelSales salesContext={salesContext} />
      )}'''
)

file.write_text(text)

print("Dashboard sales context connected")
