from pathlib import Path

path = Path("src/pages/CashDeclaration.jsx")
text = path.read_text()

# Navigation import
if 'useNavigate' not in text:
    text = text.replace(
        'import { useState',
        'import { useState'
    )
    text = text.replace(
        'from "react";',
        'from "react";\nimport { useNavigate } from "react-router-dom";'
    )

# Navigator
if 'const navigate = useNavigate();' not in text:
    text = text.replace(
        'export default function CashDeclaration',
        'export default function CashDeclaration'
    )
    text = text.replace(
        '{',
        '{\n  const navigate = useNavigate();',
        1
    )

# After successful save
text = text.replace(
    'setMessage("Declaration saved successfully.");',
    '''setMessage("Declaration saved successfully.");
navigate("/shift-reconciliation");'''
)

path.write_text(text)
print("Module 2 Cash Declaration integration completed.")
