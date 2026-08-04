from pathlib import Path

path = Path("src/pages/AttendantDashboard.jsx")

text = path.read_text()

# import CashDeclaration
if 'import CashDeclaration' not in text:
    text = text.replace(
        'import ShiftClose from "./ShiftClose";',
        '''import ShiftClose from "./ShiftClose";
import CashDeclaration from "./CashDeclaration";'''
    )

# add cash page state handling
controller = '''
if (page === "cash-declaration") {
  return (
    <CashDeclaration
      staff={staff}
      onComplete={() => {
        setPage("dashboard");
        loadPumpShift();
      }}
    />
  );
}

'''

if controller not in text:
    text = text.replace(
        'if (page === "shift-close") {',
        controller + 'if (page === "shift-close") {'
    )

path.write_text(text)

print("Cash Declaration controller added.")
