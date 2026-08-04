export default function MeterSalesSummary({litres, amount}) {
  return (
    <div>
      <h3>Sales Summary</h3>
      <p>Total Litres: {litres}</p>
      <p>Total Sales: ₦{amount}</p>
    </div>
  );
}
