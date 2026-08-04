from pathlib import Path

path = Path("src/pages/ShiftClose.jsx")

text = path.read_text()

text = text.replace(
    'import { useNavigate } from "react-router-dom";\n',
    ''
)

text = text.replace(
    '  const navigate = useNavigate();\n',
    ''
)

text = text.replace(
    '          navigate("/cash-declaration");\n',
    ''
)

path.write_text(text)

print("ShiftClose router dependency removed.")
