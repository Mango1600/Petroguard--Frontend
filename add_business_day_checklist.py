from pathlib import Path

path = Path("src/pages/BusinessDayClose.jsx")
text = path.read_text()

checklist = """
      {Object.keys(checks).length > 0 && (
        <div
          style={{
            marginTop: "20px",
            padding: "15px",
            border: "1px solid #ccc",
            borderRadius: "8px"
          }}
        >
          <h3>🔒 Business Day Close Check</h3>

          <p>
            {checks.attendance
              ? "🟢 Attendance Completed"
              : "🔴 Attendance Pending"}
          </p>

          <p>
            {checks.pump_readings
              ? "🟢 Pump Readings Completed"
              : "🔴 Pump Readings Pending"}
          </p>

          <p>
            {checks.tank_dip
              ? "🟢 Tank Dip Completed / Not Required"
              : "🔴 Tank Dip Pending"}
          </p>

          <p>
            {checks.payment_summary
              ? "🟢 Payment Summary Submitted"
              : "🔴 Payment Summary Pending"}
          </p>

          <p>
            {checks.manager_approval
              ? "🟢 Manager Approval Completed / Not Required"
              : "🔴 Manager Approval Pending"}
          </p>

        </div>
      )}
"""

if "Business Day Close Check" not in text:
    text = text.replace(
        "      <p>{message}</p>",
        "      <p>{message}</p>\n" + checklist
    )

path.write_text(text)

print("Business Day checklist added successfully.")
