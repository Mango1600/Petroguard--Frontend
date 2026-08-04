from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

old = """<p>ID: {reading.id}</p>
            <p>Station: {getStationName(reading.station_id)}</p>
            <p>Opening Meter: {reading.opening_meter}</p>
            <p>Closing Meter: {reading.closing_meter}</p>
<p>
  Litres Sold: {Number(reading.closing_meter) - Number(reading.opening_meter)} L
</p>
            <p>Variance: {reading.variance}</p>

            <p>Status: {reading.status}</p>"""

new = """<h3>Pump Transaction #{reading.id}</h3>

            <p>Station: {getStationName(reading.station_id)}</p>

            <p>Product: {reading.product_type || "Not set"}</p>

            <p>Opening Meter: {reading.opening_meter} L</p>

            <p>Closing Meter: {reading.closing_meter} L</p>

            <p>
              Litres Sold: {Number(reading.closing_meter) - Number(reading.opening_meter)} L
            </p>

            <hr />

            <h4>Sales Calculation</h4>

            <p>
              Unit Price: ₦{Number(reading.unit_price).toLocaleString()}
            </p>

            <p>
              Expected Sales: ₦{Number(reading.expected_sales).toLocaleString()}
            </p>

            <hr />

            <h4>Payment Summary</h4>

            <p>Cash: ₦{Number(reading.cash_sales).toLocaleString()}</p>
            <p>POS: ₦{Number(reading.pos_sales).toLocaleString()}</p>
            <p>Transfer: ₦{Number(reading.transfer_sales).toLocaleString()}</p>
            <p>Credit: ₦{Number(reading.credit_sales).toLocaleString()}</p>

            <p>
              Total Collected: ₦{Number(reading.total_collected).toLocaleString()}
            </p>

            <p>
              Sales Variance: ₦{Number(reading.sales_variance).toLocaleString()}
            </p>

            <p>Status: {reading.status}</p>"""

if old in text:
    text = text.replace(old, new)
    file.write_text(text)
    print("PumpReadings.jsx updated successfully")
else:
    print("Old section not found")
