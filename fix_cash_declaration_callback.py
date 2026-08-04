from pathlib import Path

path = Path("src/pages/CashDeclaration.jsx")

text = path.read_text()

# accept callback prop
text = text.replace(
    'export default function CashDeclaration({ shiftData }) {',
    'export default function CashDeclaration({ shiftData, onComplete }) {'
)

# trigger callback after successful submit
text = text.replace(
    'setMessage(\n"Cash declaration submitted"\n);',
    '''setMessage(
"Cash declaration submitted"
);

if(onComplete){
  onComplete();
}'''
)

path.write_text(text)

print("CashDeclaration callback added.")
