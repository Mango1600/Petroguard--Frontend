from pathlib import Path

path = Path("src/pages/PaymentSummary.jsx")
text = path.read_text()

# Add loadPaymentStatus() before savePayment()
if "async function loadPaymentStatus()" not in text:
    marker = "async function savePayment(status) {"

    load_function = '''
  async function loadPaymentStatus() {
    const today = new Date().toISOString().split("T")[0];

    const { data, error } = await supabase
      .from("daily_reconciliation")
      .select("status")
      .eq("station_id", staff.station_id)
      .eq("reconciliation_date", today)
      .maybeSingle();

    if (!error && data) {
      setPaymentStatus(data.status || "Draft");
    }
  }

'''

    text = text.replace(marker, load_function + marker)

# Call it from useEffect()
if "loadPaymentStatus();" not in text:
    text = text.replace(
        "useEffect(() => {",
        """useEffect(() => {
    loadPaymentStatus();
"""
    )

path.write_text(text)
print("loadPaymentStatus() added successfully.")
