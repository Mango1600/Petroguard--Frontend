from pathlib import Path

file = Path("src/pages/Dashboard.jsx")

text = file.read_text()

# Add state
text = text.replace(
"const [modulePermissions, setModulePermissions] = useState([]);",
"""const [modulePermissions, setModulePermissions] = useState([]);
  const [dashboardSummary, setDashboardSummary] = useState(null);"""
)

# Add function before useEffect
marker = "useEffect(() => {"

function = """
async function loadDashboardSummary() {
  const { data, error } = await supabase
    .from("dashboard_summary")
    .select("*")
    .single();

  if (error) {
    console.log("Dashboard summary error:", error);
    return;
  }

  setDashboardSummary(data);
}

"""

text = text.replace(marker, function + marker)

# Add function call
text = text.replace(
"loadStationPolicy();",
"""loadStationPolicy();
  loadDashboardSummary();"""
)

# Replace KPI values
text = text.replace(
"""<p>⛽ Litres Sold: 0 L</p>
<p>💰 Expected Revenue: ₦0.00</p>
<p>💵 Cash Received: ₦0.00</p>
<p>💳 POS Sales: ₦0.00</p>
<p>🏦 Bank Transfers: ₦0.00</p>
<p>📒 Credit Sales: ₦0.00</p>""",
"""<p>
⛽ Litres Sold: {dashboardSummary?.total_liters_sold || 0} L
</p>

<p>
💰 Expected Revenue: ₦{Number(dashboardSummary?.total_revenue || 0).toLocaleString()}
</p>

<p>
📊 Transactions: {dashboardSummary?.total_transactions || 0}
</p>

<p>💵 Cash Received: ₦0.00</p>
<p>💳 POS Sales: ₦0.00</p>
<p>🏦 Bank Transfers: ₦0.00</p>
<p>📒 Credit Sales: ₦0.00</p>"""
)

file.write_text(text)

print("Dashboard summary connected successfully")
