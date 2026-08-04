from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
'''.from("pump_readings")
        .select("*")
        .order("id")''',
'''.from("pump_readings")
        .select(`
          *,
          pumps(
            pump_name,
            product_type
          )
        `)
        .order("id")'''
)

text = text.replace(
'''<p>Product: {reading.product_type || "Not set"}</p>''',
'''<p>
              Pump: {reading.pumps?.pump_name || `Pump ${reading.pump_id}`}
            </p>

            <p>
              Product: {reading.pumps?.product_type || "Not set"}
            </p>'''
)

file.write_text(text)

print("Pump details added successfully")
