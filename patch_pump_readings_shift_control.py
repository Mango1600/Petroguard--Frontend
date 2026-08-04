from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
'.from("staff_shifts")',
'.from("pump_shifts")'
)

text = text.replace(
'reading.staff_shift_id || "Not assigned"',
'reading.pump_shift_id || "Not assigned"'
)

file.write_text(text)

print("Pump Readings shift control patched")
