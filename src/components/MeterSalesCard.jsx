export default function MeterSalesCard({opening, closing, litres, amount}) {
  return (
    <div>
      <h3>Meter Sales</h3>
      <p>Opening: {opening}</p>
      <p>Closing: {closing}</p>
      <p>Litres Sold: {litres}</p>
      <p>Total Amount: ₦{amount}</p>
    </div>
  );
}
