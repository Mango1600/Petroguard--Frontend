from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

old = """<p>
              Unit Price: ₦{Number(reading.unit_price).toLocaleString()}
            </p>

            <p>
              Expected Sales: ₦{Number(reading.expected_sales).toLocaleString()}
            </p>"""

new = """<p>
              Unit Price:
              ₦{Number(
                getFuelPrice(reading.pumps?.product_type)
              ).toLocaleString()}
            </p>

            <p>
              Expected Sales:
              ₦{(
                (Number(reading.closing_meter) -
                Number(reading.opening_meter)) *
                Number(getFuelPrice(reading.pumps?.product_type))
              ).toLocaleString()}
            </p>"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("Revenue display added successfully")
else:
    print("Revenue section not found")
