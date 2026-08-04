from pathlib import Path

file = Path("src/pages/Dashboard.jsx")

text = file.read_text()

text = text.replace(
    'import FuelSales from "./FuelSales";',
    'import ShiftReconciliation from "./ShiftReconciliation";'
)

text = text.replace(
    'const [showFuelSales, setShowFuelSales] = useState(false);',
    'const [showShiftReconciliation, setShowShiftReconciliation] = useState(false);'
)

text = text.replace(
    'setShowFuelSales(!showFuelSales)',
    'setShowShiftReconciliation(!showShiftReconciliation)'
)

text = text.replace(
    '{showFuelSales ? "Hide Fuel Sales" : "Open Fuel Sales"}',
    '{showShiftReconciliation ? "Hide Shift Reconciliation" : "Open Shift Reconciliation"}'
)

text = text.replace(
    '{showFuelSales && <FuelSales />}',
    '{showShiftReconciliation && <ShiftReconciliation />'
)

file.write_text(text)

print("Dashboard patched successfully")
