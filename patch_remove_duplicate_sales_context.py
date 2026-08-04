from pathlib import Path

file = Path("src/pages/FuelSales.jsx")

text = file.read_text()

text = text.replace(
"""          pump_shift_id: salesContext?.pump_shift_id || null,
          staff_id: salesContext?.staff_id || null,""",
""
)

file.write_text(text)

print("Duplicate sales context fields removed")
