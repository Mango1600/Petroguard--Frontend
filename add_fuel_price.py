from pathlib import Path

file = Path("src/pages/PumpReadings.jsx")

text = file.read_text()

text = text.replace(
'const [shifts, setShifts] = useState([]);',
'''const [shifts, setShifts] = useState([]);
  const [fuelPrices, setFuelPrices] = useState([]);'''
)

text = text.replace(
'''supabase
        .from("staff_shifts")
        .select("*")
        .order("id"),''',
'''supabase
        .from("staff_shifts")
        .select("*")
        .order("id"),

      supabase
        .from("fuel_prices")
        .select("*")
        .order("effective_date", { ascending: false }),'''
)

text = text.replace(
'''setShifts(shiftResult.data || []);
    setLoading(false);''',
'''setShifts(shiftResult.data || []);
    setFuelPrices(shiftResult.data || []);
    setLoading(false);'''
)

text = text.replace(
'''function getShift(shiftId) {
    return shifts.find((s) => s.id === shiftId);
  }''',
'''function getShift(shiftId) {
    return shifts.find((s) => s.id === shiftId);
  }

  function getFuelPrice(productType) {
    const price = fuelPrices.find(
      (p) => p.product_type === productType
    );

    return price ? price.unit_price : 0;
  }'''
)

file.write_text(text)

print("Fuel price support added")
