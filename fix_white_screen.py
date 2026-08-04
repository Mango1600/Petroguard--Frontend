from pathlib import Path

f = Path("src/pages/AttendantDashboard.jsx")
text = f.read_text()

text = text.replace(
    'const [page, setPage] = useState("shiftStatus");',
    'const [page, setPage] = useState("menu");'
)

text = text.replace(
    'if (page === "shiftStatus")',
    'if (false && page === "shiftStatus")'
)

text = text.replace(
    'return (',
    'if (page == "menu") return (',
    1
)

f.write_text(text)

print("✅ White screen bypass applied.")
