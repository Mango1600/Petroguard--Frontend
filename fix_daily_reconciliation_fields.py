from pathlib import Path

f = Path("src/pages/DailyReconciliation.jsx")
t = f.read_text()

t = t.replace("<th>Litres Sold</th>", "<th>Fuel Sales</th>")
t = t.replace("<th>Payments</th>", "<th>Total Collected</th>")
t = t.replace("<th>Stock Variance</th>", "<th>Variance</th>")

t = t.replace(
    "<td>{row.litres_sold || 0}</td>",
    "<td>₦{Number(row.fuel_sales || 0).toLocaleString()}</td>"
)

t = t.replace(
    "<td>₦{Number(row.total_collected || 0).toLocaleString()}</td>",
    """<td>
₦{Number(
(row.cash_sales || 0) +
(row.pos_sales || 0) +
(row.transfer_sales || 0) +
(row.credit_sales_amount || 0)
).toLocaleString()}
</td>"""
)

t = t.replace(
    "<td>{row.stock_variance || 0}</td>",
    "<td>₦{Number(row.variance || 0).toLocaleString()}</td>"
)

f.write_text(t)

print("✅ DailyReconciliation fields aligned")
