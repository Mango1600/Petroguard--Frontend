export default function VerificationCard({
  status = "Pending",
  risk = "Low",
  manager = null,
  owner = null,
  comment = ""
}) {
  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "12px",
        borderRadius: "8px",
        marginTop: "10px",
        background: "#fafafa"
      }}
    >
      <h4>Verification</h4>

      <p><strong>Status:</strong> {status}</p>

      <p><strong>Risk Level:</strong> {risk}</p>

      <p>
        <strong>Manager:</strong>{" "}
        {manager || "Pending"}
      </p>

      <p>
        <strong>Owner:</strong>{" "}
        {owner || "Pending"}
      </p>

      <p>
        <strong>Comment:</strong>{" "}
        {comment || "No comments"}
      </p>
    </div>
  );
}
