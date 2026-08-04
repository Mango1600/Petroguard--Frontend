from pathlib import Path

file = Path("src/pages/FuelSales.jsx")

text = file.read_text()

text = text.replace(
"function FuelSales() {",
"function FuelSales({ salesContext }) {"
)

text = text.replace(
"const [stationId, setStationId] = useState(\"\");",
"const [stationId, setStationId] = useState(\"\");"
)

text = text.replace(
"pump_id: Number(pumpId),",
"pump_id: salesContext?.pump_id || Number(pumpId),"
)

text = text.replace(
"station_id: Number(stationId),",
"station_id: salesContext?.business_day_id ? stationId : Number(stationId),"
)

text = text.replace(
"payment_method: paymentMethod,",
"""payment_method: paymentMethod,
          pump_shift_id: salesContext?.pump_shift_id || null,
          staff_id: salesContext?.staff_id || null,"""
)

file.write_text(text)

print("FuelSales context patch complete")
