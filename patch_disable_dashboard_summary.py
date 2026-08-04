from pathlib import Path

p = Path("src/pages/Dashboard.jsx")
text = p.read_text()

text = text.replace(
"  loadDashboardSummary();",
'  // loadDashboardSummary();'
)

p.write_text(text)
print("Dashboard summary disabled.")
