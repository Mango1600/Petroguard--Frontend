from pathlib import Path

path = Path("src/pages/ShiftClose.jsx")
text = path.read_text()

# Add navigation
if 'useNavigate' not in text:
    text = text.replace(
        'import { useEffect, useState } from "react";',
        'import { useEffect, useState } from "react";\nimport { useNavigate } from "react-router-dom";'
    )

if 'const navigate = useNavigate();' not in text:
    text = text.replace(
        'export default function ShiftClose({ staff }) {',
        'export default function ShiftClose({ staff }) {\n  const navigate = useNavigate();'
    )

# After closing video completes, go to Cash Declaration
old = """        onComplete={async () => {
          setShowVideo(false);
        }}"""

new = """        onComplete={async () => {
          setShowVideo(false);
          navigate("/cash-declaration");
        }}"""

text = text.replace(old, new)

path.write_text(text)
print("Module 1 Shift Close integration completed.")
