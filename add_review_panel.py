from pathlib import Path

path = Path("src/pages/ManagerApproval.jsx")
text = path.read_text()

panel = '''
      {selectedRecord && (
        <div
          style={{
            border: "2px solid #0a7",
            padding: "15px",
            marginBottom: "20px",
            borderRadius: "8px",
          }}
        >
          <h3>📋 Manager Review</h3>

          <p><b>Business Date:</b> {selectedRecord.reconciliation_date}</p>
          <p><b>Station ID:</b> {selectedRecord.station_id}</p>
          <p><b>Status:</b> {selectedRecord.status}</p>

          <hr />

          <p><b>Expected Revenue:</b> ₦{Number(selectedRecord.expected_revenue || 0).toLocaleString()}</p>

          <p><b>Actual Collection:</b> ₦{(
            Number(selectedRecord.cash_sales || 0) +
            Number(selectedRecord.pos_sales || 0) +
            Number(selectedRecord.transfer_sales || 0) +
            Number(selectedRecord.credit_sales_amount || 0)
          ).toLocaleString()}</p>

          <p><b>Variance:</b> ₦{Number(selectedRecord.revenue_variance || 0).toLocaleString()}</p>

          <button onClick={() => approve(selectedRecord.id)}>
            ✅ Approve
          </button>

          <button
            style={{marginLeft:"10px"}}
            onClick={() => reject(selectedRecord.id)}
          >
            ❌ Reject
          </button>

          <button
            style={{marginLeft:"10px"}}
            onClick={() => setSelectedRecord(null)}
          >
            Close
          </button>
        </div>
      )}
'''

if "📋 Manager Review" not in text:
    text = text.replace(
        '<h2>📋 Manager Approval Dashboard</h2>',
        '<h2>📋 Manager Approval Dashboard</h2>\n' + panel
    )

path.write_text(text)

print("Manager Review panel added successfully.")
