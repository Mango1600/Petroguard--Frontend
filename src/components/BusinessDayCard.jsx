export default function BusinessDayCard({
  businessDay,
  stationName,
  onOpen,
  onClose,
  loading,
}) {
  const isOpen = businessDay?.status === "OPEN";

  return (
    <div className="card">
      <h2>🏢 Business Day</h2>

      <p>
        <strong>Station:</strong> {stationName || "-"}
      </p>

      <p>
        <strong>Date:</strong>{" "}
        {businessDay?.business_date || new Date().toISOString().slice(0, 10)}
      </p>

      <p>
        <strong>Status:</strong>{" "}
        {isOpen ? "🟢 OPEN" : "🔴 CLOSED"}
      </p>

      {!isOpen ? (
        <button onClick={onOpen} disabled={loading}>
          Open Business Day
        </button>
      ) : (
        <button onClick={onClose} disabled={loading}>
          Close Business Day
        </button>
      )}
    </div>
  );
}
