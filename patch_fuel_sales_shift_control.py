from pathlib import Path

file = Path("src/pages/FuelSales.jsx")

text = file.read_text()

text = text.replace(
'''const [paymentMethod, setPaymentMethod] = useState("Cash");''',
'''const [paymentMethod, setPaymentMethod] = useState("Cash");
  const [activeShift, setActiveShift] = useState(null);
  const [activeAssignment, setActiveAssignment] = useState(null);'''
)

text = text.replace(
'''if (!stationId || !pumpId || !openingMeter || !closingMeter || !unitPrice) {
      return;
    }''',
'''if (!stationId || !pumpId || !openingMeter || !closingMeter || !unitPrice) {
      return;
    }

    const { data: shift } = await supabase
      .from("pump_shifts")
      .select("*")
      .eq("pump_id", Number(pumpId))
      .eq("status", "OPEN")
      .single();

    if (!shift) {
      alert("No active Pump Shift found for this pump");
      return;
    }

    const { data: assignment } = await supabase
      .from("attendant_assignments")
      .select("*")
      .eq("pump_shift_id", shift.id)
      .eq("status", "ACTIVE")
      .single();

    if (!assignment) {
      alert("No active attendant assignment found");
      return;
    }'''
)

text = text.replace(
'''pump_id: Number(pumpId),
          quantity: quantity,''',
'''pump_id: Number(pumpId),
          pump_shift_id: shift.id,
          staff_id: assignment.staff_id,
          quantity: quantity,'''
)

file.write_text(text)

print("Fuel Sales Pump Shift control patch complete")
