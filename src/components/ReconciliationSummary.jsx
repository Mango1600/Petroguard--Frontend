
export default function ReconciliationSummary({ records = [] }) {
  const totalFuelSales = records.reduce(
    (sum, r) => sum + Number(r.fuel_sales || 0),
    0
  );

  const totalCash = records.reduce(
    (sum, r) => sum + Number(r.cash_sales || 0),
    0
  );

  const totalPOS = records.reduce(
    (sum, r) => sum + Number(r.pos_sales || 0),
    0
  );

  const totalCredit = records.reduce(
    (sum, r) => sum + Number(r.credit_sales_amount || 0),
    0
  );

  const totalVariance = records.reduce(
    (sum, r) => sum + Number(r.variance || 0),
    0
  );

  return (
    <div
      style={{
        border: "1px solid #ddd",
        padding: "12px",
        borderRadius: "8px",
        marginBottom: "20px",
      }}
    >
      <h3>Summary</h3>

      <p>Total Fuel Sales: {totalFuelSales}</p>
      <p>Total Cash: {totalCash}</p>
      <p>Total POS: {totalPOS}</p>
      <p>Total Credit: {totalCredit}</p>
      <p>Total Variance: {totalVariance}</p>
    </div>
  );
}
