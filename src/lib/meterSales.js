export function calculateSales(openingMeter, closingMeter, unitPrice) {
  const litresSold = closingMeter - openingMeter;
  const totalAmount = litresSold * unitPrice;

  return {
    litresSold,
    totalAmount,
  };
}
