export default function BusinessDayStatus({ businessDay }) {
  const isOpen = businessDay?.status === "OPEN";

  return (
    <div className="card">
      <h3>Business Day Status</h3>

      <p>
        <strong>Status:</strong>{" "}
        {isOpen ? "🟢 OPEN" : "🔴 CLOSED"}
      </p>

      <p>
        <strong>Date:</strong>{" "}
        {businessDay?.business_date || "-"}
      </p>

      <p>
        <strong>Opened:</strong>{" "}
        {businessDay?.opened_at
          ? new Date(businessDay.opened_at).toLocaleString()
          : "-"}
      </p>

      <p>
        <strong>Closed:</strong>{" "}
        {businessDay?.closed_at
          ? new Date(businessDay.closed_at).toLocaleString()
          : "Not Closed"}
      </p>
    </div>
  );
}
